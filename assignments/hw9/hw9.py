"""
Name: Dylan Embrey
hw9.py
Problem: This will display and play a game of hangman.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def get_words(file_name):
    word = open(file_name, 'r')
    words_file = []
    for lines in word:
        words_file.append(lines)
    return words_file


def get_random_word(words):
    listing = len(words) - 1
    word_list = words[randint(0, listing)]
    return word_list.replace('\n', '')


def letter_in_secret_word(letter, secret_word):
    for i in letter:
        if i in secret_word:
            return True
        return False


def already_guessed(letter, guesses):
    count = 0
    for i in letter:
        if i in guesses:
            count /= 1 or count == len(letter)
            return True
        return False


def make_hidden_secret(secret_word, guesses):
    hangman_text = ""
    for i in secret_word:
        if i not in guesses:
            hangman_text = hangman_text + "_ "
            hangman_text = hangman_text + i + " "
    return hangman_text


def won(guessed):
    guessing = guessed.replace(' ', '')
    for i in guessing:
        if i == '_':
            return False
    return True


def play_command_line(secret_word):
    print("Welcome to the game, Hangman!")
    print("The word is" + str(len(secret_word)) + " letters long.")
    letters_guessed = ''
    guesses_left = 8
    print("------------")
    while True:
        print("You have " + str(guesses_left) + " guesses left.")
        print("Available letters: " + make_hidden_secret(secret_word, letters_guessed))
        print("Oh! That letter is not in my word: " + make_hidden_secret(secret_word, letters_guessed))
        guesses_left -= 1
        print("------------")
        if guesses_left <= 0:
            print("Sorry, no more guesses: " + secret_word + ".")
            break
        if letter_in_secret_word(secret_word, letters_guessed):
            print("WHOO! You've won!")


if __name__ == '__main__':
    pass
