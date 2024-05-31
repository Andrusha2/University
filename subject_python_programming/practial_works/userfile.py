import p1_p2_paradoxes
import p3_wheel_of_fortune
paradoxn = int(input("Which package would you like to run?\n"
                     "1. The Monty Hall Problem\n"
                     "2. The Birthday Problem\n"
                     "3. Wheel of fortune the game\n"))
if paradoxn == 1:
    p1_p2_paradoxes.montyHall()
elif paradoxn == 2:
    p1_p2_paradoxes.birthday()
elif paradoxn == 3:
    p3_wheel_of_fortune.start_game()
