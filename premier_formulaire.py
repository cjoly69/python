"""
Formulaire :
Demander à l’utilisateur de remplir un formulaire contenant(nom, prénom, email,
adresse, ville , pays, profession, numéro de téléphone ).
Puis retournez-lui un message contenant ses informations
"""
nom = input('Votre nom est : ')
prenom = input('Votre prénom est : ')
mail = input('Votre email est : ')
address = input('Votre adresse est : ')
ville = input('La ville : ')
pays = input('Le Pays : ')
phone = input('Votre téléphone : ')

print(f'Bonjour { prenom } { nom }, votre email est {mail}, \nà l\'adresse {address}\n{ville}\n{pays}\nVotre numéro de téléphone : {phone}')





