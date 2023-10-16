from random import randint
changedwinc = []
stayedwinc = []


def play(usernumber):
    windoor = randint(0, 3)
    doors = [0, 0, 0]
    doors[windoor] += 1
    doorsstr = '012'
    closeddoor = doorsstr.replace(str(windoor), '').replace(usernumber, '')
    closeddoor = randint(int(closeddoor[0]), int(closeddoor[-1]) + 1)
    print(f"There was a goat, behind the {closeddoor} door")
    doors.pop(closeddoor)
    decicion = input("Would you like to change your mind?(yes/no)")
    if decicion == "yes":
        newchoice = doorsstr.replace(str(closeddoor), '').replace(usernumber, '')
        if newchoice == str(windoor):
            changedwinc.append(1)
            return "You won!"
        else:
            return "You lost!"
    else:
        if usernumber == windoor:
            stayedwinc.append(1)
            return "You won!"
        else:
            return "You lost!"
