import menu
import os
import funcoesEntregadores
import banco

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
                #cadastrar entregador
                case 1:
                    os.system('cls')
                    print('''
================================
      Cadastrar Entregador
================================  
                ''')
                    id = funcoesEntregadores.gerar_idEntreg()
                    nome = str(input('Digite o nome do entregador: '))
                    cpf = int(input('Digite o cpf do entregador: '))
                    print('''
    Opções de veículos disponíveis:
    1 - Carro               
    2 - Moto                           
    3 - Van      
    4 - Caminhão                             
                    ''')                    
                    veiculo = int(input('Digite o veículo que o entregador usará [1, 2, 3 ou 4]: '))
                    while veiculo not in [1, 2, 3, 4]:
                        veiculo = int(input('Digite um veículo válido')).lower()
                    match veiculo:
                        case 1:
                            veiculo = 'carro'
                        case 2:
                            veiculo ='moto'
                        case 3:
                            veiculo ='van'
                        case 4:
                            veiculo = 'caminhao'

                    funcoesEntregadores.cadastrarEntrg(id, nome, cpf, veiculo)
                    input('\nEntregador cadastrado! Precione enter para voltar à tela inicial! ')
                #editar dados
                case 2:
                    os.system('cls')
                    entregador_encontrado = None
                    entregador = int(input('Digite o id do entregador: '))
                    for e in banco.entregadores:
                        if e['id'] == entregador:
                            entregador_encontrado = e
                            break
                    
                    if entregador_encontrado is None:
                        print('Entregador não encontrado!')
                        input('Precione enter para voltar!')
                    else:
                        print('Entregador encontrado!')
                        print(f"ID: {entregador_encontrado['id']} | Nome: {entregador_encontrado['nome']} | CPF: {entregador_encontrado['cpf']} | Veículo: {entregador_encontrado['veiculo']} | Status: {entregador_encontrado['status']}")
                        funcoesEntregadores.editarEntrg(entregador_encontrado)
                #listar todos os entregadores
                case 3:
                    funcoesEntregadores.listarEntrg()
                    input('\nPrecione enter para voltar à tela inicial! ')
                #mostrar todos entregadores disponíveis
                case 4:
                    print('''
================================
   Entregadores Disponíveis
================================
                        ''')
                    funcoesEntregadores.listarEntrgDisp()
                    input('\nPrecione enter para voltar à tela inicial! ')
                    
        case 3:
            menu.menuOperacoes()
            escolha2 = int(input('Digita a sua escolha: '))
        #finalizar sistema
        case 4:
            print('Sistema encerrado')
            break
        