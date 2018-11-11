"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Garrett Sanders.
"""

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, discuss the "big picture" of laptop-robot
# TODO:    communication:
# TODO:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# TODO:        user presses a button intended to make something happen on the
# TODO:        ROBOT, the LAPTOP program sends a message to its MQTT client
# TODO:        indicating what it wants the ROBOT to do, and the MQTT client
# TODO:        SENDS that message TO a program running on the ROBOT.
# TODO:
# TODO:      - Another program runs on the ROBOT. It stays in a loop, responding
# TODO:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# TODO:        It also, in the background, listens for messages TO the ROBOT
# TODO:        FROM the program running on the LAPTOP.  When it hears such a
# TODO:        message, it calls the method in the DELAGATE object's class
# TODO:        that the message indicates, sending arguments per the message.
# TODO:
# TODO:  Once you understand the "big picture", delete this TODO (if you wish).
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 99
# TODO:    to use YOUR robot's number instead of 99.
# TODO:    Commit and push the change, then other team members Update Project.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 4. Run this module.
# TODO:    Study its code until you understand how the GUI is set up.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)

    root.mainloop()
    # --------------------------------------------------------------------------
    # TODO: 5. Add code above that constructs a   com.MqttClient   that will
    # TODO:    be used to send commands to the robot.  Connect it to this EV3.
    # TODO:    Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    degree_entry_box = ttk.Entry(frame)
    distance_entry_box = ttk.Entry(frame)

    speed_label = ttk.Label(frame, text="Speed")
    degree_label = ttk.Label(frame, text="Degree")
    distance_label = ttk.Label(frame, text="Distance")

    go_forward_button = ttk.Button(frame, text="Go Forward")
    go_backward_button = ttk.Button(frame, text="Go Backward")
    turn_left_button = ttk.Button(frame, text="Turn Left")
    turn_right_button = ttk.Button(frame, text="Turn Right")
    quit_button = ttk.Button(frame, text="QUIT")

    speed_label.grid()
    speed_entry_box.grid()
    degree_label.grid()
    degree_entry_box.grid()
    distance_label.grid()
    distance_entry_box.grid()

    go_forward_button.grid()
    go_backward_button.grid()
    turn_left_button.grid()
    turn_right_button.grid()
    quit_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, distance_entry_box, mqtt_client)
    go_backward_button['command'] = \
        lambda: handle_go_backward(speed_entry_box, distance_entry_box, mqtt_client)


def handle_go_forward(entry_box_1, entry_box_2, mqtt_client):
    """
    Tells the robot to go forward at the speed and distance specified in the given entry box.
    """
    speed_string = entry_box_1.get()
    distance_string = entry_box_2.get()
    mqtt_client.send_message('go_forward', [speed_string, distance_string])


def handle_go_backward(entry_box_1, entry_box_2, mqtt_client):
    """
    Tells the robot to go backward at the speed and distance specified in the given entry box.
    """
    speed_string = entry_box_1.get()
    distance_string = entry_box_2.get()
    mqtt_client.send_message('go_backward', [speed_string, distance_string])


main()
