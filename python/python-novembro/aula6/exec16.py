class Quadrado:
    __lado = None

    def __init__(self, lado):
        self.__lado = lado

    def retornar_lado(self):
        return self.__lado

    def mudar_lado(self, lado):
        self.__lado = lado

    def area(self):
        return self.__lado * self.__lado