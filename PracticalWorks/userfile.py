import P1P2Paradoxes
import P3WheelOfFortune
paradoxn = int(input("Which package would you like to run?\n"
                     "1. The Monty Hall Problem\n"
                     "2. The Birthday Problem\n"
                     "3. Wheel of fortune the game\n"))
if paradoxn == 1:
    P1P2Paradoxes.montyHall()
elif paradoxn == 2:
    P1P2Paradoxes.birthday()
elif paradoxn == 3:
    P3WheelOfFortune.start_game()
