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
    robot.color_sensor.get_color()
    while True:
        robot.drive_system.start_moving(100, 100)
        if robot.color_sensor.get_color() == 6:
            robot.drive_system.turn_degrees(1, 100)

main()
