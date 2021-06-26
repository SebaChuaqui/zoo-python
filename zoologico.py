from clases.tigre import Tigre
from clases.panda import Panda
from clases.tiburon import Tiburon
from colorama import init, Fore, Back, Style
init()

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




