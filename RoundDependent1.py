class RoundDependent1:
    def __init__(self, opponent_move, round_num):
        self.opponent_move = opponent_move
        self.round_num = round_num

    def play(self):
        if self.round_num < 150:
            return 'c'
        else:
            return 'd'
