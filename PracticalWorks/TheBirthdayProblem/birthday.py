from random import randint
totalgroups = []
matchgroups = []


def createandequal():
    group = ([[randint(1, 28), randint(1, 12)] for i in range(23)])
    totalgroups.append(1)
    flag = False
    for i in range(0, len(group) - 1):
        for j in range(i + 1, len(group)):
            if group[i] == group[j]:
                matchgroups.append(1)
                flag = True
                if flag:
                    break
        if flag:
            break





def result(totalgroups, matchgroups):
    return sum(matchgroups) / sum(totalgroups)


