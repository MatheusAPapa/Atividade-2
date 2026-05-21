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
                    print('''
================================
     Consultar Pedido(s)
================================
                    ''')
                    from banco import pedidos
                    busca = input("Digite o ID do pedido (ou Enter para listar todos): ")
                    if busca == "":
                        resultado = pedidos
                    else:
                        for i in pedidos:
                            if i['id'] == busca.upper():
                                resultado.append(i)
                    if len(pedidos) == 0:
                        print("Nenhum pedido encontrado.")
                    else:
                         for i in resultado:
                            print(f"ID: {i['id']}")
                            print(f"Cliente: {i['nome']}")
                            print(f"Produto: {i['produto']}")
                            print(f"Endereço: {i['endereco']}")
                            print(f"Prioridade: {i['prioridade']}")
                            print(f"Descrição: {i['descricao']}")
                            print(f"Status: {i['status']}")
                    input('Pressione Enter para voltar à tela inicial! ')
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
        