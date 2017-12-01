with open('arq.txt', 'a') as f:
    f.write('NOVA LINHA\n')

with open('arq.txt', 'r') as f:
    print(f.readline())

with open('arq.txt', 'r') as f:
    for l in f.readlines():
        print("Linha: %s" % l)