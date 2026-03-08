from random import randint


class Reactive1:
    def __init__(self, opponent_move, round_num):
        self.opponent_move = opponent_move
        self.round_num = round_num

    def play(self):
        if self.opponent_move == 'c':
            p = 0.9
        elif self.round_num <= 100:
            p = 0.8
        else:
            p = 0.1
        if randint(1, 100) / 100 < p:
            return 'c'
        else:
            return 'd'
