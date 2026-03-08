from random import choice


class Random:
    def __init__(self, opponent_move, round_num):
        self.opponent_move = opponent_move
        self.round_num = round_num

    def play(self):
        return choice(['d', 'c'])
