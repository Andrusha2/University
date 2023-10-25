from ForGit.PracticalWorks.Paradoxes.TheMontyHallProblem import *


def montyHall():
    while True:
        func = int(input("Choose function:\n0. Automode\n1. Play\n2. Stats\n3. Exit\n"))
        if func == 0:
            for i in range(int(input("How many times would you like to test\n"))):
                automode()
            print(*stats(changedwinc, mainc))
            ex()
        elif func == 1:
            print(play(input("Choose number: 0, 1 or 2\n")))
        elif func == 2:
            print(*stats(changedwinc, mainc))
        else:
            ex()

