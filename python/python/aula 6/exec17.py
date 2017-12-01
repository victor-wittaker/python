# 17 - Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.

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
    
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_idade(self):
        return self.__idade
    def set_idade(self, idade):
        self.__idade = idade
    def get_peso(self):
        return self.__peso
    def set_altura(self, altura):
        self.__altura = altura
    
    def envelhecer(self, mais_idade):
        return (self.__idade + mais_idade)
    def engordar(self, mais_peso):
        return (self.__peso + mais_peso)
    def crescer(self, mais_altura):
        return (self.__altura + mais_altura)
    
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
peso = input("Digite o peso: ")
altura = input("Digite a altura: ")

pessoa_nova = Pessoa(nome, int(idade), float(peso), float(altura))

print(pessoa_nova.envelhecer(4))
print(pessoa_nova.engordar(4))
print(pessoa_nova.crescer(0.4))