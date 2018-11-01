"""
  Capstone Project.  Code written by Garrett Sanders.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # movement_experiment()
    # degree_experiment()
    # test_go_inches()
    # test_spin_degree()
    # turn_degree_experiment()
    # test_turn_degrees()
    # test_polygon()
    test_calibrate()


def test_go_inches():
    robot = rb.Snatch3rRobot()

    robot.drive_system.go_straight_inches(10)


def movement_experiment():
    robot = rb.Snatch3rRobot()

    robot.drive_system.start_moving(100, 100)
    time.sleep(1)
    robot.drive_system.stop_moving()
    print(robot.drive_system.left_wheel.get_degrees_spun())
# 9.6in,831  9.6in,826 9.6in,823
# 86.39 degrees per inch in one sec


def test_spin_degree():
    robot = rb.Snatch3rRobot()

    for k in range(4):
        robot.drive_system.spin_in_place_degrees(90)
        time.sleep(.5)


def degree_experiment():
    robot = rb.Snatch3rRobot()

    robot.drive_system.start_moving(-50, 50)
    time.sleep(1.75)
    robot.drive_system.stop_moving()
    print(robot.drive_system.left_wheel.get_degrees_spun())
# 475, 90degrees,452, 90degrees, 465, 90degrees
# 5.18 degrees spun per degree


# def test_turn_degrees():


def turn_degree_experiment():
    robot = rb.Snatch3rRobot()

    robot.drive_system.start_moving(50, 0)
    time.sleep(3.555)
    robot.drive_system.stop_moving()
    print(robot.drive_system.left_wheel.get_degrees_spun())
# 989, 90 degrees    965, 90 degrees     974, 90 degrees
# 10.84 degrees spun per degree


def test_turn_degrees():
    robot = rb.Snatch3rRobot()

    robot.drive_system.turn_degrees(90)
    time.sleep(.5)
    robot.drive_system.turn_degrees(-90)


def polygon(n):
    s8n = rb.Snatch3rRobot()

    angle = 360 / n
    for k in range(n):
        s8n.drive_system.go_straight_inches(18)
        time.sleep(1)
        s8n.drive_system.spin_in_place_degrees(angle)
        time.sleep(1)


def test_polygon():
    polygon(4)


def test_raise_and_close():
    robot = rb.ArmAndClaw

    robot.raise_arm_and_close_claw(robot)


def test_calibrate():
    robot = rb.ArmAndClaw

    robot.calibrate()


def test_move_arm_to_position():
    robot = rb.ArmAndClaw

    robot.move_arm_to_position(360 * 7)


main()
