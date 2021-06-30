from clases.animales import Animal

class Tiburon(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad, atrib_unico):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        
        self.especie = "Tiburon"
        self.edad = 15
        self.nivel_salud = 20
        self.nivel_felicidad = 10
        self.atrib_unico = 100

    def alimento(self):
        self.nivel_salud += 30
        self.nivel_felicidad += 30
        print("Se ha alimentado al Tiburon")
        return self

    def nadar(self):
        self.nivel_salud += 15
        self.nivel_felicidad += 35
        print("El tiburon nado hasta agotarse")
        return self
    
    def display_info(self):
        print(f'''Soy el Tiburon: {self.nombre}, tengo: {self.edad} anios, mi salud es de: {self.nivel_salud}, mi felicidad es de: {self.nivel_felicidad} y hoy nade: {self.nadar}''')
        return self
    
if __name__== '__main___':
    try:
        tiburon1 = Tiburon("Tiburon", 30, 30, 40, 25)
        tiburon1.display_info()
        tiburon1.alimento()
        tiburon1.display_info()
        tiburon1.nadar()
        tiburon1.display_info()
    except Exception as error:
        print("Error", error)
        print("Verifique el Error")





