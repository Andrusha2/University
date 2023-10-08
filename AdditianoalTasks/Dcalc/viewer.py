from dcalc import *


def lcreate(*args, **kwargs):
    dic = {}
    for i in range(len(args)):
        dic[f"Point {i}"] = deg_to_gms(args[i])
    for i in kwargs:
        kwargs[i] = deg_to_gms(kwargs[i])
    return list(map(lambda x: f"{x[0]} = {x[1]}", (dic | kwargs).items()))


print(lcreate(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706440))
# 172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706440