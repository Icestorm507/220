"""
Name: Dylan Embrey
lab12.py
Problem: This will take different functions and complete different objectives for each of them.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def find_and_remove_first(list, value):
    name = "Dylan Embrey"
    i = 0
    num_value = value
    while i < len(list):
        if list[i] == value:
            list.remove(num_value)
            list.insert(i, name)
            i = len(list)
        i += 1


def good_input():
    number = eval(input("enter a number between 1 and 10: "))
    while not 10 > number > 1:
        if 10 < number:
            return "This number is too high, please try again!"
        if 1 > number:
            return "This number is too low, please try again!"
        number = eval(input("Enter a number between 1 and 10: "))
    return number


def num_digits():
    value = int(input("enter a number and put in a negative number or 0 to end the counting"))
    while value > 0:
        digit = 0
        while value != 0:
            value = value // 10
            digit += 1
        print("Your number has", digit, "digits!")
        value = int(input("enter a number and put in a negative number or 0 to end the counting"))

def hi_lo_game():
    num = randint(1, 100)
    question = int(input("Guess the Number: "))
    i = 7
    while i > 0:
        if question == num:
            print("That is the correct number!", num, " You win in ", i + 1, " guesses!")
            i = 0
        elif question > num:
            print("too high")
        elif question < num:
            print("too low")
        i -= 1
        question = int(input("Guess the number: "))
    else:
        if question != num:
            print("Sorry,you lose.The number was ", num)
