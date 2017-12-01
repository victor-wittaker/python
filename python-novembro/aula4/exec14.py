menu = """
MENU
1) INSERIR
2) BUSCAR
3) SAIR
Digite uma opção: """

def inserir(nome, email):
    with open('cadastro.txt', 'a') as f:
        f.write("%s|%s\n" % (nome, email))

def get_todos():
    with open('cadastro.txt', 'r') as f:
        return f.read()

def get_um(email):
    with open('cadastro.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            line = line.split('|')

            if email in line:
                return line[0]
    
    return 'Nao encontrado'

while True:
    opcao = int(input(menu))

    if opcao == 1:
        nome = input("Insira o nome: ")
        email = input("Insira o email: ")

        inserir(nome, email)
        print(get_todos())
    elif opcao == 2:
        email = input("Insira o email: ")
        print(get_um(email))

    elif opcao == 3:
        break
    else:
        print('Opção inválida')