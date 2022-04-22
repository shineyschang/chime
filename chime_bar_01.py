import board
import time

from simpleio import map_range

from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

#

in_0 = AnalogIn(board.A0)
in_1 = AnalogIn(board.A1)
in_2 = AnalogIn(board.A2)
in_3 = AnalogIn(board.A3)
in_4 = AnalogIn(board.A4)
in_5 = AnalogIn(board.A5)
in_6 = AnalogIn(board.A6)
in_7 = AnalogIn(board.A7)
in_8 = AnalogIn(board.A8)
in_9 = AnalogIn(board.A9)
in_10 = AnalogIn(board.A10)
in_11 = AnalogIn(board.A11)
in_12 = AnalogIn(board.A12)
in_13 = AnalogIn(board.A13)
in_14 = AnalogIn(board.A14)

#

while True:
    print(in_0.value, in_1.value, in_2.value, in_3.value, in_4.value, in_5.value, in_6.value, in_7.value, in_8.value, in_9.value, in_10.value, in_11.value, in_12.value, in_13.value, in_14.value, sep=",")

    time.sleep(.04)
