from functions import *

if __name__ == '__main__':
    words = read_file('data.txt')
    save_file('count.txt', words)
