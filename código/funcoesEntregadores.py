import os
import random
import banco 
def gerar_idEntreg():
    id = random.randint(1000, 9999)
    return id
def cadastrarEntrg(id_entregador, nome_entregador, cpf_entregador, veiculo_entregador, disponibilidade_entregador):
    entregador = {
        "id": id_entregador,
        "nome": nome_entregador,
        "cpf": cpf_entregador,
        "veiculo": veiculo_entregador,
        "disponibilidade": disponibilidade_entregador
    }

    banco.entregadores.append(entregador)

def lsitarEntrg ():
    if not banco.entregadores:
        print("Nenhum entregador cadastrado.")
        return
    for e in banco.entregadores:
        print(f"ID: {e['id']} | Nome: {e['nome']} | CPF: {e['cpf']} | Veículo: {e['veiculo']} | Status: {e['disponibilidade']}")