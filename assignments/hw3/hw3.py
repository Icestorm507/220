"""
Name: Dylan Embrey
Loops.py
Problem: This program is designed to do multiple things. It will calculate a grade average, the number pi, the amount
of donations in a tip jar, and  a square root.
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my work.
"""


def average():
    grades_amount = eval(input("How many grades will you enter? "))
    total_grades = 0
    for i in range(grades_amount):
        print("Enter grade:", i + 1)
        grade_number = eval(input(""))
        total_grades = (grade_number + total_grades)
    grade_average = (total_grades / grades_amount)
    print("The average of your grades is:", grade_average)


def tip_jar():
    tip_question = eval(input("How many donations are there? "))
    for n in range(tip_question):
        tip_amount = int(input("How much would you like to donate? "))
        tip_total = tip_amount + n
    print("Total Tips:", tip_total)


def newton():
    number = int(eval(input("What number do you want to square root?", )))
    formula_1 = 0.5 * number
    for n in range(formula_1):
        eval(input("How many times should we improve the approx?", ))
        better_approx = 0.5 * (formula_1 + number)
        print("The square root is approximately:", better_approx)


def sequence():
    seq = range("")
    for i in range(seq):
        eval(input("How many terms would you like? "))
    print(seq)


def pi():
    f = 1000
    pie = 1.0
    for i in range(1, f):
        numer = i * 2 + 1
        denom = i * 2 - 1
        pie_2 = (pie * (numer * numer) / (denom * (denom + 2)) * 2)
        q = eval(input("How many terms in the series? "))
        print(q * pie_2)
