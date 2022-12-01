import random

class Board:
    def __init__(self):
        self.board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        self.selections = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def disp_board(self):
        b = self.board
        spaces = (f"{b[1]}|{b[2]}|{b[3]}\n-----\n{b[4]}|{b[5]}|{b[6]}\n-----\n{b[7]}|{b[8]}|{b[9]}")
        print(spaces)

    def clear_board(self):
        self.board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    def apply_token(self, selection, player = 'Human'):
        if (player == 'Human'):
            self.board[selection] = 'X'
        else:
            self.board[selection] = 'O'

    def comp_move(self, selections):
        selection = random.choice(selections)
        self.apply_token(selection, 'CPU')
        return selection
        
