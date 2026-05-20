import menu
import funcoesPedidos

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
                    print('''
================================
     Cadastro do Pedido
================================
                    ''')
                    idPedido = funcoesPedidos.gerar_idPedido()
                    nomeCliente = input("Digite o nome do cliente: ")
                    produto = input("Qual o produto: ")
                    endereco = input("Digite o endereço: ")
                    prioridade = input("Qual a prioridade do pedido(Alta,Normal): ")
                    descricao = input("Dê uma descrição do produto: ")
                    status = 'Pendente'
                    input('Precione Enter para concluir o cadastro.')

                    continue
                #Editar Pedido(s)
                case 2:
                    
                    input('Precione enter para voltar à tela inicial! ')
                    continue
                #Consultar Pedido(s)
                case 3:
                    
                    input('Precione enter para voltar à tela inicial! ')
                    continue
                #Gerenciar Pedido(s)
                case 4:
                    
                    input('Precione enter para voltar à tela inicial! ')
                    continue
                #Cancelar Pedido(s)
                case 5:
                    
                    input('Precione enter para voltar à tela inicial! ')
                    continue
                #Voltar a tela inicial 
                case 6:
                    
                    input('Precione enter para voltar à tela inicial! ')
                    continue
        case 2:
            menu.menuEntregadores()
            escolha1 = int(input('Digita a sua escolha: '))
        case 3:
            menu.menuOperacoes()
            escolha2 = int(input('Digita a sua escolha: '))
        #finalizar sistema
        case 4:
            print('Sistema encerrado')
            break
        