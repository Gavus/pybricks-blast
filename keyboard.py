"""
This program is for controlling Blast using the keyboard.

q Lower cannon.
e Raise cannon.
f Shoot cannon.

w Move forward.
s Move backward.
a Turn left.
d Turn right.
"""

from usys import stdin
from uselect import poll

from demo import Blast

def keyboard_listen(blast):
    keyboard = poll()
    keyboard.register(stdin)
    forward = 'w'
    backward = 's'
    turn_left = 'a'
    turn_right = 'd'
    lower_cannon = 'q'
    raise_cannon = 'e'
    shoot_cannon = 'f'

    while True:
        # Only supports on key at a time.
        key = stdin.read(1)

        if forward in key:
            blast.move_forward(50, False)
        elif backward in key:
            blast.move_backward(50, False)
        elif turn_left in key:
            blast.turn_left(15, False)
        elif turn_right in key:
            blast.turn_right(15, False)
        elif raise_cannon in key:
            blast.raise_cannon(50, False)
        elif lower_cannon in key:
            blast.lower_cannon(50, False)
        elif shoot_cannon in key:
            blast.shoot_cannon()
        else:
            blast.drive_base.stop()
            blast.arm_movement_motor.stop()
    

def run_keyboard():
    blast = Blast()      
    keyboard_listen(blast)