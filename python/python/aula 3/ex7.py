# 7) FAÇA UM PROGRAMA QUE RECEBA UM USUARIO E SENHA. SE O USUARIO FOR IGUAL A SENHA PEÇA NOVAMENTE, SENÃO, ENCERRE O PROGRAMA.

usr = input("Usuario: ")
senha = input("Senha: ")

while usr == senha:
    print("Digite novamente!")
    usr = input("Usuario: ")
    senha = input("Senha: ")
else:
    exit(0)
