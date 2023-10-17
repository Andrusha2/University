import MontyHallProblem
import TheBirthdayProblem
paradoxn = int(input("Which problem would you like to solve?\n"
                     "1. The Monty Hall Problem\n"
                     "2. The Birthday Problem\n"))

if paradoxn == 1:
    MontyHallProblem.show()
elif paradoxn == 2:
    TheBirthdayProblem.show()