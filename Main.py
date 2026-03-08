from random import choice, choices
from time import sleep

from Alternate1 import Alternate1
from Alternate2 import Alternate2
from Bully import Bully
from Complex1 import Complex1
from Complex2 import Complex2
from FadingCooperation import FadingCooperation
from FadingDefection import FadingDefection
from GenerousTitForTat import GenerousTitForTat
from OppositeTitForTat import OppositeTitForTat
from Random import Random
from Reactive1 import Reactive1
from Reactive2 import Reactive2
from Reactive3 import Reactive3
from Reactive4 import Reactive4
from SuspiciousTitForTat import SuspiciousTitForTat
from TitForTat import TitForTat


def cursor(time):
    a = ["\033[3;32m", "\033[3;32m", "\033[3;32m", "\033[3;32m", "\033[3;32m", "\033[3;32m", "\033[3;32m", "\033[3;32m",
         "\033[3;32m", "\033[3;32m", "\033[3;32m"]
    for i, val in enumerate(range(time, 0, -1)):
        print("\b" * 100, end="", flush=True)
        sleep(0.5)
        print(f"{a[i]}█\033[0m", end="", flush=True)
        sleep(0.5)
    print("\b" * 100, end="", flush=True)
cursor(10)

s = [Complex1, Complex2, TitForTat, SuspiciousTitForTat, GenerousTitForTat, OppositeTitForTat, Random,
            Alternate1, Alternate2, FadingCooperation, FadingDefection, Reactive1, Reactive2, Reactive3, Reactive4,
            Bully]
k = choice([5, 6])
strategy = choices(s, k=k+1)
class PrisonersGame:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.rounds = 2000
        self.player1_strategy = choice(strategy)
        self.player2_strategy = choice(strategy)

    def game(self):
        player2_last_move = ''
        player1_last_move = ''
        for n in range(1, self.rounds + 1):
            player1_move = self.player1_strategy(player2_last_move, n).play()
            player2_move = self.player2_strategy(player1_last_move, n).play()
            player1_move = 'd' if player1_move.lower().startswith('d') else 'c'
            player2_move = 'd' if player2_move.lower().startswith('d') else 'c'
            if player1_move == "d" and player2_move == "d":
                self.player1_score += 1
                self.player2_score += 1
            elif player1_move == "c" and player2_move == "c":
                self.player1_score += 3
                self.player2_score += 3
            elif player1_move == "d" and player2_move == "c":
                self.player1_score += 5
                self.player2_score += 0
            elif player1_move == "c" and player2_move == "d":
                self.player1_score += 0
                self.player2_score += 5
            player2_last_move = player2_move
            player1_last_move = player1_move
        return self.player2_score, self.player1_score

    def winner(self):
        return self.player1_strategy.__name__, self.player2_strategy.__name__, self.player1_score, self.player2_score

    def play(self):
        self.game()
        self.winner()


def main():
    scores = {}
    for i in range(5000):
        game = PrisonersGame()
        game.play()
        if game.player1_strategy.__name__ in scores:
            scores[game.player1_strategy.__name__] += game.player1_score
        else:
            scores[game.player1_strategy.__name__] = game.player1_score
        if game.player2_strategy.__name__ in scores:
            scores[game.player2_strategy.__name__] += game.player2_score
        else:
            scores[game.player2_strategy.__name__] = game.player2_score
    sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    print("\033[3;32mPrisoner's Dilemma\033[0m")
    print("\033[3;32m—\033[0m" * 20)
    for name, score in sorted_scores.items():
        cursor(3)
        print(f"\033[3;32m{name}: {score}\033[0m")

r = True
while r:
    main()
    print("\033[3;32m—\033[0m"*20)
    user_input = input("\033[3;32mPress Enter to continue or any other key to quit... \033[0m")
    cursor(3)
    if not user_input == "":
        break
print("\033[3;32mThanks for using Samvar's Prisoner's Dilemma software\033[0m")