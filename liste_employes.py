liste_employes = dict({})
i = 1

print("Entrer un nouvel employé : ")
choix = input("y or n ? ")
if choix == "y":
    nom = input('Votre nom est : ')
    prenom = input('Votre prénom est : ')
    age = input('Votre age est : ')
    salaire = input('Votre salaire est : ')
    role = input('role : ')

    liste_employes.update({i: {"nom": nom, "prenom": prenom, "age": age, "salaire": salaire, "role": role}})
    i += 1
    for key in liste_employes.items():
        print(liste_employes.items())
else:
    print("bye")