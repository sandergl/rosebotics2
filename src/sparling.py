"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import ev3dev.ev3 as ev3
import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # color = rb.Color.GREEN.value
    # move_to_color(color)
    infared_sensor()

    # WHITE/RED does not work same with the BLUE/GREEN going down


def move_to_color(color):
    s8n = rb.Snatch3rRobot()
    s8n.drive_system.start_moving(50, 50)
    s8n.color_sensor.wait_until_color_is(color)
    s8n.drive_system.stop_moving()


def infared_sensor():
    robot = rb.Snatch3rRobot()
    button = robot.touch_sensor
    while True:
        distance = robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
        if distance < 15:
            ev3.Sound.beep().wait()
            time.sleep(1)
        if button.is_pressed() == 1:
            break


main()
