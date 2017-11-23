# 3) FAÇA UM PROGRAMA QUE LEIA 5 NÚMEROS E INFORME O MAIOR NÚMERO.

numeros = []
maior = 0
while len(numeros) < 5:
    atual = int(input("Digite os numeros: "))
    if atual > maior:
        maior = atual

print(maior)


           


