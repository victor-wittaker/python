#11 - CRIE UMA FUNÇÃO PARA CADA OPERAÇÃO ARITIMÉTICA (SOMA, DIVISÃO, SUBTRAÇÃO E MULTIPLICAÇÃO). PEÇA A OPERAÇÃO E DOIS NÚMEROS. REALIZE O CALCULO E MOSTRE AO USUÁRIO.


def soma (a, b):
    return a + b

def divisao (a, b):
    return a / b

def subtracao (a, b):
    return a - b

def multi (a, b):
    return a * b

menu = """

Escolha uma operacao:

1 - Soma
2 - Subtracao
3 - Divisao
4 - Multiplicacao
"""
opcao = input(menu)
if int(opcao) <= 0 or int(opcao) > 4: 
    print("Opcao invalida")
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
