"""
Dylan Benton Embrey
2/23/2022
Lab 6.py
Computer Programming Labs 6: Ciphers
Problem: This code will help show a button with text, as well as go through a vigenere ciphers through the program.
This is my work.
"""
from graphics import Text, Point, Rectangle, Entry, GraphWin


def vigenere():
    box_width = 500
    box_height = 400
    box = GraphWin("Vigenere", box_width, box_height)
    box.setBackground('white')
    coding_text = Text(Point(170, 100), "Message to code:")
    coding_entry = Entry(Point(340, 100), 30)
    key_text = Text(Point(170, 150), "Key:")
    key_entry = Entry(Point(340, 150), 30)
    click_text = Text(Point(260, 250), "Click to Encode")
    button_outline = Rectangle(Point(200, 240), Point(320, 260))
    result_text = Text(Point(50, 10), "")
    coding_text.draw(box)
    coding_entry.draw(box)
    key_text.draw(box)
    key_entry.draw(box)
    click_text.draw(box)
    button_outline.draw(box)
    result_text.draw(box)
    box.getMouse()
    coding = coding_entry.getText()
    key = key_entry.getText()
    coding = coding.upper()
    key = key.upper()
    key_length = len(key)
    key_int = [ord(i) for i in key]
    coding_int = [ord(i) for i in coding]
    encoded = ''
    coding.replace(" ", "")
    for c in range(len(coding_int)):
        encryption = (coding_int[c] + key_int[c % key_length]) % 26
        encoded += chr(encryption + 65)
    click_text.setText("Resulting Message:")
    button_outline.undraw()
    message4_text = Text(Point(260, 290), encoded)
    message4_text.draw(box)
    message3_text = Text(Point(260, 350), "Click anywhere to close")
    message3_text.draw(box)
    box.getMouse()
    return encoded
