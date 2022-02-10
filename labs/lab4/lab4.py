"""
Dylan Benton Embrey
2/9/2022
Computer Programming Labs 4: Greeting Card
I certify that this is my work.
"""
from graphics import Circle, Point, GraphWin, Text, Image


def greeting_card():
    win = GraphWin('Greeting Card!', 700, 700)
    win.setCoords(10, 10, 100, 100)
    greeting_card_text = Text(Point(50, 50), "Happy Valentine's Day!!!")
    greeting_card_text.draw(win)
    win.getMouse()


greeting_card()

