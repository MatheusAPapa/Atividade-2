# ============================================================
#   UTILITÁRIOS - FluxoNorte
#   Funções auxiliares usadas pelos demais módulos
# ============================================================

import os
import banco

def limpar_tela():
    """Limpa o terminal (Windows e Linux/Mac)."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Verifica quantos pedidos estão com status 'Em Rota' para um entregador
def pedidos_ativos_entregador(id_entregador):
    count = 0
    for pid in banco.entregadores[id_entregador]['pedidos']:
        if pid in banco.pedidos:
            if banco.pedidos[pid]['status'] == 'Em Rota':
                count += 1
    return count

# Organiza lista de IDs por prioridade (Alta primeiro, Normal depois)
def ordenar_pedidos_por_prioridade(lista_ids):
    alta   = [p for p in lista_ids if banco.pedidos[p]['prioridade'] == 'Alta']
    normal = [p for p in lista_ids if banco.pedidos[p]['prioridade'] == 'Normal']
    return alta + normal

# Exibe os dados formatados de um pedido
def exibir_pedido(pedido):
    print(f"\n  ID Pedido  : {pedido['id']}")
    print(f"  Cliente    : {pedido['nome']}")
    print(f"  Produto    : {pedido['produto']}")
    print(f"  Endereço   : {pedido['endereco']}")
    print(f"  Prioridade : {pedido['prioridade']}")
    print(f"  Status     : {pedido['status']}")
    entregador = pedido['id_entregador'] if pedido['id_entregador'] else 'Nenhum'
    print(f"  Entregador : {entregador}")
    print(f"  Descrição  : {pedido['descricao']}")
    print()