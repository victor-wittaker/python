import csv

with open('alunos.csv', 'r') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=';')

    for a in arquivo:
        print(a)

with open('arquivos.csv', 'a') as csvfile:
    arquivo = csv.writer(csvfile, demiliter=';')
    arquivo.writerow(['joao', 'joao@mail'])