#!/usr/bin/env python3

from Board import Board

board = Board()
game = True
board.disp_board()

while game:
    user_input = input("Please enter numbered space for X token (enter 'q' for quit): ")

    if user_input in board.selections:
        print(f'player selects space {user_input}')
        board.selections.remove(user_input)
        board.apply_token(user_input)
        comp_move = board.comp_move(board.selections)
        board.selections.remove(comp_move)
        print(f'computer selects space {comp_move}')
        board.disp_board()
    elif user_input == 'q':
        game = False
    else:
        print('Invalid entry!')
