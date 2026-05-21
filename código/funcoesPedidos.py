import random
from banco import pedidos
def gerar_idPedido():
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letra = random.choice(alfabeto).upper()
    numeros = random.randint(1000,9999)
    id = letra + str(numeros)
    return id

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