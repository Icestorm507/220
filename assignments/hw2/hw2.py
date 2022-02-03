"""
Name: Dylan Benton Embrey
Homework #2.py
Problem: This program will help solve questions regarding various math problems using different means such as
addition, multiplication, or division.
Certification of Authenticity:
I certify that this assignment is entirely my own work done on Jan 29th.
"""
import math


def sum_of_threes():
    n = eval(input("what is the upper bound: "))
    return sum(range(3, n + 1, 3))


print("The sum of threes is", sum_of_threes())


def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(str(x * y), end=" ")
            print()


multiplication_table(1, 10)


def triangle_area():
    a = eval(input("Enter side length a: "))
    b = eval(input("Enter side length b: "))
    c = eval(input("Enter side length c: "))

    s = (a + b + c) / 2

    area: float = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The area of a triangle is:", area)


triangle_area()

def sum_squares():
    lower = eval(input("Enter lower range: "))
    upper = eval(input("Enter upper range: "))
    n = (lower, upper)
    print("The sum of the squares is: ", sum_squares)

sum_squares()


def power():
        num = eval(input("The number: "))
        p = eval(input("The power: "))
        a = 1
        for n in range(p):
            a = a * num
            assert isinstance(a, object)
            print(num,"^",p,a)

power()

if __name__ == '__main__':
    pass
