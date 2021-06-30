from clases.tigre import Tigre
from clases.panda import Panda
from clases.tiburon import Tiburon

class Zoo():
    def __init__(self, zoo_name):
        self.animales = []
        self.name = zoo_name

    def add_tigre(self, animal):
        self.animales.append(animal)

    def add_panda(self, animal):
        self.animales.append(animal)

    def add_tiburon(self, animal):
        self.animales.append(animal)
    
    def imprimir_info(self):
        print("-"*20, self.name, "-"*20)
        for animal in self.animales:
            animal.display_info()

tigre1 = Tigre("Tigre", "Alfonsino", 15, 20, 30)
tigre1.alimento()
tigre1.display_info()



zoo1 = Zoo("TP Zoo")
zoo1.add_tigre(Tigre)
zoo1.add_panda(Panda)
zoo1.add_tiburon(Tiburon)
zoo1.imprimir_info()




