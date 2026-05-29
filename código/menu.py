# ============================================================
#   MENUS - FluxoNorte
#   Definição de todos os menus do sistema
# ============================================================

import utilidade

def menuInicial():
    utilidade.limpar_tela()
    print('''
================================
         Fluxo Norte
================================
    1 - Aba Administrador
    2 - Sair do sistema
''')

def menuAdm():
    utilidade.limpar_tela()
    print('''
================================
         Administrador
================================
    1 - Pedidos
    2 - Entregadores
    3 - Operações do dia
    4 - Finalizar sistema
''')

def menuPedidos():
    utilidade.limpar_tela()
    print('''
================================
           Pedidos
================================
    1 - Cadastrar Pedido
    2 - Editar Pedido
    3 - Consultar Pedido(s)
    4 - Gerenciar Pedido (status / associar entregador)
    5 - Cancelar Pedido
    6 - Voltar
''')

def menuEntregadores():
    utilidade.limpar_tela()
    print('''
================================
         Entregadores
================================
    1 - Cadastrar Entregador
    2 - Editar Entregador
    3 - Listar todos os entregadores
    4 - Consultar entregadores disponíveis
    5 - Suspender / Reativar Entregador
    6 - Voltar
''')

def menuOperacoes():
    utilidade.limpar_tela()
    print('''
================================
        Operações do Dia
================================
    1 - Atribuir Pedido a Entregador
    2 - Remover Associação de Entregador
    3 - Relatório do dia
    4 - Voltar
''')

def menuGerenciarPedido():
    utilidade.limpar_tela()
    print('''
================================
       Gerenciar Pedido
================================
    1 - Alterar status do pedido
    2 - Associar entregador a pedido
    3 - Remover associação de entregador
    4 - Voltar
''')

def menuConsultarPedidos():
    utilidade.limpar_tela()
    print('''
================================
       Consultar Pedidos
================================
    1 - Listar todos os pedidos
    2 - Pedidos Pendentes
    3 - Pedidos Em Rota
    4 - Pedidos Entregues
    5 - Buscar por ID
    6 - Voltar
''')