"""
Name: Dylan Embrey
Homework-4.py
Problem: This program is designed to do multiple things. It will calculate a approximation difference in pi and allow
multiple shapes to be shown from user input such as circles or squares.
Certification of Authenticity:
I certify that this assignment is entirely my work.
"""
from graphics import *


def squares():
    win = GraphWin('Clicks', 700, 700)
    win.setBackground('white')
    first_text = Text(Point(350, 350), "Click to create a square")
    first_text.draw(win)
    shape_1 = Rectangle(Point(200, 200), Point(250, 250))
    shape_1.setOutline("red")
    shape_1.setFill("red")
    shape_1.draw(win)
    for k in range(5):
        p = win.getMouse()
        c = shape_1.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape_1 = (dx, dy)
    win.getMouse()
    first_text.setText("Click to close")
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Draw a Rectangle", 700, 700)
    win.setBackground('white')
    message = Text(Point(350, 350), "Click on two points")
    message.draw(win)

    p1 = win.getMouse()
    p4 = win.getMouse()
    p2 = Point(p4.getX(), p1.getY())
    p3 = Point(p1.getX(), p4.getY())
    p1.draw(win)
    p2.draw(win)
    p3.draw(win)
    p4.draw(win)
    line_1 = Line(p1, p2)
    line_1.draw(win)
    line_2 = Line(p2, p4)
    line_2.draw(win)
    line_3 = Line(p3, p4)
    line_3.draw(win)
    line_4 = Line(p3, p1)
    line_4.draw(win)
    rectangle_1 = Polygon(p1, p2, p3, p4)
    rectangle_1.draw(win)
    rec_area = line_1 * line_3
    print((message.setText("Area ="), rec_area), Point(350, 350))
    win.getMouse()
    message.setText("Click anywhere to quit.")
    win.getMouse()


def circle():
    w = 350
    h = 250
    from math import sqrt
    win = GraphWin("Click to create circle", w, h)
    win.setBackground('white')
    shape = Circle(Point(100, 100), 20)
    shape_center = win.getMouse()
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    shape_circumference = win.getMouse()
    dx = shape_circumference.getX() - shape_center.getX()
    dy = shape_circumference.getY() - shape_center.getY()
    radius = sqrt(dx * dx + dy * dy)
    print(("Radius=", radius), Point(40, 40))
    win.getMouse()
    print("Click to close", Point(40, 40))


def leibniz(n):
    t_sum = 0
    for i in range(n):
        term = (-1) ** i / (2 * i + 1)
        t_sum = t_sum + term
    return t_sum * 4


x = 3.1415926535897932
terms = int(input("Enter number of terms: "))
pi = leibniz(terms)
pie_final = float(x - pi)
print("pi approximation= ", pi)
print("accuracy:", abs(pie_final))
