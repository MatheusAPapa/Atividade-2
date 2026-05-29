pedidos = []
'''
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
'''
entregadores = []
'''
[0]: id - número de 4 dígitos
[1]: nome do entregador
[2]: cpf do entregador
[3]: veículo que entregador usará
[4]: Status(D - disponível, E - em entrega, S - suspenso)
'''
LIMITE_PEDIDOS_ENTREGADOR = 5

status_validos = ['pendente', 'em rota', 'entregue', 'cancelado']

veiculos_permitidos = ['carro', 'van', 'moto']