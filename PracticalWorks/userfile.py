import Paradoxes
import WheelOfFortune
paradoxn = int(input("Which package would you like to run?\n"
                     "1. The Monty Hall Problem\n"
                     "2. The Birthday Problem\n"
                     "3. Wheel of fortune the game\n"))
if paradoxn == 1:
    Paradoxes.montyHall()
elif paradoxn == 2:
    Paradoxes.birthday()
elif paradoxn == 3:
    WheelOfFortune.start_game()
