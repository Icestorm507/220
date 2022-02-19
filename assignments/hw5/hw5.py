"""
Name: Dylan Embrey
hw5.py
Problem: This program will show initials and even convert english to pig latin.
I certify that this assignment is entirely my own work..
"""


def name_reverse():
    name_call = input('enter a name (first last):')
    first_name = name_call.split()[0]
    last_name = name_call.split()[1] + ','
    print(last_name, first_name)


def company_name():
    domain = input('Enter a domain name:')
    website_name = domain.split('.')[1]
    new_string = ''
    for i in range(len(website_name)):
        new_string += website_name[i]
    print(new_string)


def initials():
    n = int(input("Total Number of Student: "))
    for i in range(n):
        first_name = input("Enter the first name of student: ")
        last_name = input("Enter the last name of student: ")
        print(f"The student's initials are {first_name[0] + last_name[0]}.")


def names():
    people_names = input("enter a list of names:")
    naming_list = people_names.split(', ')
    for i in naming_list:
        initial = i.split(" ")
        print(initial[0][0] + initial[1][0], end=" ")


def thirds():
    sentence = input("Please enter a sentence:")
    print("Original Sentence:", sentence)
    for i in range(0, len(sentence), 3):
        print(sentence[0:3])


def word_average():
    sentence = input('enter a sentence:')
    word = sentence.split()
    total = sum(map(len, word)) / len(word)
    print(total)


def pig_latin():
    sentence = input("Enter the sentence: ")
    words = sentence.split()
    new_sentence = ""
    for i in words:
        new_sentence += i[1:] + i[0] + "ay "
    new_sentence = new_sentence.lower()

    return new_sentence


print(pig_latin())


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
