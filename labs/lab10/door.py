"""
Name: Dylan Embrey
lab10.py
Problem: This will take a class as input and then result in a door and button being made.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


class Door:

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
        if point <= x2:
            return True
        elif point >= x1:
            return True
        elif point >= y2:
            return True
        elif point <= y1:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.shape.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.shape.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.is_secret():
            return True
        else:
            return False

    def set_secret(self, secret):
         if self.set_secret(self, secret) == secret:
            return True
         else:
            return False


