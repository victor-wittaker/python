# Cria tuplas, sem numero de parametros definidos
def soma(*args):
    print(sum(args))

# Cria dicionarios, sem numero de parametros definidos
def cadastro(**kwargs): 
    print(kwargs)

soma(1,2)

cadastro(nome="teste",cidade="SP")