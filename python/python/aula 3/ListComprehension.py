frutas = ["pera", "uva", "maca", "banana"]

nova_lista = []

for f in frutas:
    if len(f) == 4:
        nova_lista.append(f)

print(nova_lista)

## USANDO LIST COMPREHENSION

nova_lista = [ f for f in frutas if len(f) == 4 ]
print(nova_lista)
