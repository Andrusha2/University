from random import *
a = []
for i in range(7):
    a.append([])
    for j in range(7):
        a[i].append(randint(-19, 19))
b = a.copy()
for i in range(len(b)):
    mx = max(b[i], key=abs)
    b[i] = [int((x / mx) * 1000) / 1000 for x in b[i]]
