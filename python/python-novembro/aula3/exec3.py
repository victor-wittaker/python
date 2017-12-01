numeros = []

while len(numeros) < 5:
    atual = int(input("Insira um número: "))
    numeros.append(atual)

maior = 0

for n in numeros:
    if n > maior:
        maior = n

print(maior)

#######

maior = 0

while len(numeros) < 5:
    atual = int(input("Insira um número: "))
    if atual > maior:
        maior = atual
    
print maior