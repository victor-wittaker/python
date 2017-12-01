#14 - CONTINUE O PROGRAMA ANTERIOR E CRIE A FUNÇÃO DE BUSCAR REGISTRO PELO EMAIL. 
# ADICIONE A OPÇÃO NO MENU, RECEBA VALOR DE EMAIL, 
#BUSQUE NO ARQUIVO E MOSTRE NA TELA O NOME REFERENTE AO EMAIL P ASSADO.

def inserir (nome, email):
    with open("registro_exec.txt", "a") as f:
        f.write("%s|%s\n" % (nome, email))

def busca(email):
    with open("registro_exec.txt", "r") as f:
        for i in f.readlines():
            i = i.strip("\n")
            i = i.split("|")
    
            if i[1] == email:
                return i[0]
                
    return 'nao encontrado'
    

def menu ():
    menu = """
 Escolha a opcao:
 1 - Inserir
 2 - Buscar
 0 - Sair

 """
    opcao = input(menu)
    if int(opcao) == 1:
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        inserir(nome, email)
    elif int(opcao) == 2:
        email = input("Digite email: ")
        print(busca(email))
    elif int(opcao) < 1:
        exit()
 
while True:
    menu()

