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
    # --------------------------------------------------------------------------
    # TODO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------
    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed() is True:
            ev3.Sound.beep().wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
            ev3.Sound.speak("Hello. How are you?")
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
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
                    self.robot.drive_system.stop_moving()
                    time.sleep(3)
                    self.robot.drive_system.stop_moving(speed, speed)
                if color == 6:
                    print('white')
                if color == 7:
                    print('brown')
            color_1 = self.robot.color_sensor.get_color()


main()