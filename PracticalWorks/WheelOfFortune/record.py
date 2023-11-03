words = open("words.txt", "r+")
words.seek(0)
total_record = int(words.readline())


def record(total_record, current_record):
    if current_record > total_record:
        print("New record!!!")
        print(current_record)
        words.seek(0)
        words.write(str(current_record))
        words.close()
    elif current_record == total_record:
        print("Same record")
        print(current_record)
    else:
        print(f"You need {total_record - current_record + 1} more points to reach a new record")
        print(f"Your score is {current_record}")
