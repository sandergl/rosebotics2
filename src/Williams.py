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
    #data, samplerate = sf.read('youtube_8660.wav')
    #sf.write('new_file.ogg', data, samplerate)
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
    s8n = rb2.Snatch3rRobot()
    camera = rb2.Camera()
    #camera.set_signature(sig_name)
    camera.get_biggest_blob()
    while True:
        object = camera.get_biggest_blob()
        if object.is_against_right_edge():
                ev3.Sound.beep().wait()
                time.sleep(.5)

        if s8n.touch_sensor.is_pressed() == 1:
            break
def test_touch_sensor():
    s8n = rb2.Snatch3rRobot()
    s8n.drive_system.start_moving(100, 100)
    if s8n.touch_sensor.is_pressed():
        s8n.drive_system.stop_moving()

main()
