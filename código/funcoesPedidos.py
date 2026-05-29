# ============================================================
#   FUNÇÕES DE PEDIDOS - FluxoNorte
#   Cadastro, edição, consulta e gerenciamento de pedidos
# ============================================================

import random
import banco
import utilidade

# ============================================================
# GERAÇÃO DE ID
# ============================================================

def gerar_idPedido():
    """Gera um ID único no formato: 1 letra + 4 dígitos (ex: A1234)."""
    alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    while True:
        letra   = random.choice(alfabeto)
        numeros = random.randint(1000, 9999)
        novo_id = letra + str(numeros)
        if novo_id not in banco.pedidos:
            return novo_id

# ============================================================
# CADASTRO
# ============================================================

def cadastrarPedido(idPedido, nomeCliente, prod, ender, priorid, desc):
    """Cadastra um novo pedido no banco de dados."""
    pedido = {
        'id'           : idPedido,
        'nome'         : nomeCliente,
        'produto'      : prod,
        'endereco'     : ender,
        'prioridade'   : priorid,
        'descricao'    : desc,
        'status'       : 'Pendente',
        'id_entregador': ''
    }
    banco.pedidos[idPedido] = pedido
    return pedido

# ============================================================
# EDIÇÃO
# ============================================================

def editarPedido():
    """Permite editar campos de um pedido existente."""
    id_pedido = input('  Digite o ID do pedido: ').strip().upper()

    if id_pedido not in banco.pedidos:
        print('  Pedido não encontrado.')
        input('\n  Pressione Enter para voltar. ')
        return

    pedido = banco.pedidos[id_pedido]

    if pedido['status'] in ('Cancelado', 'Entregue'):
        print(f"  Pedido com status '{pedido['status']}' não pode ser editado.")
        input('\n  Pressione Enter para voltar. ')
        return

    utilidade.exibir_pedido(pedido)
    print('''
  O que deseja editar?
  1 - Nome do cliente
  2 - Produto
  3 - Endereço
  4 - Prioridade
  5 - Descrição
  6 - Voltar
    ''')

    opcao = input('  Escolha: ').strip()
    match opcao:
        case '1':
            novo = input('  Novo nome do cliente: ').strip()
            if novo:
                pedido['nome'] = novo
                print('  Nome atualizado!')
        case '2':
            novo = input('  Novo produto: ').strip()
            if novo:
                pedido['produto'] = novo
                print('  Produto atualizado!')
        case '3':
            novo = input('  Novo endereço: ').strip()
            if novo:
                pedido['endereco'] = novo
                print('  Endereço atualizado!')
        case '4':
            print('  Prioridade: [1] Alta  [2] Normal')
            op = input('  Escolha: ').strip()
            if op == '1':
                pedido['prioridade'] = 'Alta'
                print('  Prioridade atualizada!')
            elif op == '2':
                pedido['prioridade'] = 'Normal'
                print('  Prioridade atualizada!')
            else:
                print('  Opção inválida.')
        case '5':
            novo = input('  Nova descrição: ').strip()
            pedido['descricao'] = novo
            print('  Descrição atualizada!')
        case '6':
            return
        case _:
            print('  Opção inválida.')

    input('\n  Pressione Enter para continuar. ')

# ============================================================
# ATUALIZAÇÃO DE STATUS E ASSOCIAÇÕES
# ============================================================

def alterar_status():
    """Altera o status de um pedido."""
    id_pedido = input('  ID do Pedido: ').strip().upper()

    if id_pedido not in banco.pedidos:
        print('  Pedido não encontrado.')
        input('\n  Pressione Enter para voltar. ')
        return

    pedido = banco.pedidos[id_pedido]

    if pedido['status'] == 'Cancelado':
        print('  Pedido cancelado não pode ser alterado.')
        input('\n  Pressione Enter para voltar. ')
        return

    print(f"  Status atual: {pedido['status']}")
    print('  Novo status: [1] Pendente  [2] Em Rota  [3] Entregue')
    opcao = input('  Escolha: ').strip()
    mapa = {'1': 'Pendente', '2': 'Em Rota', '3': 'Entregue'}

    if opcao not in mapa:
        print('  Opção inválida.')
        input('\n  Pressione Enter para voltar. ')
        return

    novo_status = mapa[opcao]

    # Se marcado como Entregue, verifica se libera o entregador
    if novo_status == 'Entregue' and pedido['id_entregador']:
        id_ent = pedido['id_entregador']
        if id_ent in banco.entregadores:
            if utilidade.pedidos_ativos_entregador(id_ent) <= 1:
                banco.entregadores[id_ent]['status'] = 'D'

    pedido['status'] = novo_status
    print(f"  Status atualizado para '{novo_status}'.")
    input('\n  Pressione Enter para continuar. ')

def cancelar_pedido():
    """Cancela um pedido (irreversível)."""
    id_pedido = input('  ID do Pedido: ').strip().upper()

    if id_pedido not in banco.pedidos:
        print('  Pedido não encontrado.')
        input('\n  Pressione Enter para voltar. ')
        return

    pedido = banco.pedidos[id_pedido]

    if pedido['status'] == 'Cancelado':
        print('  Pedido já está cancelado.')
        input('\n  Pressione Enter para voltar. ')
        return

    confirma = input(f"  Confirmar cancelamento do pedido {id_pedido}? (s/n): ").strip().lower()
    if confirma != 's':
        print('  Cancelamento abortado.')
        input('\n  Pressione Enter para voltar. ')
        return

    # Remove associação com o entregador se houver
    id_ent = pedido['id_entregador']
    if id_ent and id_ent in banco.entregadores:
        lista = banco.entregadores[id_ent]['pedidos']
        if id_pedido in lista:
            lista.remove(id_pedido)
        if utilidade.pedidos_ativos_entregador(id_ent) == 0:
            banco.entregadores[id_ent]['status'] = 'D'

    pedido['status'] = 'Cancelado'
    pedido['id_entregador'] = ''
    print(f"  Pedido {id_pedido} cancelado com sucesso.")
    input('\n  Pressione Enter para continuar. ')

def associar_entregador():
    """Associa um entregador disponível a um pedido pendente."""
    id_pedido = input('  ID do Pedido: ').strip().upper()

    if id_pedido not in banco.pedidos:
        print('  Pedido não encontrado.')
        input('\n  Pressione Enter para voltar. ')
        return

    pedido = banco.pedidos[id_pedido]

    if pedido['status'] in ('Cancelado', 'Entregue'):
        print(f"  Pedido com status '{pedido['status']}' não pode receber entregador.")
        input('\n  Pressione Enter para voltar. ')
        return

    if pedido['id_entregador']:
        print(f"  Pedido já possui entregador: {pedido['id_entregador']}")
        input('\n  Pressione Enter para voltar. ')
        return

    id_ent = input('  ID do Entregador: ').strip()

    if id_ent not in banco.entregadores:
        print('  Entregador não encontrado.')
        input('\n  Pressione Enter para voltar. ')
        return

    entregador = banco.entregadores[id_ent]

    if entregador['status'] == 'S':
        print('  Entregador está suspenso e não pode receber pedidos.')
        input('\n  Pressione Enter para voltar. ')
        return

    ativos = utilidade.pedidos_ativos_entregador(id_ent)
    if ativos >= banco.LIMITE_PEDIDOS_ENTREGADOR:
        print(f"  Entregador atingiu o limite de {banco.LIMITE_PEDIDOS_ENTREGADOR} pedidos em rota.")
        input('\n  Pressione Enter para voltar. ')
        return

    pedido['id_entregador'] = id_ent
    pedido['status'] = 'Em Rota'
    entregador['pedidos'].append(id_pedido)
    entregador['status'] = 'E'

    print(f"  Pedido {id_pedido} associado ao entregador {id_ent} ({entregador['nome']}).")
    input('\n  Pressione Enter para continuar. ')

def remover_associacao():
    """Remove a associação entre pedido e entregador."""
    id_pedido = input('  ID do Pedido: ').strip().upper()

    if id_pedido not in banco.pedidos:
        print('  Pedido não encontrado.')
        input('\n  Pressione Enter para voltar. ')
        return

    pedido = banco.pedidos[id_pedido]

    if not pedido['id_entregador']:
        print('  Pedido não possui entregador associado.')
        input('\n  Pressione Enter para voltar. ')
        return

    id_ent = pedido['id_entregador']

    if id_ent in banco.entregadores:
        lista = banco.entregadores[id_ent]['pedidos']
        if id_pedido in lista:
            lista.remove(id_pedido)
        if utilidade.pedidos_ativos_entregador(id_ent) == 0:
            banco.entregadores[id_ent]['status'] = 'D'

    pedido['id_entregador'] = ''
    pedido['status'] = 'Pendente'
    print(f"  Associação removida. Pedido {id_pedido} voltou para 'Pendente'.")
    input('\n  Pressione Enter para continuar. ')

# ============================================================
# CONSULTAS
# ============================================================

def consultar_por_status(status):
    """Lista todos os pedidos com o status informado, Alta prioridade primeiro."""
    ids = [p for p in banco.pedidos if banco.pedidos[p]['status'] == status]
    ids_ordenados = utilidade.ordenar_pedidos_por_prioridade(ids)

    if not ids_ordenados:
        print(f"  Nenhum pedido com status '{status}'.")
    else:
        for pid in ids_ordenados:
            utilidade.exibir_pedido(banco.pedidos[pid])

def buscar_pedido_por_id():
    """Busca e exibe um pedido pelo ID."""
    id_pedido = input('  ID do Pedido: ').strip().upper()

    if id_pedido in banco.pedidos:
        utilidade.exibir_pedido(banco.pedidos[id_pedido])
    else:
        print('  Pedido não encontrado.')
    input('\n  Pressione Enter para continuar. ')

def listar_todos_pedidos():
    """Lista todos os pedidos cadastrados."""
    if not banco.pedidos:
        print('  Nenhum pedido cadastrado.')
        return
    ids_ordenados = utilidade.ordenar_pedidos_por_prioridade(list(banco.pedidos.keys()))
    for pid in ids_ordenados:
        utilidade.exibir_pedido(banco.pedidos[pid])
        