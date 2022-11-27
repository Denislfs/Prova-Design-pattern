"A Game Class that uses the Leaderboard Singleton"

from tabela_lideranca import Leaderboard
from Interface import IGame


class Game1(IGame):
    "Game1 implements IGame"

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, posicao,time, ponto, jogos, vitorias, jogadores):
        self.leaderboard.add_winner(posicao,time, ponto, jogos, vitorias, jogadores)

