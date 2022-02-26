"""
Dylan Benton Embrey
2/25/2022
Homework6.py
6-Strings
Problem: This code will help show the convered number of dollars, sphere area or volume, and a simple cipher code.
This is my work.
"""
import math


def cash_converter():
    dollars = eval(input("enter an integer: "))
    sentence = "That is ${:.2f}".format(float(dollars))
    print(sentence)


def encode(message: str, key: int):
    message = input('Enter a message: ')
    key = int('Enter a key: ')
    encoded = encode(message, key)
    print(encoded)
    return ''.join(chr(ord(i) + 65) for i in message)


def sphere_area():
    radius = float(input("Enter the radius of a sphere: "))
    surface_area = 4 * math.pi * pow(radius, 2)
    print("surface area of the sphere wll be %.2f" % surface_area)


def sphere_volume():
    radius = float(input("Enter the radius of a sphere: "))
    volume = (4 / 3) * math.pi * pow(radius, 3)
    print("volume of the sphere will be %.2f" % volume)


def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_n_cubes(n):
    total = 0
    for i in range(1, n + 1):
        total += (i * i * i)
    return total


def encode_better():
    message = input("enter a message: ")
    key = input("enter a key: ")
    coded = []
    result = []
    for c in range(len(message)):
        coded.append(((ord(message[c]) - 65) + (ord(key[c % len(key)]) - 65)) % 26)
    for c in coded:
        result.append(chr(int(c) + 65))
    print(coded)
    return ''.join(result)
