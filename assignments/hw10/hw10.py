"""
Name: Dylan Embrey
hw10.py
Problem: This will take a class and do specific functions with whatever class is called.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def fibonacci(number):
    zero_value = 0
    first_number = 1
    if number == 1:
        return first_number
    else:
        index = 1
        while index != number:
            sequence = zero_value + first_number
            zero_value = first_number
            first_number = sequence
            index += 1
        return first_number


def double_investment(principle: float, rate: float):
    starting_invest = principle
    time = 0
    investment_2 = 2 * principle
    while starting_invest <= investment_2:
        starting_invest += (starting_invest * rate)
        time += 1
    return time


def syracuse(num):
    # != is not equal
    # list creation needs list literal note
    temp = [num]
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = (3 * num) + 1
        temp.append(int(num))
    return temp


if __name__ == '__main__':
    pass
