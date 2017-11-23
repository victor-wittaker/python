# 1) FAÇA UM PROGRAMA QUE RECEBA DUAS STRINGS E DIGA SE ELAS POSSUEM OU NÃO O MESMO TAMANHO E SE O CONTEUDO É IGUAL OU DIFERENTE


string1 = input("Digite a 1a string: ")
string2 = input("Digite a 2a string: ") 
if (len(string1)) == (len(string2)):
        print("Possui mesmo tamanho")
        if string1 == string2:
            print("Mesmo conteudo")
        else:
            print("palavras diferentes")
else:
        print("Nao possui mesmo tamanho")

