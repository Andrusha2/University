def f(x_0, x_n, h_x):
    lst = []
    while x_0 <= x_n:
        if x_0 <= -2:
            lst.append([x_0, 4])
        elif -2 < x_0 < 2:
            lst.append([x_0, int(((16 - x_0 ** 2) ** 0.5) * 1000) / 1000])

        elif x_0 >= 2:
            lst.append([x_0, int((1.5 * x_0) * 1000) / 1000])
        x_0 += h_x
    return lst


print(f(float(input()), float(input()), float(input())))
