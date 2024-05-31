from random import *


def mx(spis):
    res = 0
    for k in spis:
        if abs(k) > abs(res):
            res = k
    return res


def president():
    a = []
    for i in range(7):
        a.append([])
        for j in range(7):
            a[i].append(randint(-19, 19))
    b = a.copy()
    for i in range(len(b)):
        mxx = mx(b[i])
        b[i] = [int((x / mxx) * 1000) / 1000 for x in b[i]]
    return a, b


print(*president(), sep='\n')