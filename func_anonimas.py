# Funcao sem nome definido, alocada em uma variavel
# lambda: nome reservado para essa funcao sem nome
funcao = lambda x: x * 2

print(funcao(2))

funcao2 = [
    lambda x: x + 2,
    lambda x: x * 2,
    lambda x: x - 2
]

print(funcao2[1](10))