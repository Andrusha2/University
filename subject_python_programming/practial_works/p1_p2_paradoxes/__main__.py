from ForGit.subject_python_programming.practial_works.p1_p2_paradoxes import *

if __name__ == '__main__':
    paradoxn = int(input("Which problem would you like to solve?\n"
                         "1. The Monty Hall Problem\n"
                         "2. The Birthday Problem\n"))

    if paradoxn == 1:
        montyHall()
    elif paradoxn == 2:
        birthday()
