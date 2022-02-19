"""
Dylan Benton Embrey
2/16/2022
Lab 5.py
Computer Programming Labs 5: Multiple Functions
Problem: This code will help show the average number of vehicles on the road per day, number of vehicles for all roads,
and the average number of vehicles per road.
This is my work.
"""
from graphics import *
from math import sqrt


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Triangle", win_width, win_height)
    win.setBackground('white')
    triangle.text = Text(Point(250, 50), "Click at three random points to create a triangle in the graphics window:")
    triangle.text.draw(win)
    point_1 = win.getMouse()
    point_2 = win.getMouse()
    point_3 = win.getMouse()
    triangle_d = Polygon(point_1, point_2, point_3)
    triangle_d.setFill("red")
    triangle_d.draw(win)
    dx1 = (point_2.getX() - point_1.getX())
    dx2 = (point_3.getX() - point_2.getX())
    dx3 = (point_1.getX() - point_3.getX())
    dy1 = (point_2.getY() - point_1.getY())
    dy2 = (point_3.getY() - point_2.getY())
    dy3 = (point_1.getY() - point_3.getY())
    length_1 = sqrt(dx1 ** 2 + dy1 ** 2)
    length_2 = sqrt(dx2 ** 2 + dy2 ** 2)
    length_3 = sqrt(dx3 ** 2 + dy3 ** 2)
    perimeter = length_1 + length_2 + length_3
    perimeter_text1 = Text(Point(250, 390), 'Perimeter is:' + str(perimeter))
    perimeter_text1.draw(win)
    s = (length_1 + length_2 + length_3) / 2
    area = (s*(s-length_1)*(s-length_2)*(s-length_3)) ** 0.5
    area_text = Text(Point(250, 420), 'Area is:' + str(area))
    area_text.draw(win)
    triangle.text = Text(Point(250, 490), 'Click to close:')
    triangle.text.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_entry = Entry(Point(245, 240), 20)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_entry = Entry(Point(245, 270), 20)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_entry = Entry(Point(245, 300), 20)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    red_text.draw(win)
    red_entry.draw(win)
    green_text.draw(win)
    green_entry.draw(win)
    blue_text.draw(win)
    blue_entry.draw(win)
    color_rgb(red_entry, green_entry, blue_entry)
    for i in color_rgb():
        shape.setFill(color_rgb(red_entry, green_entry, blue_entry))
        i = 5
        win.getMouse()
    win.getMouse()
    win.close()


def process_string():
    string1 = input("Input a statement: ")
    print("First Character:", string1[0][0])
    last_character = string1[-1]
    print("Last Character:", last_character)
    character_position = string1[2 - 5]
    print("Character Position:", character_position)
    first_last = string1[0] + string1[-1]
    print("First and Last characters:", first_last)
    first3_10 = (string1[0] + string1[1] + string1[2]) * 10
    print("The first 3 characters are:", first3_10)
    i = 0
    while i < len(string1):
        print(i, string1[i])
        i = i + 1
    character_number = len(string1)
    print("The number of letters is:", character_number)


process_string()

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x1 = values[1] + values[3]
    print(x1)
    x2 = values[0] + values[2]
    print(x2)
    x3 = values[1] * 5
    print(x3)
    x4 = [values[2], values[3], values[4]]
    print(x4)
    x5 = [values[2], values[3], values[0]]
    print(x5)
    x6 = [values[0], values[2], values[5]]
    print(x6)
    x7 = float(values[0]) + float(values[2]) + float(values[5])
    print(x7)
    x8 = len(values)
    print(x8)


def another_series():
    numbers = [2, 4, 6]
    n = (numbers[0] + numbers[1] + numbers[2]) * input('')
    print("Sum =", n)


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Target", win_width, win_height)
    win.setBackground('black')
    white_target = Circle(Point(250, 250), 250)
    white_target.setFill('white')
    white_target.draw(win)
    black_target = Circle(Point(250, 250), 200)
    black_target.setFill('black')
    black_target.draw(win)
    blue_target = Circle(Point(250, 250), 150)
    blue_target.setFill('blue')
    blue_target.draw(win)
    red_target = Circle(Point(250, 250), 100)
    red_target.setFill('red')
    red_target.draw(win)
    yellow_target = Circle(Point(250, 250), 50)
    yellow_target.setFill('yellow')
    yellow_target.draw(win)
    win.getMouse()
    win.close()
