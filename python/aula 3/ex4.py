#4) FAÇA UM PROGRAMA QUE LEIA 5 NÚMEROS E INFORME A MÉDIA DOS NÚMEROS.

numeros = []
media = 0 

while len(numeros) < 5:
    x = int(input("Digite a nota: "))
    numeros.append(x)    
    media = media + x 
    
print("Media: " + str(media/len(numeros)))
