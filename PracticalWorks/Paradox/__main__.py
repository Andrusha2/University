from ForGit.PracticalWorks.Paradox.TheMontyHallProblem import montyHall
from ForGit.PracticalWorks.Paradox.TheBirthdayProblem import birthday

if __name__ == '__main__':
    paradoxn = int(input("Which problem would you like to solve?\n"
                         "1. The Monty Hall Problem\n"
                         "2. The Birthday Problem\n"))

    if paradoxn == 1:
        montyHall()
    elif paradoxn == 2:
        birthday()
