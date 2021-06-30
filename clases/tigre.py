from clases.animales import Animal

class Tigre(Animal):
    
    def __init__(self, especie, nombre, edad, nivel_salud, nivel_felicidad):
        super().__init__(especie, nombre, edad, nivel_salud, nivel_felicidad)
        self.especie = "Tigre"
        self.edad = 20
        self.nivel_salud = 15
        self.nivel_felicidad = 25

    def alimento(self):
        self.nivel_salud += 10
        self.nivel_felicidad += 15
        print("Se ha alimentado al Tigre")
        return self

    def display_info(self):
        print(f'''Soy el Tigre: {self.nombre}, tengo: {self.edad} anios, mi salud es de: {self.nivel_salud} y mi felicidad es de: {self.nivel_felicidad}''') 
        return self

if __name__== '__main___':
    try:
        tigre1 = Tigre("Tigre", "Alfonsino", 21, 20, 40)
        tigre1.display_info()
        tigre1.alimento()
        tigre1.display_info()
    except Exception as error:
        print("Error", error)
        print("Verifique el Error")







