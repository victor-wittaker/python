class Bola:
    __cor = 'Preto'
    __circ = 3.14
    __material = 'Couro'

    def __init__(self, cor, circ, material):
        self.__cor = cor
        self.__circ = circ
        self.__material = material
    
    def set_cor(self, cor):
        self.__cor = cor

    def get_cor(self):
        return self.__cor

    def mostrar_cor(self):
        return self.get_cor()

    def trocar_cor(self, cor):
        self.set_cor(cor)

objeto = Bola('Azul', 3.15, 'Plastico')

print(objeto.mostrar_cor())

objeto.trocar_cor('Amarelo')

print(objeto.mostrar_cor())

