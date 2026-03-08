from random import randint


class GenerousTitForTat:
    def __init__(self, opponent_move, round_num):
        self.opponent_move = opponent_move
        self.round_num = round_num

    def play(self):
        if self.opponent_move == 'd':
            if randint(1, 100) / 100 < 0.1:
                return 'c'
            else:
                return 'd'
        else:
            return 'c'
