def soma(a, b):
    return a+b

def sub(a,b):
    return a-b

def div(a, b):
    return a/b

def mult(a, b):
    return a*b

menu = """
MENU
1) SOMA
2) SUBTRAÇÃO
3) DIVISÃO
4) MULTIPLICAÇÃO
Digite uma opção: """

opcao = int(input(menu))
num1 = int(input("Informe num1: "))
num2 = int(input("Informe num2: "))

if opcao == 1:
    print(soma(num1, num2))
elif opcao == 2:
    print(sub(num1, num2))
elif opcao == 3:
    print(div(num1, num2))
elif opcao == 4:
    print(mult(num1, num2))
else:
    print("Opcão inválida")