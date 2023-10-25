from ForGit.PracticalWorks.Paradoxes.TheMontyHallProblem import montyHall
from ForGit.PracticalWorks.Paradoxes.TheBirthdayProblem import birthday

if __name__ == '__main__':
    paradoxn = int(input("Which problem would you like to solve?\n"
                         "1. The Monty Hall Problem\n"
                         "2. The Birthday Problem\n"))

    if paradoxn == 1:
        montyHall()
    elif paradoxn == 2:
        birthday()
