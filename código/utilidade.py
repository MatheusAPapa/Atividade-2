import banco
# Verifica quantos pedidos estão com status 'Em rota'
def pedidos_ativos_entregador(id_entregador):
    count = 0
    for ped in banco.entregadores[id_entregador]["pedidos"]:
        if ped in banco.pedidos:
            if banco.pedidos[ped]["status"] == "Em Rota":
                count += 1
    return count

# Organiza por prioridade(Alta ou Normal)
def ordenar_pedidos_por_prioridade(lista_ids):
    alta   = [p for p in lista_ids if banco.pedidos[p]["prioridade"] == "Alta"]
    normal = [p for p in lista_ids if banco.pedidos[p]["prioridade"] == "Normal"]
    return alta + normal

# Exibir pedidos já cadastrados
def exibir_pedido(pedido):
    print(f"\nPedido  : {pedido['id']}")
    print(f"Cliente   : {pedido['cliente']}")
    print(f"Endereço  : {pedido['endereco']}")
    print(f"Prioridade: {pedido['prioridade']}")
    print(f"Status    : {pedido['status']}")
    entregador = pedido['id_entregador'] if pedido['id_entregador'] else "Nenhum"
    print(f"Entregador: {entregador}")
    print(f"Descrição : {pedido['descricao']}")