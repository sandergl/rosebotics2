"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Shamus Sparling.
"""
import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    color_1 = -1

    while True:
        if robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 1.5:
            robot.drive_system.stop_moving()
            ev3.Sound.speak("Object in path")
            break
        color = robot.color_sensor.get_color()
        if color != color_1:
            mqtt_client.send_message('display_color', [color])
        color_1 = robot.color_sensor.get_color()
        #if robot.beacon_button_sensor.is_top_red_button_pressed() is True:
         #   ev3.Sound.beep().wait()
        #if robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
         #   ev3.Sound.speak("Hello. How are you?")
        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Stores the robot
           :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forward(self, speed_string):
        print("Telling the robot to start moving at", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

        color_1 = -1
        while True:
            color = self.robot.color_sensor.get_color()
            if color != color_1:
                if color == 0:
                    print('no color')
                if color == 1:
                    print('black')
                if color == 2:
                    print('blue')
                    self.robot.drive_system.turn_degrees(90)
                if color == 3:
                    print('green')
                    self.robot.drive_system.turn_degrees(-90)
                if color == 4:
                    print('yellow')
                    self.robot.drive_system.turn_degrees(360)
                if color == 5:
                    print('red')
                    self.robot.drive_system.turn_degrees(180)
                if color == 6:
                    print('white')
                    self.robot.drive_system.stop_moving()
                    ev3.Sound.speak("Course Complete")
                    break
                if color == 7:
                    print('brown')
                self.robot.drive_system.start_moving(speed, speed)
            color_1 = self.robot.color_sensor.get_color()


main()