"A Leaderboard Singleton Class"


class Leaderboard():
    "The Leaderboard as a Singleton"
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        "A class level method"
        print("-------Posição-----------Time---------Pontos--------Jogos----------Vitorias-------------Jogadores-----------------------")
        for key, value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value[0]}\t|\t{value[1]}\t|\t{value[2]}\t|\t{value[3]}\t|\t{value[4]}\t\n")
        print()

    @classmethod
    def add_winner(cls, posicao,time, ponto, jogos, vitorias, jogadores):
        "A class level method"
        cls._table[posicao] = time, ponto, jogos, vitorias, jogadores
