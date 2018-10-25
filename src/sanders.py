"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time
# 9.6in,831  9.6in,826 9.6in,823
# 86.39 degrees per inch in one sec


def main():
    """ Runs YOUR specific part of the project """
    # movement_experiment()
    degree_experiment()


def movement_experiment():
    robot = rb.Snatch3rRobot()

    robot.drive_system.start_moving(100, 100)
    time.sleep(1)
    robot.drive_system.stop_moving()
    print(robot.drive_system.left_wheel.get_degrees_spun())


def degree_experiment():
    robot = rb.Snatch3rRobot()

    robot.drive_system.start_moving(-50, 50)
    time.sleep(1.75)
    robot.drive_system.stop_moving()
    print(robot.drive_system.left_wheel.get_degrees_spun())
# 475, 90degrees,452, 90degrees, 465, 90degrees
# 5.18 degrees spun per degree


main()
