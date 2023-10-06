phoneBook = {}
def add(name, number):
    phoneBook[name] = number
def delete(name):
    del phoneBook[name]
def check():
    tuple(map(lambda x: print(*x), phoneBook.items()))
def change(name):
    phoneBook[name] = input("Type new number")
