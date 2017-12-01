from Mongo import Mongo

mongo = Mongo('127.0.0.1', 'escola')

while True:
    menu = """
    1) Inserir
    2) Alterar
    3)
    4)
    5)
    Digite uma opção: """

    op = int(input(menu))

    if op == 1:
        nome = input('Insira o nome: ')
        email = input('Insira o email: ')

        mongo.inserir(nome, email)

        if mongo:
            print("Inserido com sucesso")

    elif op == 2:
        email = input('Insira o email: ')
        nome = input('Insira o novo nome: ')

        mongo.alterar(
            email=email, nome=nome
        )
    elif op == 3:
        pass
    elif op == 4:
        pass
    else:
        print("Opção nao encontrada")
        