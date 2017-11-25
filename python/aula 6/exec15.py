# 15 - Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    __cor = None
    __circunferencia = None
    __material = None

    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material
        
    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor
    
    def get_circunferencia(self):
        return self.__circunferencia
    
    def set_circunferencia(self, circunferencia):
        self.__circunferencia = circunferencia

    def get_material(self):
        return self.__material
    def set_material(self, material):
        self.__material = material
    
    def trocaCor(self, novacor):
        self.__cor = novacor


bola_nova = Bola("Azul","10","plastico")
cor = bola_nova.get_cor()
print(cor)

bola_nova.set_cor("Amarelo")
cor =bola_nova.get_cor()
print(cor)
