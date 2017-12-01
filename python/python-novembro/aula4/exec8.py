numa = int(input("Infome o numero: "))
numb = int(input("Infome o numero: "))

total = numa+numb

with open('resul', 'a') as f:
    text = '%s + %s = %s\n' % (numa, numb, total)
    f.write(text)
    print(text)