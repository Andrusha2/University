from ForGit.PracticalWorks.WheelOfFortune.record import *
from ForGit.PracticalWorks.WheelOfFortune.game_code import *


def start_game():
    current_record = game(word_list)
    record(total_record, current_record)
