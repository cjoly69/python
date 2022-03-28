annee_naissance = input("Année de naissance : ")
annee_naissance = int(annee_naissance)
annee_actuelle = 2022  # datetime.date.today().year
age = annee_actuelle - annee_naissance
print(f'Votre age est : { age }')
print('Votre age est : ' + str(age))

