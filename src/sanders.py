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
    movement_experiment()


def movement_experiment():
    robot = rb.Snatch3rRobot()

    robot.drive_system.start_moving(100, 100)
    time.sleep(1)
    robot.drive_system.stop_moving()
    print(robot.drive_system.left_wheel.get_degrees_spun())


main()
