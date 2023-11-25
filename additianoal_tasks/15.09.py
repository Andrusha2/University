from random import *

a = 0
count = 0
chislo = randint(0, 100)
while a == 0:
    otvet = input("vvedite chislo ")
    if otvet == "Выход":
        exit(0)
    otvet = int(otvet)
    count += 1
    if otvet == chislo:
        print("You have guessed, well done")
        print(f"It took {count} tries")
        a = 1
    elif chislo > otvet:
        print("The number is bigger")
    else:
        print("The number is less")
