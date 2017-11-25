class SeresHumanos:
    __altura = None
    __peso = None
    __idade = 0
    __nome = None

    def get_altura(self):
        return self.__altura

    def __init__(self, altura, peso, nome):
        self.altura = altura
        self.peso = peso
        self.nome = nome

    def andar(self):
        pass
    
    def falar(self):
        pass

    def comer(self):
        pass

class Mulher(SeresHumanos):
    gestante = None

    # def __init__(self, gestante, nome, altura, peso):
    #     super().__init__(altura, peso, nome)
    #     self.gestante = gestante


maria = Mulher(True, 'maria', 1.75, 85)
print(maria.altura)