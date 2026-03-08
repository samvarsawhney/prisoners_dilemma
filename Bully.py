from random import randint


class Bully:
    def __init__(self, opponent_move, round_num):
        self.opponent_move = opponent_move
        self.round_num = round_num
        self.aggression_prob = 0.05

    def play(self):
        if self.round_num == 1:
            return 'd'
        if self.opponent_move == 'd' or randint(1, 100) / 100 < self.aggression_prob:
            return 'd'
        else:
            return 'c'
