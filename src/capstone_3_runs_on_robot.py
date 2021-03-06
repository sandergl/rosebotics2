"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Elijah Williams.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this ****.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, review the "big picture" of laptop-robot
# TODO:    communication, per the comment in mqtt_sender.py.
# TODO:    Once you understand the "big picture", delete this TODO.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3



def main():
    # --------------------------------------------------------------------------
    # TODO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    s8n = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(s8n)
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
        leader = s8n.camera.get_biggest_blob()
        if leader.is_against_left_edge():
            mqtt_client.send_message('display_leader_location')

        time.sleep(0.01)  # For the delegate to do its work





class RemoteControlEtc(object):
    def __init__(self, s8n):
        """
        Stores the robot.
            :type   robot:    rb.Snatch3rRobot
        :param s8n:
        """
        self.robot = s8n
        pass
    def go_forward(self, speed_string):
        print("Here comes the nudes!", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

    def follow_the_leader(self):

        self.robot.camera.get_biggest_blob()
        while True:
            leader = self.robot.camera.get_biggest_blob()
            area = leader.get_area()
            if area > 0:
                self.robot.drive_system.start_moving(100, 100)

                if leader.is_against_left_edge():
                    self.robot.drive_system.turn_degrees(-15, 100)

                if leader.is_against_right_edge():
                    print("I'm against the right edge")
                    self.robot.drive_system.turn_degrees(15, 100)

                if self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() <= .01:
                    self.robot.drive_system.stop_moving()
                    self.robot.arm.raise_arm_and_close_claw()
                    time.sleep(.5)
                    ev3.Sound.speak('Woof! Woof! I caught you!')
                    print("Woof! Woof! I caught you!")
                    break
                self.robot.drive_system.start_moving(50, 50)


main()