import os
def menuInicial():
    os.system('cls')
    print('''
================================
         Fluxo Norte 
================================
    1 - Aba Administrador
    2 - Aba Entregador
 ''')
 
def menuAdm():
    os.system('cls')
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
    os.system('cls')
    print('''
================================
           Pedidos 
================================
          
    1 - Cadastrar Pedido(s)
    2 - Editar Pedido(s)
    3 - Consultar Pedido(s)
    4 - Gerenciar Pedido(s)
    5 - Cancelar Pedido(s)
    6 - Voltar a tela inicial   
 ''')
    
def menuEntregadores():
    os.system('cls')
    print('''
================================
        Entregadores 
================================
          
    1 - Cadastrar Entregador
    2 - Editar Entregador
    3 - Listar entregadores
    4 - Consultar Entregadores disponiveis
    5 - Remover/Suspender Entregador
    6 - Voltar a tela inicial  
 ''')

def menuOperacoes():
    os.system('cls')
    print('''
================================
        Operaçoes do dia 
================================
          
    1 - Atribuir Pedido(s)
    2 - Relatório do dia
    3 - Voltar a tela inicial
 ''')