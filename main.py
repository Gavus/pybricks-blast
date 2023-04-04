from blast import Blast, Stop


def main():
    """ TODO """
# Initialize Blast
    blast = Blast()

    # Activate his display and calibrate his arms
    blast.activate_display()
    blast.calibrate_arms()

    # Blast exercises his arms
    blast.arm_movement_motor.run_angle(
        speed=1000,
        rotation_angle=800,
        then=Stop.HOLD,
        wait=True)
    blast.arm_movement_motor.run_angle(
        speed=1000,
        rotation_angle=-800,
        then=Stop.HOLD,
        wait=True)

    # Blast attempts to do a rectangle.
    for _ in range(0, 8):
        blast.move_forward(200)
        blast.turn_right(90)


if __name__ == "__main__":
    main()
