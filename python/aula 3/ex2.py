# 2) FAÇA UM PROGRAMA QUE RECEBA UMA DATA NO FORMATO YYYY-MM-DD E MUDE PARA DD/MM/YYYY

data = input("Digite a data no formato YYYY-MM-DD: ")

print(data[8:10] + "/"+ data[5:7] +"/" + data[0:4])


# resp do intrutor

data = input("Informe a data: ")

data = data.split('-')

data = "%s/%s/%s"% (data[2], data[1], data[0])

print(data)
