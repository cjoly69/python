# manger, move, descr methode abstraite

from abc import ABC, abstractmethod


class EtreVivant(ABC):
    @abstractmethod
    def manger(self):
        pass

    def move(self):
        pass

    def descr(self):
        pass


class Homme(EtreVivant):
    def __init__(self, nom, age, poste):
        self.nom = nom
        self.age = age
        self.poste = poste

    def manger(self):
        print('Je suis omnivore')

    def move(self):
        print('je me déplace à pied')


class Catherine(Homme):
    def __init__(self, nom, poste):
        super().__init__(nom, 0, poste)

    def move(self):
        print(f"Bonjour, moi c'est {self.nom} et je travaille au poste de {self.poste}!")

    def manger(self):
        print("J'aime manger et boire du vin")


C1 = Catherine('Cat', 'devops')
C1.move()
C1.manger()
