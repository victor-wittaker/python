with open("arq.txt", "w") as f:
    f.write('Nova Linha\n')

with open("arq.txt", "r") as f:
    print(f.readline())

with open('arq.txt', 'r') as f:
    for l in f.readlines():
        print("Linha: " % l)
