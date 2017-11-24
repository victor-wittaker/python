#12 - FAÇA UM PROGRAMA QUE MOSTRE UM MENU COM OPÇÕES SOMA, MULTIPLICAÇÃO, SUBTRAÇÃO, DIVISÃO E SAIR. 
# MOSTRE O RESULTADO AO USUARIO. O PROGRAMA DEVE ENCERRAR APENAS QUANDO A OPÇÃO SAIR FOR INSERIDA.


def soma (a, b):
    return a + b

def divisao (a, b):
    return a / b

def subtracao (a, b):
    return a - b

def multi (a, b):
    return a * b

def menu ():
    menu = """
Escolha uma operacao:

1 - Soma
2 - Subtracao
3 - Divisao
4 - Multiplicacao
0 - SAIR
"""
    opcao = input(menu)
    if int(opcao) > 4: 
        print("Opcao invalida")
        exit(0)
    elif int(opcao) <= 0:
        exit(0)

    num1 = input("Digite o 1o numero: ")
    num2 = input("Digite o 2o numero: ")

    if int(opcao) == 1:
        print(soma(int(num1), int(num2)))
    elif int(opcao) == 2:
        print(subtracao(int(num1), int(num2)))
    elif int(opcao) == 3:
        print(divisao(int(num1), int(num2)))
    elif int(opcao) == 4:
        print(multi(int(num1), int(num2)))
   

while True:
    menu()

