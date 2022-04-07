"""
Name: Dylan Embrey
lab10.py
Problem: This will take a class as input and then result in a door and button being made.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def set_label(self, label):
        self.text.setText(label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        x1 = self.shape.getP1().getX()
        y1 = self.shape.getP1().getY()
        x2 = self.shape.getP2().getX()
        y2 = self.shape.getP2().getY()
        if x2 >= point >= x1 and y1 <= point <= y2:
            return True
        else:
            return False

    def color(self, color):
        self.shape.setFill(color)

