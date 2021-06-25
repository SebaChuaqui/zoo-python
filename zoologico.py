class Zoo:

    def __init__(self,  zoo_nombre):
        self.zoo_nombre = zoo_nombre
        self.animales = []

    def agregar_tigre(self, nombre):
        self.animales.append(Tigre(nombre))
        return self

    def agregar_panda(self,nombre):
        self.animales.append(Panda(nombre))
        return self

    def agregar_jirafa(self, nombre):
        self.animales.append(Jirafa(nombre))

    def imprimir_info(self):
        print("-"*20, self.zoo_nombre, "-"*20)
        for animal in self.animales:
            animal.info()
        print("-"*20, self.zoo_nombre, "-"*20)
        return self

class Tigre:

class Panda:

class Jirafa:






