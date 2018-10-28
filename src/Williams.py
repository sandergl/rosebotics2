"""
  Capstone Project.  Code written by Elijah Williams.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    follow_line()

def follow_line():
    robot = rb.Snatch3rRobot()
    robot.color_sensor.get_reflected_intensity()
    while True:
        robot.drive_system.start_moving(50, 50)
        if robot.color_sensor.get_reflected_intensity() >5:
            robot.drive_system.turn_degrees(10, 50)


main()
