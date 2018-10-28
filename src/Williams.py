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
    white = rb.Color.WHITE
    while True:
        s8n.drive_system.start_moving(20, 20)
        if s8n.color_sensor.get_color() == white:
            s8n.drive_system.stop_moving()
            s8n.drive_system.spin_in_place_degrees(90, 50)

main()
