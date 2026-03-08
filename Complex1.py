from random import randint


class Complex1:
    def __init__(self, round_num, opponent_move):
        self.round_num = round_num
        self.opponent_move = opponent_move

    def play(self):
        if randint(1, 10) == 1:
            return 'c'
        else:
            return 'd'
