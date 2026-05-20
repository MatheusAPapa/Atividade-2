import menu
import os
import funcoesEntregadores
opcao = 1
while opcao != 4:
    menu.menuInicial()
    opcao = int(input('Digita a sua escolha: '))
    while opcao not in [1, 2, 3, 4]:
        opcao = int(input('Digita a sua escolha: '))
    match opcao:
        case 1:
            menu.menuPedidos()
            escolha = int(input('Digita a sua escolha: '))
            match escolha:
                #Cadastrar Pedido(s)
                case 1:
                    print('a')
                    input('Precione enter para voltar à tela inicial! ')
                    continue
                #Editar Pedido(s)
                case 2:
                    print('a')
                    input('Precione enter para voltar à tela inicial! ')
                    continue
                #Consultar Pedido(s)
                case 3:
                    print('a')
                    input('Precione enter para voltar à tela inicial! ')
                    continue
                #Gerenciar Pedido(s)
                case 4:
                    print('a')
                    input('Precione enter para voltar à tela inicial! ')
                    continue
                #Cancelar Pedido(s)
                case 5:
                    print('a')
                    input('Precione enter para voltar à tela inicial! ')
                    continue
                #Voltar a tela inicial 
                case 6:
                    print('a')
                    input('Precione enter para voltar à tela inicial! ')
                    continue
        case 2:
            menu.menuEntregadores()
            escolha1 = int(input('Digita a sua escolha: '))
            match escolha1:
                case 1:
                    os.system('cls')
                    print('''
================================
      Cadastrar Entregador
================================  
                ''')
                    id = funcoesEntregadores.gerar_idEntreg()
                    nome = str(input('Digite o nome do entregador: '))
                    cpf = str(input('Digite o cpf do entregador: '))
                    veiculo = str(input('Digite o veículo que o entregador usará'))
                    disponibilidade = 'Disponível'

                    funcoesEntregadores.cadastrarEntrg(id, nome, cpf, veiculo, disponibilidade)

        case 3:
            menu.menuOperacoes()
            escolha2 = int(input('Digita a sua escolha: '))
        #finalizar sistema
        case 4:
            print('Sistema encerrado')
            break
        