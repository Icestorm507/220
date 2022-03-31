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


def Special_Door():
    win_width = 700
    win_height = 800
    win = GraphWin("Test", win_width, win_height)
    win.setBackground('white')
    door_outline = Rectangle(Point(250, 275), Point(420, 760))
    dar = Door(door_outline, "Closed")
    dor = Door(door_outline, "Open")
    dar.color_door('red')
    dar.draw(win)
    button_outline = Rectangle(Point(250, 75), Point(420, 160))
    bar = Button(button_outline, "Exit")
    bar.draw(win)
    win.getMouse()
    win.close()



Special_Door()
