class Animal:

    def __init__(self, especie, nombre, edad, nivel_salud, nivel_felicidad):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
        self.nivel_salud = nivel_salud
        self.nivel_felicidad = nivel_felicidad

    def __str__(self):
        return f"Animal: Nombre {self.nombre} - Edad {self.edad} - Salud {self.nivel_salud} - Felicidad {self.nivel_felicidad} "

    def display_info(self):
        print(f'''
                Nombre:    {self.nombre}
                Edad:      {self.edad}
                Salud:     {self.nivel_salud}%
                Felicidad: {self.nivel_felicidad}''')
        return self
    def alimento(self):
        self.nivel_salud += 10
        self.nivel_felicidad +=10
        return self

if __name__ == '__main__':
    try:
        animal1=Animal("Animal", "Seba", 12, 20, 30)
        print(animal1)
        animal1.alimento()
        animal1.display_info()
    except Exception as error:
        print("Error", error)
        print("Verifique el Error")





        


