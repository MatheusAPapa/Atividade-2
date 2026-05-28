import random
from banco import pedidos

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

# Busca pedido pelo ID
def buscarPedidoPorId(idBusca):
    idBusca = idBusca.strip().upper()
    for p in pedidos:
        if p['id'] == idBusca:
            return p
    return None

# Lista pedidos
def listaPedidos(filtro:None):
    resultado = []
    for p in pedidos:
        if filtro is None or p['status'] == filtro:
            resultado.append(p)
    return resultado

# Listar pedidos por prioridade: Alta ou baixa
def listaPrioridade():
    altos   = []
    normais = []
    for p in pedidos:
        if p['status'] == 'Pendente' and p['id_entregador'] is None:
            if p['prioridade'] == 'Alta':
                altos.append(p)
            else:
                normais.append(p)
    return altos + normais

def editarPedido(pedido, campo, novoValor):
    """Edita um campo do pedido. Pedidos cancelados não podem ser editados."""
    if pedido['status'] == 'Cancelado':
        return False, 'Pedido cancelado não pode ser editado.'
    pedido[campo] = novoValor
    return True, 'Campo atualizado com sucesso!'
 
 
def alterarStatusPedido(pedido, novoStatus):
    """
    Altera o status do pedido.
    Regra: pedido cancelado não pode ser reativado (decisão do time).
    """
    if pedido['status'] == 'Cancelado':
        return False, 'Pedido cancelado não pode ter o status alterado.'
    pedido['status'] = novoStatus
    # Se entregou, libera o entregador
    if novoStatus == 'Entregue' and pedido['id_entregador'] is not None:
        _liberar_entregador(pedido)
    return True, f"Status atualizado para '{novoStatus}'."
 
 
def cancelarPedido(pedido):
    """
    Cancela o pedido.
    Regra: pedido já cancelado não pode ser cancelado novamente.
    Regra: pedido cancelado nunca pode ser reativado (decisão do time).
    """
    if pedido['status'] == 'Cancelado':
        return False, 'Pedido já está cancelado.'
    if pedido['id_entregador'] is not None:
        _liberar_entregador(pedido)
    pedido['status'] = 'Cancelado'
    return True, 'Pedido cancelado com sucesso.'
 
 
# ---------- ASSOCIAÇÃO DE ENTREGADOR ----------
 
def associarEntregador(pedido, entregador):
    """
    Associa um entregador ao pedido.
    Regras:
    - Pedido deve estar Pendente
    - Entregador não pode estar Suspenso
    - Entregador não pode ter mais de MAX_PEDIDOS_POR_ENTREGADOR pedidos simultâneos
    - Pedido não pode já ter entregador
    """
    if pedido['status'] == 'Cancelado':
        return False, 'Pedido cancelado não pode receber entregador.'
    if pedido['status'] == 'Entregue':
        return False, 'Pedido já foi entregue.'
    if pedido['id_entregador'] is not None:
        return False, 'Pedido já possui entregador. Remova a associação antes.'
    if entregador['status'] == 'S':
        return False, 'Entregador está suspenso.'
    if len(entregador['pedidos']) >= MAX_PEDIDOS_POR_ENTREGADOR:
        return False, f'Entregador já possui {MAX_PEDIDOS_POR_ENTREGADOR} pedidos (limite máximo).'
 
    pedido['id_entregador']  = entregador['id']
    pedido['status']         = 'Em Rota'
    entregador['pedidos'].append(pedido['id'])
    entregador['status']     = 'E'
    return True, 'Entregador associado com sucesso!'
 
 
def removerEntregador(pedido):
    """Remove a associação do entregador, voltando pedido para Pendente."""
    if pedido['id_entregador'] is None:
        return False, 'Pedido não possui entregador atribuído.'
    if pedido['status'] == 'Entregue':
        return False, 'Pedido já entregue, não é possível remover o entregador.'
    _liberar_entregador(pedido)
    pedido['status'] = 'Pendente'
    return True, 'Entregador removido. Pedido voltou para Pendente.'
 
 
# ---------- AUXILIAR INTERNO ----------

def _liberar_entregador(pedido):
    """Remove o pedido da lista do entregador e atualiza seu status se necessário."""
    for e in banco.entregadores:
        if e['id'] == pedido['id_entregador']:
            if pedido['id'] in e['pedidos']:
                e['pedidos'].remove(pedido['id'])
            if len(e['pedidos']) == 0:
                e['status'] = 'D'
            break
    pedido['id_entregador'] = None