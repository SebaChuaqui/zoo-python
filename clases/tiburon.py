from clases.animales import Animal

class Tiburon(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)

    def alimento(self):
        self.nivel_salud += 30
        self.nivel_felicidad += 30
        return self

    def nadar(self):
        self.nivel_salud += 15
        self.nivel_felicidad += 35
        return self
    
    def display_info(self):
        print(f'''Soy el Tiburón: {self.nombre}, 
                tengo: {self.edad} anios,
                mi salud es de: {self.nivel_salud} y 
                mi felicidad es de: {self.nivel_felicidad}''') 
        return self
    
    

