"""
This program is for Blast's basic warm-up actions. 

It's simply a demo, showing what Blast can do.
"""

from blast import Blast
from pybricks.tools import wait


def run_demo():
    blast = Blast()
    blast.calibrate_arms()

    # Demo
    blast.move_forward(300)
    blast.move_backward(300)
    wait(100)
    blast.turn_left(90)
    blast.raise_cannon(45)
    blast.shoot_cannon()
    blast.turn_right(90)
    blast.lower_cannon(45)
    blast.shoot_cannon()
    blast.hub.speaker.beep()
