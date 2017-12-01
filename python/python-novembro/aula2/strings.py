var = "PYT''\"HON"
var = 'PYTH"ON'

# TODAS MAIUSCULAS
print(var.upper())

# TODAS MINUSCULAS
print(var.upper())

# SUBSTITUI T POR X
print(var.replace('T', 'X'))

# PRIMEIRA LETRA MAIUSCULA0
print(var.title())

# CONTA QUANTIDADE DE LETRAS T
print(var.count('T'))

# PROCURAR POSIÇÃO DA LETRA T
print(var.find('T'))

# QUANTIDADE DE CARACTERES DA STRING
print(len(var))

# JUNTA UMA LISTA EM UMA STRING
print(', '.join(['a', 'b', 'c']))

# EXPLODE UMA STRING EM UMA LISTA
print(var.split(','))

var = "PYTHON"

print(var[-4])
# T

print(var[2:6])
# 'THON'

print(var[:-1])
# 'PYTHO'

print(var[-1:])
# 'N'

print(var[-3:])
# 'HON'

print(var[::-1])
# 'NOHTYP'

# CONCATENAÇÃO
nome = "Gabriel"
idade = 27
var = "SEU NOME É: " + "GABRIEL"
var = "SEU NOME É: %s TENHO %s ANOS" % (nome, idade)

var = "SEU NOME É: {0} TENHO {1} ANOS".format(nome[0:3], idade)

print(var)
