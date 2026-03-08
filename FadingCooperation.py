from random import randint


class FadingCooperation:
    def __init__(self, opponent_move, round_num):
        self.opponent_move = opponent_move
        self.round_num = round_num

    def play(self):
        if randint(1, 10) / 10 < max(0, 1 - 0.1 * self.round_num):
            return 'c'
        else:
            return 'd'
