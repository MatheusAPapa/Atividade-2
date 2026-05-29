# ============================================================
#   FUNÇÕES DE ENTREGADORES - FluxoNorte
#   Cadastro, edição, consulta e gerenciamento de entregadores
# ============================================================

import random
import banco
import utilidade

# ============================================================
# GERAÇÃO DE ID
# ============================================================

def gerar_idEntreg():
    """Gera um ID único de 4 dígitos para o entregador."""
    while True:
        novo_id = str(random.randint(1000, 9999))
        if novo_id not in banco.entregadores:
            return novo_id

# ============================================================
# CADASTRO
# ============================================================

def cadastrarEntrg(id_entregador, nome_entregador, cpf_entregador, veiculo_entregador):
    """Cadastra um novo entregador no banco de dados."""
    entregador = {
        'id'     : id_entregador,
        'nome'   : nome_entregador,
        'cpf'    : cpf_entregador,
        'veiculo': veiculo_entregador,
        'status' : 'D',        # D = Disponível, E = Em entrega, S = Suspenso
        'pedidos': []
    }
    banco.entregadores[id_entregador] = entregador

# ============================================================
# EDIÇÃO
# ============================================================

def editarEntrg(entregador):
    """Permite editar os dados de um entregador."""
    print('''
================================
         Editar Dados
================================
  1 - Nome
  2 - CPF
  3 - Veículo
  4 - Voltar
    ''')
    opcao = input('  Digite sua escolha: ').strip()
    match opcao:
        case '1':
            novo = input('  Novo nome: ').strip()
            if novo:
                entregador['nome'] = novo
                print('  Nome atualizado!')
        case '2':
            novo = input('  Novo CPF: ').strip()
            if novo:
                entregador['cpf'] = novo
                print('  CPF atualizado!')
        case '3':
            print('''
  Veículos disponíveis:
  1 - Carro
  2 - Moto
  3 - Van
  4 - Caminhão
            ''')
            op = input('  Escolha: ').strip()
            mapa = {'1': 'carro', '2': 'moto', '3': 'van', '4': 'caminhao'}
            if op in mapa:
                entregador['veiculo'] = mapa[op]
                print('  Veículo atualizado!')
            else:
                print('  Opção inválida.')
        case '4':
            return
        case _:
            print('  Opção inválida.')
    input('\n  Pressione Enter para continuar. ')

# ============================================================
# SUSPENDER / REATIVAR
# ============================================================

def suspenderOuReativarEntrg():
    """Suspende ou reativa um entregador."""
    id_ent = input('  ID do entregador: ').strip()

    if id_ent not in banco.entregadores:
        print('  Entregador não encontrado.')
        input('\n  Pressione Enter para voltar. ')
        return

    ent = banco.entregadores[id_ent]

    if ent['status'] == 'S':
        ent['status'] = 'D'
        print(f"  Entregador {ent['nome']} reativado com sucesso.")
    elif ent['status'] == 'E':
        print('  Entregador está em rota de entrega. Finalize os pedidos antes de suspender.')
    else:
        ent['status'] = 'S'
        print(f"  Entregador {ent['nome']} suspenso.")

    input('\n  Pressione Enter para continuar. ')

# ============================================================
# LISTAGENS
# ============================================================

def _status_label(s):
    if s == 'D': return 'Disponível'
    if s == 'E': return 'Em rota de entrega'
    if s == 'S': return 'Suspenso'
    return s

def listarEntrg():
    """Lista todos os entregadores cadastrados."""
    utilidade.limpar_tela()
    print('''
================================
       Todos os Entregadores
================================
    ''')
    if not banco.entregadores:
        print('  Nenhum entregador cadastrado.')
        return
    for e in banco.entregadores.values():
        print(f"  ID: {e['id']} | Nome: {e['nome']} | CPF: {e['cpf']} | "
              f"Veículo: {e['veiculo']} | Status: {_status_label(e['status'])}")

def listarEntrgDisp():
    """Lista apenas os entregadores disponíveis."""
    if not banco.entregadores:
        print('  Nenhum entregador cadastrado.')
        return
    encontrou = False
    for e in banco.entregadores.values():
        if e['status'] == 'D':
            ativos = utilidade.pedidos_ativos_entregador(e['id'])
            print(f"  ID: {e['id']} | Nome: {e['nome']} | Veículo: {e['veiculo']} | "
                  f"Em rota: {ativos}/{banco.LIMITE_PEDIDOS_ENTREGADOR}")
            encontrou = True
    if not encontrou:
        print('  Nenhum entregador disponível no momento.')

def entregas_por_entregador():
    """Exibe todos os pedidos associados a um entregador."""
    id_ent = input('  ID do Entregador: ').strip()

    if id_ent not in banco.entregadores:
        print('  Entregador não encontrado.')
        input('\n  Pressione Enter para voltar. ')
        return

    ent = banco.entregadores[id_ent]
    print(f"\n  Entregador : {ent['nome']}")
    print(f"  Veículo    : {ent['veiculo']}")
    print(f"  Status     : {_status_label(ent['status'])}")
    print(f"  Total de pedidos associados: {len(ent['pedidos'])}")

    if not ent['pedidos']:
        print('  Nenhuma entrega registrada.')
    else:
        for pid in ent['pedidos']:
            if pid in banco.pedidos:
                utilidade.exibir_pedido(banco.pedidos[pid])
            else:
                print(f"  [!] Pedido {pid} não encontrado no sistema.")

    input('\n  Pressione Enter para continuar. ')