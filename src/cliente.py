"Singleton Use Case Example Code."

from jogo1 import Game1
from jogo2 import Game2
from jogo3 import Game3


GAME1 = Game1()
GAME1.add_winner(1, "Brasil", "3", "1", "1", "Alisson, Daniel Alves, Thiago Silva, Marquinhos e Alex Sandro; Casemiro, Fred e Lucas Paquetá; Raphinha, Richarlison e Vini Jr")

GAME2 = Game2()
GAME2.add_winner(2, "Suiça", "3", "1", "1", "Sommer, Widmer, Schar, Akanji e Rodriguez, Freuler, Xhaka, Shaqiri, Sow e Vargas, Embolo")

GAME3 = Game3()
GAME3.add_winner(3, "Camarões", "0", "1", "0", "Onana; Tolo, N'Koulou, Castelletto e Fai; Ekambi, Hongla, Ntcham e Bryan Mbeumo; Choupo-Moting e Aboubakar")

GAME1.leaderboard.print()
GAME2.leaderboard.print()
GAME3.leaderboard.print()
