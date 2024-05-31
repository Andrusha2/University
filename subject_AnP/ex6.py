spis = input().split()
flag = False
if len(spis) % 2 != 0:
    flag = True
    lst = spis[-1]
    spis.pop(-1)
for i in range(0, len(spis), 2):
    spis[i], spis[i + 1] = spis[i + 1], spis[i]

if flag:
    spis.append(lst)
    print(spis)
else:
    print(spis)

# O(n)