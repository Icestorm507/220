"""
Name: Dylan Embrey
lab12.algorithms.py
Problem: This will take different functions and complete different objectives for each of them.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    file = open(filename, 'r')
    line = file.readline()
    list_of_nums = []
    while line:
        nums_string = line.split(' ')
        i = 0
        while i < len(nums_string):
            eval(nums_string[i])  # make the current element a number
            i += 1
            list_of_nums.append()
        # nums_string.replace(' ', ', ')
        line = file.readline()


def is_in_linear(search_value, values):
    i = 0
    while i < len(values):
        if values[i] == search_value:
            return True
        i += 1
    else:
        return False


def selection_sort(values):
    for i in range(len(values) - 1):
        min_index = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]


def calculate_area(rect): # use abs() for values
    for i in rect:
        x * y = area j





def rect_sort(rectangles):
    for i in range(len(rectangles)):
        min_index = i
        for j in range(i + 1, len(rectangles)):
            if rectangles[min_index] > rectangles[j]:
                min_index = j
        rectangles[i], rectangles[min_index] = rectangles[min_index], rectangles[i]
