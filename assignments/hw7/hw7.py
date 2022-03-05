"""
Name: Dylan Embrey
Homework-7.py
Problem: This program will display hourly wages, a print statment in word by word per each line,
and encode different messages.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode


def number_words(in_file_name, out_file_name):
    sentence = open(in_file_name, 'r')
    space = open(out_file_name, 'w')
    word = sentence.readlines()
    spacer = (word, '\n')
    for i in spacer:
        i = i + 1
        spaced = [i + " " + spacer]
        print(spaced, file=space)


def hourly_wages(in_file_name, out_file_name):
    wages = open(in_file_name, 'r')
    hourly_wage = open(out_file_name, 'w')
    for lines in wages:
        employee_data = lines.split()
        employee_name = employee_data[0] + ' ' + employee_data[1]
        employee_salary = (float(employee_data[2]) + 1.65) * int(employee_data[3])
        employee_salary = '{:.2f}'.format(employee_salary)
        new_info = employee_name + ' ' + str(employee_salary)
        print(new_info, file=hourly_wage)


def calc_check_sum(isbn):
    isbn_num = isbn.replace("-", "")
    done = 0
    digits = 10
    for i in isbn_num:
        i = int(i)
        done = done + i * digits
        digits = digits - 1
    return done


def send_message(file_name, friend_name):
    file_name = open(file_name, 'r')
    friend_name = open(friend_name + ".txt", "w")
    for i in file_name.readlines():
        print(i, file=friend_name, end='')


def send_safe_message(file_name, friend_name, key):
    file_name = open(file_name, 'r')
    friend_name = open(friend_name + ".txt", 'w')
    for i in file_name.readlines():
        encode_string = encode(i, key)
        print(encode_string, file=friend_name)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
