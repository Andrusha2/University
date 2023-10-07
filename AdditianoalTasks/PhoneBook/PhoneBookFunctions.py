phoneBook = {}


def namestd(name):
    name = name.split()
    result = ''
    for i in range(len(name)):
        result += name[i][0].upper() + name[i][1:].lower() + ' '
    return result


def numstd(number):
    return "+7" + str(number)[-10:]


def add(name, number):
    phoneBook[namestd(name)] = numstd(number)


def delete(name):
    del phoneBook[namestd(name)]


def check():
    tuple(map(lambda x: print(*x), phoneBook.items()))


def change(name):
    phoneBook[namestd(name)] = numstd(input("Enter new phone number: "))


