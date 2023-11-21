from ForGit.PracticalWorks.P7BooksSearch import *

if __name__ == '__main__':
    lst = get_books(input('Type the search word here: '))
    min_sum = int(input('Enter the minimum amount: '))
    add = int(input('Enter how many should be added: '))
    result = get_totals(lst, min_sum, add)
    print(result)
    with open(input('Enter the name of the new file: '), 'w') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\r')
        for i in result:
            writer.writerow(i)
