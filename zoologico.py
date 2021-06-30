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

panda1 = Panda("Panda", "Ditto", 16, 30, 40, 50)
panda1.alimento()
panda1.duerme()
panda1.display_info()

tiburon1 = Tiburon("Tiburon", "Renato", 10, 70, 40, 40)
tiburon1.alimento()
tiburon1.nadar()
tiburon1.display_info()

zoo1= Zoo("TP Zoo")
zoo1.add_tigre(tigre1)
zoo1.add_panda(panda1)
zoo1.add_tiburon(tiburon1)
zoo1.imprimir_info()







