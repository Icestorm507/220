"""
Name: Dylan Embrey
Lab-8.py
Problem: This will work with multiple functions to bring them together for one code process.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import *
import math
from time import sleep


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball, ball2):
    center1 = ball.getCenter()
    center2 = ball2.getCenter()
    radius1 = ball.getRadius()
    radius2 = ball2.getRadius()
    x1 = center1.getX()
    x2 = center2.getX()
    y1 = center1.getY()
    y2 = center2.getY()
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    sum_radius = radius2 + radius1
    if distance >= sum_radius:
        return False
    else:
        return True


def hit_vertical(circle_ball, graphwin):
    dx = 0.01
    circle_ball.move(dx)
    center1 = circle_ball.getCenter()
    x1 = center1.getX()
    x_true = x1 + dx
    ball_height = circle_ball.getRadius + center1
    y = 0
    if ball_height >= graphwin.height(700) or ball_height <= y:
        return x_true * -1
    else:
        return False


def hit_horizontal(circle_ball, graphwin):
    dy = 0.01
    circle_ball.move(dy)
    center1 = circle_ball.getCenter()
    y1 = center1.getY()
    y_true = y1 + dy
    x = 0
    ball_width = circle_ball.getRadius + center1
    if ball_width >= graphwin.width(700) or ball_width <= x:
        return y_true * -1
    else:
        return False


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = (red, green, blue)
    return color


def bumper():
    while get_random(randint(-10, 700)):
        time.sleep(0.025)
        get_random_color()
        hit_horizontal() and hit_vertical()
        did_collide()


bumper()
