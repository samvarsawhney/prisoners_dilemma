class TitForTat:
    def __init__(self, opponent_move, round_num):
        self.opponent_move = opponent_move
        self.round_num = round_num

    def play(self):
        if self.opponent_move == 'd':
            return 'd'
        else:
            return 'c'
