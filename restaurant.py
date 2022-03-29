'''

Bienvenue au Banana Club
Choisissez votre banana  split préféré

1 - banana choco
2 - banana caramel
3 - banana fraise

'''

menuBanana = ("banana choco", "banana caramel", "banana fraise")
print('Bienvenue au Banana Club\nChoisissez votre banana  split préféré')
for i in menuBanana:
    print(f"{menuBanana.index(i) + 1} - {i}")
while True:
    try:
        command = int(input("Quel est votre choix ? "))
        if command == -1:
            print('Merci pour votre commande')
            break
        elif command < 1 or command > len(menuBanana):
            print('rupture de stock')
        else:
            print(f"Vous avez commandé {menuBanana[command - 1]}")
    except ValueError:
        print("element introuvable")
