import os
import random
import banco 
def gerar_idEntreg():
    id = random.randint(1000, 9999)
    return id
def cadastrarEntrg(id_entregador, nome_entregador, cpf_entregador, veiculo_entregador, disponibilidade_entregador='D'):
    entregador = {
        "id": id_entregador,
        "nome": nome_entregador,
        "cpf": cpf_entregador,
        "veiculo": veiculo_entregador,
        "status": disponibilidade_entregador
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
        if e['status'] == 'D':
            disponibilidade = 'Disponível'
        elif e['status'] == 'E':
            disponibilidade = 'Em rota de entrega'
        elif e['status'] == 'S':
            disponibilidade = 'Suspenso'

        print(f"ID: {e['id']} | Nome: {e['nome']} | CPF: {e['cpf']} | Veículo: {e['veiculo']} | Status: {disponibilidade}")

def listarEntrgDisp ():
    if len(banco.entregadores) == 0:
        print("Nenhum entregador cadastrado.")
        return
    for e in banco.entregadores:
        if e['status'].upper() == 'D':
            disponibilidade = 'Disponível'
            print(f"ID: {e['id']} | Nome: {e['nome']} | CPF: {e['cpf']} | Veículo: {e['veiculo']} | Status: {disponibilidade}")

def entregas_por_entregador():
    id_ent = input("  ID do Entregador: ").strip()
 
    if id_ent not in banco.entregadores:
        print("  [ERRO] Entregador não encontrado.")
        return
 
    ent = banco.entregadores[id_ent]
    print(f"\nEntregador : {ent['nome']}")
    print(f"Veículo      : {ent['veiculo']}")
    print(f"Disponível   : {'Sim' if ent['disponivel'] else 'Não'}")
    print(f"Total de pedidos associados: {len(ent['pedidos'])}")
 
    if not ent["pedidos"]:
        print("  Nenhuma entrega registrada.")
    else:
        for ped in ent["pedidos"]:
            if ped in banco.pedidos:
                print(banco.pedidos[ped])
            else:
                print(f"Pedido {ped} não encontrado no sistema.")

