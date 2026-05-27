import os
import random
import banco 
def gerar_idEntreg():
    id = random.randint(1000, 9999)
    return id
def cadastrarEntrg(id_entregador, nome_entregador, cpf_entregador, veiculo_entregador, disponibilidade_entregador='D', status="A"):
    entregador = {
        "id": id_entregador,
        "nome": nome_entregador,
        "cpf": cpf_entregador,
        "veiculo": veiculo_entregador,
        "disponibilidade": disponibilidade_entregador,
        "status": status
    }

    banco.entregadores.append(entregador)

def editarEntrg (entregador):
    print('''
================================
         Editar Dados
================================  
    1 - Nome
    2 - CPF
    3 - veículo
    4 - Voltar para o menu anteriorm
    ''')
    opcaoEditar = int(input('Digite sua escolha: '))
    match opcaoEditar:
        case 1:
            novoNome = str(input('Digite o nome do entregador: '))
            entregador['nome'] = novoNome
            print('Nome atualizado com sucesso!')
            input('\nPrecione enter para voltar! ')
        case 2:
            novoCpf = int(input('Digite o nome do entregador: '))
            entregador['cpf'] = novoCpf
            print('CPF atualizado com sucesso!')
            input('\nPrecione enter para voltar! ')
        case 3:
            print('''
    Opções de veículos disponíveis:
    1 - Carro               
    2 - Moto                           
    3 - Van      
    4 - Caminhão                             
                ''') 
            novoVeiculo = int(input('Digite o novo tipo veículo do entregador: '))
            match novoVeiculo:
                case 1:
                    novoVeiculo = 'carro'
                case 2:
                    novoVeiculo ='moto'
                case 3:
                    novoVeiculo ='van'
                case 4:
                    novoVeiculo = 'caminhao'
            entregador['veiculo'] = novoVeiculo
            print('Veículo atualizado com sucesso!')
            input('\nPrecione enter para voltar! ')

def listarEntrg ():
    os.system('cls')
    print('''
================================
       Todos Entregadores
================================
    ''')
    if len(banco.entregadores) == 0:
        print("Nenhum entregador cadastrado.")
        return
    for e in banco.entregadores:
        if e['disponibilidade'] == 'D':
            disponibilidade = 'Disponível'
        elif e['disponibilidade'] == 'E':
            disponibilidade = 'Em rota de entrega'
        elif e['disponibilidade'] == 'S':
            disponibilidade = 'Suspenso'
        
        if e['status'] == 'A':
            status = 'Ativo'
        elif e['status'] == 'S':
            status = 'Suspenso'

        print(f"ID: {e['id']} | Nome: {e['nome']} | CPF: {e['cpf']} | Veículo: {e['veiculo']} | Disponibilidade: {disponibilidade} | Status: {e['status']}")

def listarEntrgDisp ():
    if len(banco.entregadores) == 0:
        print("Nenhum entregador cadastrado.")
        return
    for e in banco.entregadores:
        if e['disponibilidade'].upper() == 'D' and e['status'] == 'A':
            disponibilidade = 'Disponível'
            print(f"ID: {e['id']} | Nome: {e['nome']} | CPF: {e['cpf']} | Veículo: {e['veiculo']} | Disponibilidade: {disponibilidade}")

def gerenciarEntreg (entregador, acao):
    match acao:
        #remover
        case 1:
            banco.entregadores.remove(entregador)
            print('Entregador removido com sucesso!')
        #suspender
        case 2:
            if entregador['status'] == 'S':
                print('Entregador já está suspenso!')
            else:
                entregador['status'] = 'S'
                print(f"Entregador {entregador['nome']} suspenso!")
        case 3:  # Reativar
            if entregador['status'] == 'A':
                print('Entregador já está ativo!')
            else:
                entregador['status'] = 'A'
                print(f"Entregador {entregador['nome']} reativado!")
        case 4:
            print('Operação cancelada.')