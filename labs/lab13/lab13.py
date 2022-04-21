"""
Dylan Benton Embrey
4/20/2022
Lab 13.py
Computer Programming Labs 13: Sorting
Problem: This code will help with sorting lists and finding the areas of shapes.
This is my work.
"""


def trade_alert(filename):
    file = open(filename, 'r')
    line = file.readline()
    line = line.split(' ')
    line = map(int, line)
    second = 0
    for i in line:
        second += 1
        if i > 830:
            print("Warning, the trades have gone above 830 in the past", second, 'seconds')
        elif i == 500:
            print('Please pay attention as the stocks have gone above 500 at least', second, 'times!')
    file.close()
