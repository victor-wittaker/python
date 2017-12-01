def dec_mostra(func):
    def nova_func(num1, num2):
        return "Resultado: " + str(func(num1, num2))
    return func


def soma(num1, num2):
    return num1 + num2

@dec_mostra
def sub(num1, num2):
    return num1 - num2

resultado = dec_mostra(soma)

print(resultado(2, 4))

print(sub(2, 1))

#############