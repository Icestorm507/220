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
    pass


if __name__ == '__main__':
    pass
