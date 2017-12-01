class Pessoa:
    __nome = None
    __idade = None
    __peso = None
    __altura = None

    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def envelhecer(self, idade):
        self.__idade += idade

    def engordar(self, kilos):
        self.__peso += kilos

    def emagrecer(self, kilos):
        self.__peso -= kilos

    def crescer(self, altura):
        self.__altura += altura