from random import randint

from ForGit.PracticalWorks.WheelOfFortune.hp import *

with open("words.txt", "a+") as words:
    words.seek(0)
    word_list = words.read().split()


def game(word_list):
    playing = True
    current_record = 0
    while playing:
        word = word_list[randint(1, len(word_list) - 1)]
        hidden_word = list(word.replace(word, '■' * len(word)))
        word_l = list(word)
        health = difficulty(input("Choose the difficulty level\n"
                                  "1. easy\n2. normal\n3. hard\n"))
        while health > 0 :
            print(f"{''.join(hidden_word)} | ❤x{health}")
            user_letter = input("Choose a letter or type the whole word: ")
            if len(user_letter) > 1:
                if user_letter == word:
                    print(word)
                    print("You won! Receive the prizes!")
                    current_record += 1
                    if cont():
                        break
                    else:
                        playing = False
                        break
                else:
                    print("You lost!")
                    playing = False
                    break
            if user_letter in word_l:
                letter_index = word_l.index(user_letter)
                hidden_word[letter_index] = user_letter
                word_l[letter_index] = ''
                if ''.join(hidden_word) == word:
                    print(word)
                    print("You won! Receive the prizes!")
                    if cont():
                        current_record += 1
                        break
                    else:
                        playing = False
                        break
            else:
                print("Wrong. You lose life")
                health -= 1
                if health == 0:
                    print("You lost!")
                    playing = False
    return current_record


def cont():
    if input("Would you like to continue? (yes|no) ") == 'yes':
        return 1
    else:
        return 0


