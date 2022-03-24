"""
Name: Dylan Embrey
lab9.py
Problem: This will work with making a tic-tac-toe board.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build_board():
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return list_of_numbers


def print_board(board):
    red = "\033[1;31m"
    blue = "\033[1;36m"
    light_gray = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = red + board[i] + light_gray
        elif str(board[i]).find('o') >= 0:
            new_board[i] = blue + board[i] + light_gray
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(light_gray)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    empty = board[position - 1]
    return str(empty).isnumeric()


def fill_spot(board, position, character):
    board[position].fill(character)
    character.strip()
    character.lower()


def winning_game(board):
    for i in range(0, 8, 3):
        if board[i] == board[i + 1] == board[i + 2]:
            return True
    for i in range(0, 2):
        if board[i] == board[i + 3] == board[i + 6]:
            return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    else:
        return False


def game_over(board):
    if winning_game(board):
        return True
    else:
        for i in range(1, 9):
            if is_legal(board, i):
                return False
        return True


def get_winner(board):
    if not game_over(board):
        return None
    acc_x = 0
    acc_o = 0
    for i in board:
        if i == 'x':
            acc_x = i + 1
        if i == 'o':
            acc_o = i + 1
    if acc_o == acc_x:
        return True
    if acc_x >= acc_o:
        return True


def play(board):
    instructions = """This is Tic-Tac-Toe, a game where you will be either x's or o's and will try to get 3 of 
    your letter in a row in any of the 9 boxes. If there are no more moves to make with neither letter having 3 in a 
    row then the game is over. X's will go first and enter in the number of where you want your symbol to go.
    """
    build_board()
    print_board(board)
    entry = eval(input("What position would you like your symbol to go to? "))
    if entry == is_legal(board, position=int):
        fill_spot(board, entry, character='x' or 'o')
    else:
        return entry
    question = input("Would you like to play another round? (y/n)")
    while question == 'y':
        build_board()
        play(board)
        while not game_over(board):
            return play(board)
        else:
            print("Goodbye")
    if not get_winner(board):
        print("tie!")
    else:
        game = "The " + str(get_winner(board)) + "'s have won!"
        print(instructions, game)
        exit(board)


def main():
    pass


if __name__ == '__main__':
    main()
