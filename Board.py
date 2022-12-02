import random

class Board:
    def __init__(self):
        self.board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        self.selections = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.winning_sequences = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
        self.game = True

    def disp_board(self):
        b = self.board
        spaces = (f"{b[1]}|{b[2]}|{b[3]}\n-----\n{b[4]}|{b[5]}|{b[6]}\n-----\n{b[7]}|{b[8]}|{b[9]}")
        print(spaces)

    def clear_board(self):
        self.board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        self.selections = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def apply_token(self, selection, player = 'Human'):
        self.selections.remove(selection)
        selection = int(selection)
        if (player == 'Human'):
            self.board[selection] = 'X'
        else:
            self.board[selection] = 'O'
        print(f"{player} selects space {selection}")
        self.check_game_status(player, selection)

    def comp_move(self, selections):
        if (self.game):
           selection = random.choice(selections)
           self.apply_token(selection, 'Computer')
    
    def check_game_status(self, player, selection):
        b = self.board
        num = selection
        for sequence in self.winning_sequences:
            s1 = sequence[0]
            s2 = sequence[1]
            s3 = sequence[2]
            if ((num in sequence) and self.game and (b[s1] == b[s2] and b[s1] == b[s3])):
                self.game = False
                print(f"The {player} wins!")
                self.disp_board()
        if len(self.selections) == 0:
            self.game = False
            print("This game ends in a draw!")
            self.disp_board()

        