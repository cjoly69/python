nombreMult = int(input('donner un nombre à multiplier : '))

for i in range(1,11) :
    print (f'{i} x {nombreMult} = {i * nombreMult}')
###############################################################
print(f'table des {nombreMult}')
a = 0

while a <= 11:
    a += 1
    c = a * nombreMult
    print( str(nombreMult)+' x '+str(a)+' ='+str(c))

