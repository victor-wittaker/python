x = ['python', 'php', 'java']

# Mostra conteudo da lista
print(x)

# Mostra posição 1 da lista
print(x[1])

# Substitui valor na posição 2 por javascript
x[2] = 'Javascript'

# Adiciona ao final da lista
x.append('Java')

# Remove item com o valor php
x.remove('php')
print(x)

# Remove item na posição 1
del x[1]
print(x)

x = [
    'java', 'php', 'python'
]

z = ['windows', 'linux']

# JUNTA DUAS LISTAS
print(x+z)

x.insert(1, 'golang')
print(x)

print(x.count('php'))

print(x.reverse())