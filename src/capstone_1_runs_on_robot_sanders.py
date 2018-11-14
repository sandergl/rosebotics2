"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Garrett Sanders.
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
        if robot.beacon_button_sensor.is_top_red_button_pressed() is True:
            ev3.Sound.beep().wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
            ev3.Sound.speak('Hello. How are you?')
        color = robot.color_sensor.get_color()
        if color != color_1:
            mqtt_client.send_message('display_color', [color])
        color_1 = robot.color_sensor.get_color()
        if robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 3:
            robot.drive_system.stop_moving()
            ev3.Sound.speak('Object in path').wait()
            break
        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Stores the robot.
          :type robot: rb.Snatch3rRobot
        """
        self.robot = robot
        self.mqtt_client = com.MqttClient

    def go_forward(self, speed_string, distance_string):
        """Makes the robot go forward at the given speed to reach the given distance."""
        speed = abs(int(speed_string))
        distance = int(distance_string)
        self.robot.drive_system.go_straight_inches(distance, speed)

    def go_backward(self, speed_string, distance_string):
        """Makes the robot go backward at the given speed to reach the given distance."""
        speed = -(abs(int(speed_string)))
        distance = int(distance_string)
        self.robot.drive_system.go_straight_inches(distance, speed)

    def spin_degrees(self, degree_string):
        """Makes the robot spin a certain number of degrees."""
        degree = int(degree_string)
        self.robot.drive_system.spin_in_place_degrees(degree)

    def quit_running(self):
        """Stops the robot."""
        self.robot.drive_system.stop_moving()
        exit()


main()
