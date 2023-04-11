"""
This program is for Blast's basic warm-up actions. 

It's simply a demo, showing what Blast can do.
"""

from blast import Blast
from pybricks.tools import wait


def run_demo():
    blast = Blast()
    blast.calibrate_arms()

    # Demo. Replace code here.
    blast.move_forward(300)
    blast.move_backward(300)
    wait(100)
    blast.turn_left(30)
    blast.raise_cannon(rotation_angle=400)
    blast.shoot_cannon()
    blast.turn_right(30)
    blast.lower_cannon(rotation_angle=100)
    blast.shoot_cannon()
    blast.hub.speaker.beep()
