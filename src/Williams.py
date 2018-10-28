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
    white = rb.Color.WHITE
    while True:
        robot.drive_system.start_moving(50, 50)
        if robot.color_sensor.get_color() == white:
            robot.drive_system.stop_moving()
            robot.drive_system.spin_in_place_degrees(10, 50)

main()
