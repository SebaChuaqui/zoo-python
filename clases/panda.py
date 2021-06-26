from clases.animales import Animal

class Panda(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)

        self.edad = 15
        self.nivel_salud = 20
        self.nivel_felicidad = 10

    def alimento(self):
        self.nivel_salud += 45
        self.nivel_felicidad += 60
        return self

    def duerme(self):
        self.nivel_salud += 30
        self.nivel_felicidad += 40
        return self

    def display_info(self):
        print(f'''Soy el Panda: {self.nombre}, 
                tengo: {self.edad} anios,
                mi salud es de: {self.nivel_salud} y 
                mi felicidad es de: {self.nivel_felicidad}''') 
        return self

