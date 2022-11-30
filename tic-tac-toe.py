#!/usr/bin/env python3

from Board import Board

board = Board()
game = True
selections = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

while game:
    board.disp_board()
    user_input = input("Please enter numbered space for X token (enter 'q' for quit): ")

    if user_input in selections:
        print(f'player selects space {user_input}')
        # need movement method for board
    elif user_input == 'q':
        game = False
    else:
        print('Invalid entry!')
