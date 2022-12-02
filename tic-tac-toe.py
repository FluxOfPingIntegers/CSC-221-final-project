#!/usr/bin/env python3

from Board import Board

board = Board()
welcome_message = '---Welcome To Tic Tac Toe---'
print(welcome_message)

while board.game:
    board.disp_board()
    user_input = input("Please enter numbered space for X token (enter 'q' for quit): ")

    if user_input in board.selections:
        board.apply_token(user_input)
        board.comp_move(board.selections)
        if board.game == False:
            new_game_input = input("Would you like to play another game?  (enter 'y' for yes): ")
            board.game = (new_game_input == 'y')
            if board.game:
                print(welcome_message)
            else:
                print("Thanks for playing!")
            board.clear_board()

    elif user_input == 'q':
        board.game = False
        print("Thanks for playing!")
    else:
        print('Invalid entry!')
