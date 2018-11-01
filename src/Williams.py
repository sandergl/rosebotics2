"""
  Capstone Project.  Code written by Elijah Williams.
  Fall term, 2018-2019.
"""

import time
import ev3dev.ev3 as ev3
import rosebotics_new as rb2

def main():
    """ Runs YOUR specific part of the project """
    #follow_line()

    beep_for_color()
def follow_line():
    s8n = rb2.Snatch3rRobot()
    s8n.color_sensor.get_color()
    while True:
        s8n.drive_system.start_moving(100, 100)
        if s8n.color_sensor.get_color() != 1:
            print('Nota res mala, optima.')
            s8n.drive_system.stop_moving()
            s8n.drive_system.turn_degrees(-15, 100)
def beep_for_color():
    camera = rb2.Camera()
    camera.set_signature()
    blank = camera.get_biggest_blob()
    if camera.get_biggest_blob() > blank:
        ev3.Sound.beep().wait()


main()
