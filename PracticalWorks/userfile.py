import Paradoxes

paradoxn = int(input("Which package would you like to run?\n"
                     "1. The Monty Hall Problem\n"
                     "2. The Birthday Problem\n"))
if paradoxn == 1:
    Paradoxes.montyHall()
elif paradoxn == 2:
    Paradoxes.birthday()
