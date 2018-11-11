"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Garrett Sanders.
"""


import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    receiver = Received(['No Color', 'Black', 'Blue', 'Green', 'Yellow', 'Red', 'White', 'Brown'])
    mqtt_client = com.MqttClient(receiver)
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)

    root.mainloop()


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
    spin_button = ttk.Button(frame, text="Spin")
    get_color_button = ttk.Button(frame, text="Get Color")
    quit_button = ttk.Button(frame, text="QUIT")

    speed_label.grid()
    speed_entry_box.grid()
    degree_label.grid()
    degree_entry_box.grid()
    distance_label.grid()
    distance_entry_box.grid()

    go_forward_button.grid()
    go_backward_button.grid()
    spin_button.grid()
    get_color_button.grid()
    quit_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, distance_entry_box, mqtt_client)
    go_backward_button['command'] = \
        lambda: handle_go_backward(speed_entry_box, distance_entry_box, mqtt_client)
    spin_button['command'] = \
        lambda: handle_spin(degree_entry_box, mqtt_client)
    quit_button['command'] = \
        lambda: handle_quit_running(root_window, mqtt_client)


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


def handle_spin(entry_box, mqtt_client):
    """
    Tells the robot to spin degrees.
    """
    degree_string = entry_box.get()
    mqtt_client.send_message('spin_degrees', [degree_string])


def handle_quit_running(root, mqtt_client):
    """
    Quits out of the tkinter and tells robot to stop.
    """
    mqtt_client.send_message('quit_running')
    root.destroy()


def get_color(mqtt_client):
    """Tells the robot to retrieve the current color that is below it."""
    mqtt_client.send_message('get_color')


class Received(object):
    def __init__(self, colors):
        self.colors = colors

    def display_color(self, value):
        color = self.colors[value]
        print(color)


main()
