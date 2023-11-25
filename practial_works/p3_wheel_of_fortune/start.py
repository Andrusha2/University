from ForGit.practial_works.p3_wheel_of_fortune.record import *
from ForGit.practial_works.p3_wheel_of_fortune.game_code import *


def start_game():
    current_record = game(word_list)
    record(total_record, current_record)
