# tests sur quelques unes des méthodes et fonctions liées au type str

a = " AnAlaoienr "
b = "123"
print(type(a))  # retourne le type de donnée 'str'
print(len(a))  # retourne 12 => nombre de caractères de a
print(a.isupper())  # retourne false
print(a.islower())  # retourne false
print(a.upper())  # ANALAOIENR
print(a.isalpha())  # retourne False , car a contient un espace
print(b.isnumeric())  # true
print(b.isdecimal())  # true
print(a[2].isdigit())  # false
print(a.istitle())  # false => car a ne débute pas par une lettre majuscule
print(a.strip())  # AnAlaoienr => enleve l'espace qu'il y a au début et à la fin (idéal pour le nettoyage de fichiers)
print('x'.join(a))  # ajoute x à chaque élément de a =>  xAxnxAxlxaxoxixexnxrx
print(a.count("n"))
print('AnA' in a)
