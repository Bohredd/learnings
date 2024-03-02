from functools import cached_property


# criando uma classe

class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# instanciando uma classe
i30 = Carro("Hyundai", "i30")
print(i30)

# pegando atributos de uma classe
print(i30.marca)
print(i30.modelo)

# criando uma classe com funções

class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @staticmethod # usando esse decorator não precisa por self nem parâmetros
    def buzinar():
        print("Bibiii!")

i30 = Carro("Hyundai", "i30")
i30.buzinar()

# criando uma classe com funções que podem ser chamadas como atributos

class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @property
    def buzinar(self):
        print("Bibiii!")

i30 = Carro("Hyundai", "i30")
i30.buzinar

# criando uma classe com funções que podem ser chamadas como atributos que sempre terá o mesmo valor

class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @cached_property
    def buzinar(self):
        print("Bibiii!")

i30 = Carro("Hyundai", "i30")
i30.buzinar

# criando uma classe com funções que seta um dado

class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @staticmethod
    def buzinar():
        print("Bibiii!")

    def set_ano_fabricacao(self, anoFabricacao):
        self.anoFabricacao = anoFabricacao

i30 = Carro("Hyundai", "i30")
i30.set_ano_fabricacao("2009")
print(i30.anoFabricacao)

