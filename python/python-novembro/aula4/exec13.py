menu = """
MENU
1) INSERIR
2) SAIR
Digite uma opção: """

def inserir(nome, email):
    with open('cadastro.txt', 'a') as f:
        f.write("%s|%s\n" % (nome, email))

def get_todos():
    with open('cadastro.txt', 'r') as f:
        return f.read()


while True:
    opcao = int(input(menu))

    if opcao == 1:
        nome = input("Insira o nome: ")
        email = input("Insira o email: ")

        inserir(nome, email)
        print(get_todos())
    elif opcao == 2:
        break
    else:
        print('Opção inválida')