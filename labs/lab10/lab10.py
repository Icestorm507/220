"""
Name: Dylan Embrey
lab10.py
Problem: This will take a class as input and then result in a door and button being made.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from door import Door
from button import Button
from graphics import *


def main():
    win_width = 700
    win_height = 800
    win = GraphWin("Test", win_width, win_height)
    win.setBackground('white')
    door_outline = Rectangle(Point(250, 275), Point(420, 760))
    door_closed = Door(door_outline, "Closed")
    door_open = Door(door_outline, "Open")
    door_closed.color_door('red')
    door_closed.draw(win)
    button_outline = Rectangle(Point(250, 75), Point(420, 160))
    bar = Button(button_outline, "Exit")
    bar.draw(win)
    win.getMouse()
    if bar.is_clicked(button_outline):
        win.close()
    if door_closed.is_clicked(door_outline):
        door_open.draw(win)
    else:
        door_closed.draw(win)


main()
