from blast import Blast
from pybricks.tools import wait


def run_challenge():
    blast = Blast()
    blast.calibrate_arms()
    wait(500) # Wait 0.5s.
    blast.hub.speaker.beep()
