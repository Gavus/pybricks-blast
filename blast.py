#!/usr/bin/env python3

"""
This program is for Blast's basic warm-up actions. 

Follow the corresponding building instructions in the LEGO® MINDSTORMS®
Robot Inventor App.
"""

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


class Blast:
    WHEEL_DIAMETER = 44
    AXLE_TRACK = 100

    def __init__(self):
        self.hub = InventorHub()

        # Configure the drive base
        self.left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.A)
        self.drive_base = DriveBase(self.left_motor,
                                    self.right_motor,
                                    wheel_diameter=self.WHEEL_DIAMETER,
                                    axle_track=self.AXLE_TRACK)

        # Configure other motors and sensors
        self.arm_movement_motor = Motor(Port.D)
        self.action_motor = Motor(Port.B)
        self.color_sensor = ColorSensor(Port.E)
        self.distance_sensor = UltrasonicSensor(Port.F)

    def activate_display(self):
        """ TODO """
        self.hub.display.orientation(up=Side.RIGHT)

        for _ in range(10):
            self.hub.display.image(
                image=[[00, 11, 33, 11, 00],
                       [11, 33, 66, 33, 11],
                       [33, 66, 99, 66, 33],
                       [11, 33, 66, 33, 11],
                       [00, 11, 33, 11, 00]])

            self.hub.light.on(color=Color.RED)

            wait(100)

            self.hub.display.off()
            self.hub.light.off()

            wait(100)

    def calibrate_arms(self):
        """ TODO """
        self.arm_movement_motor.run_until_stalled(
            speed=1000,
            then=Stop.HOLD)

        for _ in range(10):
            self.distance_sensor.lights.on(100)
            wait(100)
            self.distance_sensor.lights.off()
            wait(100)

        self.arm_movement_motor.run_angle(
            speed=1000,
            rotation_angle=-850,
            then=Stop.HOLD,
            wait=True)

    def turn_left(self, angle=90):
        """ 
        Turn Blast left with given angle.
        @param angle: Degrees
        """
        self.drive_base.turn(-angle)

    def turn_right(self, angle=90):
        """ 
        Turn right with given angle.
        @param angle: Degrees
        """
        self.drive_base.turn(angle)

    def move_forward(self, distance=100):
        """
        Move straight with given distance. 
        @param distance: mm
        """
        self.drive_base.straight(abs(distance))

    def move_backward(self, distance=100):
        """
        Move straight backwards with given distance.
        @param distance: mm
        """
        self.drive_base.straight(-abs(distance))

