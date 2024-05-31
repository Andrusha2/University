x = -30
lst = []
while x <= 50:
    if x <= -2:
        lst.append([x, 4])
    elif -2 < x < 2:
        lst.append([x,int(((16 - x ** 2) ** 0.5) * 1000) / 1000])

    elif x >= 2:
        lst.append([x, int((1.5 * x) * 1000) / 1000])
    x += 0.25
print(lst)

