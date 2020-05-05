import random

from termcolor import cprint

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
player = 'X'

def give_instructions():
    

def play_game():
    global board, player

    while True:
        game_board()
        turn()

        is_over, winner = game_over()

        if is_over:
            game_board()
            cprint(f"{winner} has won!", "green", "on_cyan")
            break

    if input("Do you want to play again? Yes/No ").lower() == "yes":
        board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        player = 'X'

        play_game()

        

def game_board():
    global board
    print()

    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

    print()

def turn():
    global player

    cprint(f"{player}'s turn", "cyan", "on_grey")
    if player == 'X':
        while True:
            try:
                position = int(input("Pick a number from 1-9: ")) - 1
            except ValueError:
                print()
                cprint("Pick valid numbers", "white", "on_red")
                print()
                continue

            if position + 1 > len(board):
                print()
                cprint("Don't pick numbers greater than 9", "white", "on_red")
                print()
                continue

            if position < 0:
                print()
                cprint("Don't pick 0 or negative numbers", "white", "on_red")
                print()
                continue

            if board[position] != "-":
                print()
                cprint(f"position {position + 1} is already taken", "white", "on_yellow")
                print()
                continue
                

            board[position] = player
            break
            

        player = 'O'

    else:
        while True:
            position = random.choice(range(9))

            if board[position] == "-":
                board[position] = player
                break

        player = 'X'

    is_over, winner = game_over()


def game_over():
    lines = [
        board[:3], board[3:6], board[6:9],
        board[::3], board[1::3], board[2::3],
        board[::4], board[2:7:2]
    ]

    for line in lines:
        if ("-" in line) or ("X" in line and "O" in line):
            continue
        return (True, line[0])

    return (False, None)


play_game()

# THE OOP WAY! ⬇ (Not Complete), You can try to make it if I didn't

# from Board import Board

# board = Board()
# board.render()
