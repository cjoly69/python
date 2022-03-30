class Animal:
    def __init__(self, nom, couleur, genre):
        self.nom = nom
        self.couleur = couleur
        self.genre = genre

    def display(self):
        print(f'le {self.nom} a une couleur {self.couleur} et le genre {self.genre}')

    def manger(self):
        print('Je mange de tout')


class Carnivore(Animal):
    def manger(self):
        print('Je mange de la viande')


class CarniSauvage(Carnivore):
    __doc__
    '''
    Classe d'animaux sauvages qui sont aussi carnivore
    '''
# pour utiliser une methode en mandatory __init__ comme suit
    def __init__(self, nom, couleur):
        super().__init__(nom, couleur, genre="sauvage")

    def parler(self):
        print("Je vis dans la forêt !")


def main():
    A1 = Animal('Toto', 'Rose', 'domestique')
    A1.display()
    A1.manger()
    A2 = CarniSauvage('Gilles', 'gris')
    A2.display()
    A2.manger()
    A2.parler()


main()
