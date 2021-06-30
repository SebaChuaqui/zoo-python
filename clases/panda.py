from clases.animales import Animal

class Panda(Animal):
    def __init__(self, especie, nombre, edad, nivel_salud, nivel_felicidad, atrib_unico):
        super().__init__(especie, nombre, edad, nivel_salud, nivel_felicidad)
        self.especie = "Panda"
        self.edad = 15
        self.nivel_salud = 20
        self.nivel_felicidad = 10
        self.atrib_unico = atrib_unico

    def alimento(self):
        self.nivel_salud += 45
        self.nivel_felicidad += 60
        print("Se ha alimentado al Panda")
        return self

    def duerme(self):
        self.nivel_salud += 30
        self.nivel_felicidad += 40
        print("El panda se ha alimentado")
        return self

    def display_info(self):
        print(f'''Soy el Panda: {self.nombre}, tengo: {self.edad} anios, mi salud es de: {self.nivel_salud} , mi felicidad es de: {self.nivel_felicidad} y duermo: {self.atrib_unico} horas.''')
        return self

if __name__== '__main___':
    try:
        panda1 = Panda("Panda", "Ale", 20, 40, 60, 30)
        panda1.display_info()
        panda1.alimento()
        panda1.display_info()
        panda1.duerme()
        panda1.display_info()
    except Exception as error:
        print("Error", error)
        print("Verifique el Error")

