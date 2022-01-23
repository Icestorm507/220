"""
Name: Dylan Benton Embrey
Homework 1.py
Problem: This assignment is to understand the editing and programming phases of python to make a series of values go
through mathematical expressions to find an answer.
Certification of Authenticity:
This assignment is my work.
"""


def rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


rec_area()


def rec_volume():
    height = eval(input("What is the height: "))
    length = eval(input("What is the length: "))
    width = eval(input("What is the width: "))
    volume = (length * width * height)
    print("The volume is: ", volume)


rec_volume()


def shooting():
    shooting_total = eval(input("Enter the players total shots: "))
    shooting_made = eval(input("Enter the number of shots made: "))
    shooting_percent = (shooting_made/shooting_total)
    print("The Shooting Percent: %", shooting_percent * 100)


shooting()


def coffee():

    coffee_pounds = eval(input("How many pounds of coffee would you like? "))
    cost = ((10.50 + .86) * coffee_pounds) + 1.50
    print("The total total cost of your order is", cost)


coffee()


def kilometers_to_miles():
    kilometer = eval(input("How many kilometers did you travel? "))
    convert = 0.62
    miles = kilometer * convert
    print("That's", miles, "miles!")


kilometers_to_miles()
