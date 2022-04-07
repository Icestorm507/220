"""
Name: Dylan Embrey
lab10.py
Problem: This will take a class as input and then result in a door and button being made.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from door import Door
from button import Button
from graphics import *
from random import randint


def main():
    win_width = 700
    win_height = 800
    win = GraphWin("Test", win_width, win_height)
    win.setBackground('white')
    guess_text = Text(Point(310, 700), 'Click to guess which is the secret door!')
    guess_text.draw(win)
    door_outline_1 = Rectangle(Point(50, 275), Point(220, 660))
    door_outline_2 = Rectangle(Point(250, 275), Point(420, 660))
    door_outline_3 = Rectangle(Point(450, 275), Point(620, 660))
    door_closed_1 = Door(door_outline_1, "Door 1")
    door_closed_2 = Door(door_outline_2, "Door 2")
    door_closed_3 = Door(door_outline_3, "Door 3")
    door_closed_1.color_door('brown')
    door_closed_2.color_door('brown')
    door_closed_3.color_door('brown')
    door_list = randint(1, 3)
    if door_list == 1:
        door_closed_1.set_secret(True)
    elif door_list == 2:
        door_closed_2.set_secret(True)
    elif door_list == 3:
        door_closed_3.set_secret(True)
    door_closed_1.draw(win)
    door_closed_2.draw(win)
    door_closed_3.draw(win)
    game_text = Text(Point(310, 100), 'I have a secret door:')
    game_text.draw(win)
    button_outline = Rectangle(Point(455, 75), Point(550, 160))
    button_button = Button(button_outline, "Quit")
    button_button.draw(win)
    win_outline = Rectangle(Point(50, 75), Point(120, 160))
    win_outline.draw(win)
    win_count = 0
    win_button = Text(win_outline.getCenter(), win_count)
    win_button_text = Text(Point(85, 70), 'Wins')
    win_button_text.draw(win)
    win_button.draw(win)
    loss_outline = Rectangle(Point(120, 75), Point(190, 160))
    loss_outline.draw(win)
    loss_count = 0
    loss_button = Text(loss_outline.getCenter(), loss_count)
    loss_button_text = Text(Point(155, 70), 'Losses')
    loss_button_text.draw(win)
    loss_button.draw(win)
    click = win.getMouse()
    while not button_button.is_clicked(click):
        click = win.getMouse()
        if door_closed_1.is_clicked(click):
            if door_closed_1.is_secret():
                door_closed_1.color_door('green')
                win_count += 1
                win_button.setText(win_count)
                game_text.setText('You Win!')
                guess_text.setText('Click anywhere to play again.')
            else:
                door_closed_1.color_door('red')
                loss_count += 1
                loss_button.setText(loss_count)
                game_text.setText('You Lose!')
                guess_text.setText('Click anywhere to play again.')
                if door_closed_2.is_secret():
                    door_closed_2.color_door('green')
                else:
                    door_closed_3.color_door('green')
        elif door_closed_2.is_clicked(click):
            if door_closed_2.is_secret():
                door_closed_2.color_door('green')
                win_count += 1
                win_button.setText(win_count)
                game_text.setText('You Win!')
                guess_text.setText('Click anywhere to play again.')
            else:
                door_closed_2.color_door('red')
                loss_count += 1
                loss_button.setText(loss_count)
                game_text.setText('You Lose!')
                guess_text.setText('Click anywhere to play again.')
                if door_closed_1.is_secret():
                    door_closed_1.color_door('green')
                else:
                    door_closed_3.color_door('green')
        elif door_closed_3.is_clicked(click):
            if door_closed_3.is_secret():
                door_closed_3.color_door('green')
                win_count += 1
                win_button.setText(win_count)
                game_text.setText('You Win!')
                guess_text.setText('Click anywhere to play again.')
            else:
                door_closed_3.color_door('red')
                loss_count += 1
                loss_button.setText(loss_count)
                game_text.setText('You Lose!')
                guess_text.setText('Click anywhere to play again.')
                if door_closed_1.is_secret():
                    door_closed_1.color_door('green')
                else:
                    door_closed_2.color_door('green')
            win.getMouse()

    win.close()





if __name__ == '__main__':
    main()
