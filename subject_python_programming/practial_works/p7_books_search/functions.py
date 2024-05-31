import csv
import re


def get_books(search_word):
    f = open("books.csv")
    f.readline()
    reader = csv.reader(f, delimiter='|')
    books_list = list()
    for i in reader:
        if re.search(f'{search_word}', i[1].lower()):
            books_list.append(i)
    return books_list


def get_totals(book_list, m, add):
    id_price = list()
    for i in book_list:
        total = round(float(i[-1]) * int(i[-2]), 3)
        if total < m:
            tp = (i[0], total + add)
            id_price.append(tp)
        else:
            tp = (i[0], total)
            id_price.append(tp)
    return id_price
