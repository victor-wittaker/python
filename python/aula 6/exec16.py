# 16 - Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    __lado = None

    def __init__(self, lado):
        self.__lado = lado

    def get_lado(self):
        return self.__lado
    
    def set_lado(self, lado):
        self.__lado = lado

    def mudar_lado (self, novo_valor):
        self.__lado = novo_valor
    
    def calcula_area (self):
        return (print((self.__lado * 4)))


quadrado_novo = Quadrado(4)
print(quadrado_novo.get_lado())
quadrado_novo.calcula_area()
