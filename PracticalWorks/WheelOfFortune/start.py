from ForGit.PracticalWorks.WheelOfFortune.game_code import *
from ForGit.PracticalWorks.WheelOfFortune.record import *


def start_game():
    current_record = game(word_list)
    record(total_record, current_record)
