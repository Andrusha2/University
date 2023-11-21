from ForGit.PracticalWorks.P3WheelOfFortune.record import *
from ForGit.PracticalWorks.P3WheelOfFortune.game_code import *


def start_game():
    current_record = game(word_list)
    record(total_record, current_record)
