# ============================================================
#   MAIN - FluxoNorte / Operação Turno Crítico
#   Ponto de entrada — execute este arquivo para iniciar
# ============================================================

import banco
import menu
import utilidade
import funcoesPedidos
import funcoesEntregadores

# ============================================================
# RELATÓRIO DO DIA (Operações)
# ============================================================

def relatorio_do_dia():
    utilidade.limpar_tela()
    print('''
================================
        Relatório do Dia
================================
    ''')

    total = len(banco.pedidos)
    print(f"  Total de pedidos cadastrados : {total}")

    if total == 0:
        print('  Sem dados para exibir.')
        input('\n  Pressione Enter para continuar. ')
        return

    contagem = {'Pendente': 0, 'Em Rota': 0, 'Entregue': 0, 'Cancelado': 0}
    for p in banco.pedidos.values():
        if p['status'] in contagem:
            contagem[p['status']] += 1

    print()
    print('  -- Quantidade por status --')
    for status, qtd in contagem.items():
        print(f"  {status:<12}: {qtd}")

    alta = [p for p in banco.pedidos.values() if p['prioridade'] == 'Alta']
    print(f"\n  -- Pedidos com Alta Prioridade: {len(alta)} --")
    for p in alta:
        print(f"  {p['id']} | {p['nome']} | Status: {p['status']}")

    print('\n  -- Entregador com mais entregas concluídas --')
    if banco.entregadores:
        melhor_id  = None
        melhor_qtd = -1
        for eid, ent in banco.entregadores.items():
            qtd = sum(1 for pid in ent['pedidos']
                      if pid in banco.pedidos and banco.pedidos[pid]['status'] == 'Entregue')
            if qtd > melhor_qtd:
                melhor_qtd = qtd
                melhor_id  = eid
        if melhor_id and melhor_qtd > 0:
            ent = banco.entregadores[melhor_id]
            print(f"  {ent['nome']} (ID: {melhor_id}) com {melhor_qtd} entrega(s) concluída(s).")
        else:
            print('  Nenhuma entrega concluída registrada ainda.')
    else:
        print('  Nenhum entregador cadastrado.')

    input('\n  Pressione Enter para continuar. ')

# ============================================================
# SUBMENUS
# ============================================================

def submenuPedidos():
    while True:
        menu.menuPedidos()
        escolha = input('  Digite sua escolha: ').strip()

        match escolha:
            # Cadastrar Pedido
            case '1':
                utilidade.limpar_tela()
                print('''
================================
      Cadastro do Pedido
================================
                ''')
                idPedido   = funcoesPedidos.gerar_idPedido()
                print(f"  ID gerado automaticamente: {idPedido}")
                nome       = input('  Nome do cliente: ').strip()
                produto    = input('  Produto: ').strip()
                endereco   = input('  Endereço de entrega: ').strip()

                while True:
                    print('  Prioridade: [1] Alta  [2] Normal')
                    op = input('  Escolha: ').strip()
                    if op == '1':
                        prioridade = 'Alta'
                        break
                    elif op == '2':
                        prioridade = 'Normal'
                        break
                    else:
                        print('  Opção inválida.')

                descricao = input('  Descrição: ').strip()
                funcoesPedidos.cadastrarPedido(idPedido, nome, produto, endereco, prioridade, descricao)
                print(f"\n  Pedido {idPedido} cadastrado com sucesso!")
                input('\n  Pressione Enter para continuar. ')

            # Editar Pedido
            case '2':
                utilidade.limpar_tela()
                funcoesPedidos.editarPedido()

            # Consultar Pedido(s)
            case '3':
                while True:
                    menu.menuConsultarPedidos()
                    op = input('  Digite sua escolha: ').strip()
                    match op:
                        case '1':
                            utilidade.limpar_tela()
                            funcoesPedidos.listar_todos_pedidos()
                            input('\n  Pressione Enter para continuar. ')
                        case '2':
                            utilidade.limpar_tela()
                            funcoesPedidos.consultar_por_status('Pendente')
                            input('\n  Pressione Enter para continuar. ')
                        case '3':
                            utilidade.limpar_tela()
                            funcoesPedidos.consultar_por_status('Em Rota')
                            input('\n  Pressione Enter para continuar. ')
                        case '4':
                            utilidade.limpar_tela()
                            funcoesPedidos.consultar_por_status('Entregue')
                            input('\n  Pressione Enter para continuar. ')
                        case '5':
                            utilidade.limpar_tela()
                            funcoesPedidos.buscar_pedido_por_id()
                        case '6':
                            break
                        case _:
                            print('  Opção inválida.')
                            input('\n  Pressione Enter para continuar. ')

            # Gerenciar Pedido
            case '4':
                while True:
                    menu.menuGerenciarPedido()
                    op = input('  Digite sua escolha: ').strip()
                    match op:
                        case '1':
                            utilidade.limpar_tela()
                            funcoesPedidos.alterar_status()
                        case '2':
                            utilidade.limpar_tela()
                            funcoesPedidos.associar_entregador()
                        case '3':
                            utilidade.limpar_tela()
                            funcoesPedidos.remover_associacao()
                        case '4':
                            break
                        case _:
                            print('  Opção inválida.')
                            input('\n  Pressione Enter para continuar. ')

            # Cancelar Pedido
            case '5':
                utilidade.limpar_tela()
                funcoesPedidos.cancelar_pedido()

            # Voltar
            case '6':
                break

            case _:
                print('  Opção inválida.')
                input('\n  Pressione Enter para continuar. ')


def submenuEntregadores():
    while True:
        menu.menuEntregadores()
        escolha = input('  Digite sua escolha: ').strip()

        match escolha:
            # Cadastrar Entregador
            case '1':
                utilidade.limpar_tela()
                print('''
================================
     Cadastrar Entregador
================================
                ''')
                id_ent = funcoesEntregadores.gerar_idEntreg()
                print(f"  ID gerado automaticamente: {id_ent}")
                nome = input('  Nome do entregador: ').strip()
                cpf  = input('  CPF do entregador: ').strip()
                print('''
  Veículos disponíveis:
  1 - Carro
  2 - Moto
  3 - Van
  4 - Caminhão
                ''')
                while True:
                    op = input('  Escolha o veículo [1-4]: ').strip()
                    mapa = {'1': 'carro', '2': 'moto', '3': 'van', '4': 'caminhao'}
                    if op in mapa:
                        veiculo = mapa[op]
                        break
                    print('  Opção inválida.')

                funcoesEntregadores.cadastrarEntrg(id_ent, nome, cpf, veiculo)
                print(f"\n  Entregador {id_ent} - {nome} cadastrado com sucesso!")
                input('\n  Pressione Enter para continuar. ')

            # Editar Entregador
            case '2':
                utilidade.limpar_tela()
                id_ent = input('  ID do entregador: ').strip()
                if id_ent not in banco.entregadores:
                    print('  Entregador não encontrado.')
                    input('\n  Pressione Enter para voltar. ')
                else:
                    ent = banco.entregadores[id_ent]
                    print(f"  Encontrado: {ent['nome']} | {ent['veiculo']}")
                    funcoesEntregadores.editarEntrg(ent)

            # Listar todos
            case '3':
                funcoesEntregadores.listarEntrg()
                input('\n  Pressione Enter para continuar. ')

            # Entregadores disponíveis
            case '4':
                utilidade.limpar_tela()
                print('''
================================
   Entregadores Disponíveis
================================
                ''')
                funcoesEntregadores.listarEntrgDisp()
                input('\n  Pressione Enter para continuar. ')

            # Suspender / Reativar
            case '5':
                utilidade.limpar_tela()
                funcoesEntregadores.suspenderOuReativarEntrg()

            # Voltar
            case '6':
                break

            case _:
                print('  Opção inválida.')
                input('\n  Pressione Enter para continuar. ')


def submenuOperacoes():
    while True:
        menu.menuOperacoes()
        escolha = input('  Digite sua escolha: ').strip()

        match escolha:
            case '1':
                utilidade.limpar_tela()
                funcoesPedidos.associar_entregador()
            case '2':
                utilidade.limpar_tela()
                funcoesPedidos.remover_associacao()
            case '3':
                relatorio_do_dia()
            case '4':
                break
            case _:
                print('  Opção inválida.')
                input('\n  Pressione Enter para continuar. ')


def submenuAdm():
    while True:
        menu.menuAdm()
        opcao = input('  Digite sua escolha: ').strip()

        match opcao:
            case '1':
                submenuPedidos()
            case '2':
                submenuEntregadores()
            case '3':
                submenuOperacoes()
            case '4':
                print('\n  Sistema encerrado. Até logo!')
                return False   # sinaliza para encerrar
            case _:
                print('  Opção inválida.')
                input('\n  Pressione Enter para continuar. ')

        return True   # continua no loop principal


# ============================================================
# LOOP PRINCIPAL
# ============================================================

if __name__ == '__main__':
    print('''
================================
   Bem-vindo ao FluxoNorte
   Operação Turno Crítico v1.0
================================
    ''')

    rodando = True
    while rodando:
        menu.menuInicial()
        opcao = input('  Digite sua escolha: ').strip()

        match opcao:
            case '1':
                continuar = True
                while continuar:
                    menu.menuAdm()
                    op = input('  Digite sua escolha: ').strip()
                    match op:
                        case '1':
                            submenuPedidos()
                        case '2':
                            submenuEntregadores()
                        case '3':
                            submenuOperacoes()
                        case '4':
                            print('\n  Sistema encerrado. Até logo!')
                            rodando   = False
                            continuar = False
                        case _:
                            print('  Opção inválida.')
                            input('\n  Pressione Enter para continuar. ')
            case '2':
                print('\n  Sistema encerrado. Até logo!')
                rodando = False
            case _:
                print('  Opção inválida.')
                input('\n  Pressione Enter para continuar. ')