from random import randint

from ForGit.PracticalWorks.P3WheelOfFortune.hp import difficulty

path = "\\".join(list(__file__.split('\\'))[:-1]) + "\\words.txt"

with open(path, "a+") as words:
    words.seek(0)
    word_list = list(map(lambda x: x.lower(), words.read().split()))


def game(word_list):
    playing = True
    current_record = 0
    while playing and len(word_list) > 1:
        word = word_list[randint(1, len(word_list) - 1)]
        word_list.remove(word)
        hidden_word = list('■' * len(word))
        word_l = list(word)
        health = difficulty(input("Choose the difficulty level\n"
                                  "1. easy\n2. normal\n3. hard\n"))
        while health > 0:
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
            if user_letter in word_l and user_letter != '':
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
    if len(word_list) == 1:
        print("You guessed whole word list!")
    return current_record


def cont():
    if input("Would you like to continue? (1. yes|2. no) ") == '1':
        return 1
    else:
        return 0

