#13 - FAÇA UM PROGRAMA QUE MOSTRE UM MENU COM OPÇÕES DE INSERIR E SAIR. 
# AO INFORMAR QUE QUER INSERIR, PEÇA NOME E EMAIL 
#DEPOIS GUARDE EM UM ARQUIVO. O CODIGO DE INSERÇÃO DEVE ESTAR DENTRO DE UMA FUNÇÃO. 
#CADA LINHA DO ARQUIVO DEVE CONTER UM REGISTRO DE ALUNO.

def inserir (nome, email):
    with open("registro_exec.txt", "a") as f:
        f.write("%s|%s\n" % (nome, email))

def get_todos():
    with open("registro_exec.txt", "r") as f:
        return f.read()

def menu ():
    menu = """
 Escolha a opcao:
 1 - Inserir
 2 - Sair
 """
    opcao = input(menu)
    if int(opcao) == 1:
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        inserir(nome, email)
    elif int(opcao) >= 2 or int(opcao) < 1:
        exit()
 
while True:
    menu()

