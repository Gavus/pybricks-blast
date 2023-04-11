"""
Introduce a class Blast named after the Blast robot.

Makes it easier to use Blast.
"""

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase


class Blast:
    WHEEL_DIAMETER = 44
    AXLE_TRACK = 100
    __times_shot = 0

    def __init__(self):
        """ Initialize the blast robot with all it's motors. """
        self.hub = InventorHub()

        # Configure the drive base
        self.left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.F)
        self.drive_base = DriveBase(self.left_motor,
                                    self.right_motor,
                                    wheel_diameter=self.WHEEL_DIAMETER,
                                    axle_track=self.AXLE_TRACK)
        self.drive_base.settings(
            straight_speed=165*3/4,
            straight_acceleration=576/2,
            turn_rate=158/3,
            turn_acceleration=660)

        # Configure other motors and sensors
        self.arm_movement_motor = Motor(Port.C)
        self.action_motor = Motor(Port.E)
        self.color_sensor = ColorSensor(Port.B)
        self.distance_sensor = UltrasonicSensor(Port.A)

    def calibrate_arms(self):
        """
        Calibrate arms so that the cannon sort of horizontal with the ground.
        """
        self.arm_movement_motor.run_until_stalled(
            speed=1000)

        self.arm_movement_motor.run_angle(speed=500, rotation_angle=-1500, wait=False)
        while True:
            if self.distance_sensor.distance() < 100:
                self.arm_movement_motor.stop()
                self.arm_movement_motor.run_angle(speed=500, rotation_angle=-350, wait=True)
                break

    def shoot_cannon(self):
        """ Shoots one projectile from the cannon."""
        direction = 1 if self.__times_shot % 2 else -1
        self.action_motor.run_until_stalled(speed=direction*500)
        self.action_motor.run_angle(speed=500, rotation_angle=-direction*75)
        self.__times_shot += 1

    def raise_cannon(self, rotation_angle, wait=True):
        """ Raise the cannon arm with specified rotation_angle. """
        self.arm_movement_motor.run_angle(200, -1*rotation_angle, wait=wait)

    def lower_cannon(self, rotation_angle, wait=True):
        """ Lower the cannon arm with specified rotation_angle. """
        self.arm_movement_motor.run_angle(200, rotation_angle, wait=wait)

    def move_forward(self, distance, wait=True):
        """ Move blast straight forward with specified distance in mm. """
        self.drive_base.straight(distance, wait=wait)

    def move_backward(self, distance, wait=True):
        """ Move blast straight backward with specified distance in mm. """
        self.drive_base.straight(-1*distance, wait=wait)

    def turn_left(self, angle, wait=True):
        """ Turn left with specified degree angle. """
        self.drive_base.turn(angle=-angle, wait=wait)

    def turn_right(self, angle, wait=True):
        """ Turn right with specified degree angle. """
        self.drive_base.turn(angle=angle, wait=wait)
