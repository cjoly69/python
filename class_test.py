class Homme:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = int(age)


H1 = Homme('Toto', 'titi', 22)
H2 = Homme('Tata', 'Duduche', 12)
print(f"{H1.prenom} {H1.nom} a {H1.age} ans")
print(f"{H2.prenom} {H2.nom} a {H2.age} ans")
