from blast import Blast

def run_challenge():
    blast = Blast()
    blast.calibrate_arms()
    blast.hub.speaker.beep()