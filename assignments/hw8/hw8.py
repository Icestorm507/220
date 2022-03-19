"""
Name: Dylan Embrey
Homework-8.py
Problem: This will work with lists and variables to reset them in a way to make a new form of the list.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import GraphWin, Circle, Point, Text


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    total = 0
    for i in nums:
        total += i
    return total


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    lists = []
    for i in range(len(nums)):
        nums.append(nums[i])
        for i in range(len(nums)):
            lists_other = 0
            variable = nums[i]
            variable = variable.replace(",", "").split()
            for i in range(len(variable)):
                variable[i] = float(variable[i])
                lists_other = lists_other + variable[i] ** 2
        lists.append(lists_other)
    return lists


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    elif weight >= 200 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    return leap

    year = int(raw_input())
    print(leap_year(year))


def did_overlap(circle_one, circle_two):
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circum_point = win.getMouse()
    radius = math.sqrt(
        (center.getY() - circum_point.getY()) ** 2 + (center.getX() - circum_point.getX()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("yellow")
    circle_one.draw(win)
    center_2 = win.getMouse()
    circum_point_2 = win.getMouse()
    radius_2 = math.sqrt(
        (center_2.getY() - circum_point_2.getY()) ** 2 + (center_2.getX() - circum_point_2.getX()) ** 2)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill("red")
    circle_two.draw(win)
    ending_text = Text(Point(5, 5), "")
    closing_text = Text(Point(5, 7), "Click again to close:")
    circle_distance = math.sqrt((center_2.getY() - center.getY()) ** 2 + (center_2.getX() - center.getX() ** 2))
    if circle_distance < radius + radius_2:
        ending_text.setText("The circles overlap.")
        ending_text.draw(win)
        closing_text.draw(win)
        win.getMouse()
        win.close()
        return True
    else:
        ending_text.setText("The circles did not overlap.")
        ending_text.draw(win)
        closing_text.draw(win)
        win.getMouse()
        win.close()
        return False


if __name__ == '__main__':
    pass
