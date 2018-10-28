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
    s8n = rb.Snatch3rRobot()
    s8n.color_sensor.get_color()
    while True:
        s8n.drive_system.start_moving(50, 50)
        if s8n.color_sensor.get_color() != 1:
            print('Nota res mala, optima.')
            s8n.drive_system.stop_moving()
            s8n.drive_system.turn_degrees(-20, 50)


main()
