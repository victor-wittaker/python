frutas = ['pera', 'uva', 'maça', 'banana']

nova_lista = []

for f in frutas:
    if len(f) == 4:
        nova_lista.append(f)

print(nova_lista)

nova_lista = [ len(f) for f in frutas ]

print(nova_lista)