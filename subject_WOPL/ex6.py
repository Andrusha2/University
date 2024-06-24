def if_equal():
    n = int('1000', 2)
    if n == int('020', 4):
        print('020')
    if n == 10:
        print(10)
    if n == int('A', 16):
        print('A')
    if n == int('1', 8):
        print('1')
# 020


def difference():
    print(hex(int('1A', 16) - int('6', 16))[2:])
# 14


def compare():
    if int('22', 10) > int('21', 16):
        print('>')
    elif int('22', 10) < int('21', 16):
        print('<')
    else:
        print('=')
# <


def ascending_order():
    numbers = [['A1', 16], ['27', 8], ['32', 10], ['1A', 16]]
    sorted_list = [['0', 0]]
    for i in range(len(numbers)):
        current_number = int(numbers[i][0], numbers[i][1])
        sorted_min = int(sorted_list[-1][0], sorted_list[-1][1])
        if current_number < sorted_min:
            sorted_list.append(numbers[i])
            break
        for j in range(len(sorted_list)):
            if current_number > int(sorted_list[j][0], sorted_list[j][1]):
                sorted_list.insert(j, numbers[i])
                break
    sorted_list.pop(-1)
    return sorted_list
# [['A1', 16], ['32', 10], ['1A', 16], ['27', 8]]


def missed_number():
    number = int('2EDC4', 16)
    print(bin(number)[2:])
# 101110110111000100
