from .game import *


def show():
    while True:
        func = int(input("Choose function:\n1. Play\n2. Stats\n3. Exit\n"))
        if func == 1:
            print(play(input("Choose number: 0, 1 or 2\n")))
        elif func == 2:
            print(stats(changedwinc, mainc))
        else:
            ex()

