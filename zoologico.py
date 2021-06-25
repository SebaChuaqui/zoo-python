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
        print("-"*20, self.nombre, "-"*20)
        for animal in self.animales:
            animal.info()
        print("-"*20, self.nombre, "-"*20)
        return self

class Tigre(Zoo):
    def __init__(self, zoo_nombre):
        super().__init__(zoo_nombre)
    
    def info(self):
        print(f"{type(self).__nombre__}: {self.nombre}")

class Panda(Zoo):
    def __init__(self, zoo_nombre):
        super().__init__(zoo_nombre)
    
    def info(self):
        print(f"{type(self).__nombre__}: {self.nombre}")

class Jirafa(Zoo):
    def __init__(self, zoo_nombre):
        super().__init__(zoo_nombre)
    
    def info(self):
        print(f"{type(self).__nombre__}: {self.nombre}")

zoo1 = Zoo(input("Ingrese nombre del zoologico:"))









