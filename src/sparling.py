"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    color = rb.Color.YELLOW.value
    move_to_color(color)

    # BLUE does not work on mine when heading down the board

def move_to_color(color):
    s8n = rb.Snatch3rRobot()
    s8n.drive_system.start_moving(50, 50)
    s8n.color_sensor.wait_until_color_is(color)
    s8n.drive_system.stop_moving()


main()
