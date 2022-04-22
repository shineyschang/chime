import board
import time

from simpleio import map_range

from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

#

in_15 = AnalogIn(board.A0)
in_16 = AnalogIn(board.A1)
in_17 = AnalogIn(board.A2)
in_18 = AnalogIn(board.A3)
in_19 = AnalogIn(board.A4)
in_20 = AnalogIn(board.A5)
in_21 = AnalogIn(board.A6)
in_22 = AnalogIn(board.A7)
in_23 = AnalogIn(board.A8)
in_24 = AnalogIn(board.A9)
in_25 = AnalogIn(board.A10)
in_26 = AnalogIn(board.A11)
in_27 = AnalogIn(board.A12)
in_28 = AnalogIn(board.A13)
in_29 = AnalogIn(board.A14)

#

while True:
    print(in_15.value, in_16.value, in_17.value, in_18.value, in_19.value, in_20.value, in_21.value, in_22.value, in_23.value, in_24.value, in_25.value, in_26.value, in_27.value, in_28.value, in_29.value, sep=",")

    time.sleep(.04)
