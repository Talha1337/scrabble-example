from game import Scrabble
from board import ScrabbleBoard
from input_checker import InputChecker
from letters import Letters
from player import Player

#  Should probably add some tests here, will save time over time.
#  Some typical games
#  Some extreme plays


class Move():
    def __init__(self, pos: int, orientation: str, word: str):
        pass


scrabble_board = ScrabbleBoard()
input_checker = InputChecker()
letters = Letters()
scrabble_game = Scrabble(scrabble_board, input_checker, letters)
