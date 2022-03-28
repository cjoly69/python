secretNum = 5
counter = 0

while counter < 3 :
    Number = int(input("please enter un integer between 0 - 10 : "))
    counter += 1
    if Number != secretNum:
        print(f'Please try again')
    else:
        print("Congrat !")
        break