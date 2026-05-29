import random
from banco import pedidos
import utilidade
import banco

# Gera o ID unico do pedido
def gerar_idPedido():
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    while True:
        letra   = random.choice(alfabeto)
        numeros = random.randint(1000, 9999)
        novo_id = letra + str(numeros)
        # Garante unicidade
        duplicado = False
        for p in pedidos:
            if p['id'] == novo_id:
                duplicado = True
                break
        if not duplicado:
            return novo_id

# Cadastra pedidos
def cadastrarPedido(idPedido,nomeCliente,prod,ender,priorid,desc,stats):
    pedido = {
        'id': idPedido,
        'nome': nomeCliente,
        'produto': prod,
        'endereco':ender,
        'prioridade': priorid,
        'descricao': desc,
        'status': stats
    }
    pedidos.append(pedido)
    return pedido

def alterar_status():
    id_pedido = input("ID do Pedido: ").strip().upper()
 
    if id_pedido not in banco.pedidos:
        print("Pedido não encontrado.")
        
        return
 
    pedido = banco.pedidos[id_pedido]
 
    if pedido["status"] == "Cancelado":
        print("Pedido cancelado não pode ser alterado.")

        return
 
    print(f"Status atual: {pedido['status']}")
    print("Novo status: [1] Pendente  [2] Em Rota  [3] Entregue")
    opcao = input("Escolha: ").strip()
    mapa = {"1": "Pendente", "2": "Em Rota", "3": "Entregue"}
 
    if opcao not in mapa:
        print("Opção inválida.")
        
        return
 
    novo_status = mapa[opcao]
 
    # Se marcado como Entregue, verifica se libera o entregador
    if novo_status == "Entregue" and pedido["id_entregador"]:
        id_ent = pedido["id_entregador"]
        if id_ent in banco.entregadores:
            ativos = pedidos_entregador(id_ent)
            if ativos <= 1:
                banco.entregadores[id_ent]["disponivel"] = True
 
    pedido["status"] = novo_status
    print(f"Status atualizado para '{novo_status}'.")

def cancelar_pedido():
    id_pedido = input("ID do Pedido: ").strip().upper()
 
    if id_pedido not in banco.pedidos:
        print("Pedido não encontrado.")
        
        return
 
    pedido = banco.pedidos[id_pedido]
 
    if pedido["status"] == "Cancelado":
        print("Pedido já está cancelado.")
    
        return
 
    confirma = input(f"Confirmar cancelamento do pedido {id_pedido}? (s/n): ").strip().lower()
    if confirma != "s":
        print("Cancelamento abortado.")

        return
 
    # Remove associação com o entregador se houver
    id_ent = pedido["id_entregador"]
    if id_ent and id_ent in banco.entregadores:
        lista = banco.entregadores[id_ent]["pedidos"]
        if id_pedido in lista:
            lista.remove(id_pedido)
        if pedidos_entregador(id_ent) == 0:
            banco.entregadores[id_ent]["disponivel"] = True
 
    pedido["status"] = "Cancelado"
    pedido["id_entregador"] = ""
    print(f"Pedido {id_pedido} cancelado.")

def associar_entregador():
    id_pedido = input("ID do Pedido: ").strip().upper()
 
    if id_pedido not in banco.pedidos:
        print("Pedido não encontrado.")

        return
 
    pedido = banco.pedidos[id_pedido]
 
    if pedido["status"] in ("Cancelado", "Entregue"):
        print(f"Pedido com status '{pedido['status']}' não pode receber entregador.")
        
        return
 
    if pedido["id_entregador"]:
        print(f"Pedido já possui entregador: {pedido['id_entregador']}")
        
        return
 
    id_ent = input("ID do Entregador: ").strip()
 
    if id_ent not in banco.entregadores:
        print("Entregador não encontrado.")
    
        return
 
    entregador = banco.entregadores[id_ent]
 
    if not entregador["disponivel"]:
        print("Entregador está indisponível no momento.")
        return
 
    ativos = pedidos_entregador(id_ent)
    if ativos >= banco.LIMITE_PEDIDOS_ENTREGADOR:
        print(f"Entregador atingiu o limite de {banco.LIMITE_PEDIDOS_ENTREGADOR} pedidos em rota.")

        return
 
    pedido["id_entregador"] = id_ent
    pedido["status"] = "Em Rota"
    entregador["pedidos"].append(id_pedido)
 
    # Bloqueia disponibilidade se atingiu o limite
    if pedidos_entregador(id_ent) >= banco.LIMITE_PEDIDOS_ENTREGADOR:
        entregador["disponivel"] = False
 
    print(f"Pedido {id_pedido} associado ao entregador {id_ent} ({entregador['nome']}).")

def remover_associacao():
    id_pedido = input("ID do Pedido: ").strip().upper()
 
    if id_pedido not in banco.pedidos:
        print("  [ERRO] Pedido não encontrado.")
        
        return
 
    pedido = banco.pedidos[id_pedido]
 
    if not pedido["id_entregador"]:
        print("Pedido não possui entregador associado.")

        return
 
    id_ent = pedido["id_entregador"]
 
    if id_ent in banco.entregadores:
        lista = banco.entregadores[id_ent]["pedidos"]
        if id_pedido in lista:
            lista.remove(id_pedido)
        if pedidos_entregador(id_ent) < banco.LIMITE_PEDIDOS_ENTREGADOR:
            banco.entregadores[id_ent]["disponivel"] = True
 
    pedido["id_entregador"] = ""
    pedido["status"] = "Pendente"
    print(f"Associação removida. Pedido {id_pedido} voltou para 'Pendente'.")

def consultar_por_status(status):
    ids = [p for p in banco.pedidos if banco.pedidos[p]["status"] == status]
    ids_ordenados = pedidos_por_prioridade(ids)
 
    if not ids_ordenados:
        print(f"  Nenhum pedido com status '{status}'.")
    else:
        for ped in ids_ordenados:
            print(banco.pedidos[ped])
    
 
 
def buscar_pedido_por_id():
    id_pedido = input("ID do Pedido: ").strip().upper()
 
    if id_pedido in banco.pedidos:
        print(banco.pedidos[id_pedido])
    else:
        print("Pedido não encontrado.")
    
