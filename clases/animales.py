class Animal:

    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
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
        


