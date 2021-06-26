from clases.tigre import Tigre
from clases.panda import Panda
from clases.tiburon import Tiburon

class Zoo():
    def __init__(self, zoo_name):
        self.animales = []
        self.name = zoo_name

    def add_tigre(self,animal):
        self.animales.append(animal)

    def add_panda(self,animal):
        self.animales.append(animal)

    def add_tiburon(self,animal):
        self.animales.append(animal)
    
    def imprimir_info(self):
        print("-"*20, self.name, "-"*20)
        for animal in self.animales:
            animal.display_info()

tigre1 = Tigre("Tigrito", 12, 15, 30)
tigre1.display_info()
panda1 = Panda("PO", 10, 30, 35)
panda1.display_info()
tiburon1 = Tiburon("Calafate", 14, 50, 5)
tiburon1.display_info()

zoo1 = Zoo("TP Zoo")
zoo1.add_tigre(tigre1)
zoo1.add_panda(panda1)
zoo1.add_tiburon(tiburon1)
zoo1.imprimir_info()







