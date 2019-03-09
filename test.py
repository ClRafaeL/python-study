from Turn import Turn
from Corredor import Corredor

claudio = Corredor('07', 'Rafael')
turn1 = Turn(1, '1', 50)
turn2 = Turn(1.20, '2', 55)
turn3 = Turn(2.5, '3', 60)

claudio.add_turn(turn1)
claudio.add_turn(turn2)
claudio.add_turn(turn3)

res = claudio.calc_time_med()
print(res)