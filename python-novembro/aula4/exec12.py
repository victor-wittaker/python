def soma():
    return num1+num2

def sub():
    return num1-num2

def div():
    return num1/num2

def mult():
    return num1*num2

def get_num():
    global num1, num2
    num1 = int(input("Informe num1: "))
    num2 = int(input("Informe num2: "))

menu = """
MENU
1) SOMA
2) SUBTRAÇÃO
3) DIVISÃO
4) MULTIPLICAÇÃO
5) SAIR
Digite uma opção: """

while True:
    opcao = int(input(menu))

    if opcao == 1:
        get_num()
        print(soma())
    elif opcao == 2:
        get_num()
        print(sub())
    elif opcao == 3:
        get_num()
        print(div())
    elif opcao == 4:
        get_num()
        print(mult())
    elif opcao == 5:
        break
    else:
        print("Opcão inválida")