from random import randint
changedwinc = []
mainc = []


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


def play(usernumber):
    windoor = randint(0, 2)
    doors = [0, 0, 0]
    doors[windoor] += 1
    doorsstr = '012'
    closeddoor = doorsstr.replace(str(windoor), '').replace(usernumber, '')
    closeddoor = randint(int(closeddoor[0]), int(closeddoor[-1]))
    print(f"There was a goat, behind the {closeddoor} door")
    doors.pop(closeddoor)
    decicion = input("Would you like to change your mind?(yes/no)\n")
    mainc.append(1)
    if decicion == "yes":
        newchoice = doorsstr.replace(str(closeddoor), '').replace(usernumber, '')
        if newchoice == str(windoor):
            changedwinc.append(1)
            return "You won!"
        else:
            return "You lost!"
    else:
        if usernumber == str(windoor):
            return "You won!"
        else:
            changedwinc.append(1)
            return "You lost!"


def automode():
    usernumber = str(randint(0, 2))
    windoor = randint(0, 2)
    doors = [0, 0, 0]
    doors[windoor] += 1
    doorsstr = '012'
    closeddoor = doorsstr.replace(str(windoor), '').replace(usernumber, '')
    closeddoor = randint(int(closeddoor[0]), int(closeddoor[-1]))
    doors.pop(closeddoor)
    decicion = randint(0, 1)
    mainc.append(1)
    if decicion == 'yes':
        newchoice = doorsstr.replace(str(closeddoor), '').replace(usernumber, '')
        if newchoice == str(windoor):
            changedwinc.append(1)
    else:
        if usernumber != str(windoor):
            changedwinc.append(1)


def stats(changedwinc, mainc):
    winpersent = sum(changedwinc) / sum(mainc) * 100
    return f"{winpersent}% of wins when the door was changed", f"{100 - winpersent}% of win when the door wasn't changed"


def ex():
    return exit()

