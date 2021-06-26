from clases.animales import Animal

class Tigre(Animal):
    
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        
        self.edad = 20
        self.nivel_salud = 15
        self.nivel_felicidad = 25

    def alimento(self):
        self.nivel_salud += 10
        self.nivel_felicidad += 5
        return self

    def display_info(self):
        print(f'''Soy el Tigre: {self.nombre}, tengo: {self.edad} anios, mi salud es de: {self.nivel_salud} y mi felicidad es de: {self.nivel_felicidad}''') 
        return self





