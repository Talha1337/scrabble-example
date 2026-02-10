from board import ScrabbleBoard

n_turns = 0
max_turns = 10

while n_turns < max_turns:
    n_turns += 1
    if n_turns % 2:
        user_input = input("Player 1: ")
    else:
        user_input = input("Player 2: ")


class Scrabble():
    def __init__(self, board: ScrabbleBoard):
        pass

    def validate_input_slot(slot_input: str):
        try:
            slot_int = int(slot_input)
        except:
            return False
        if slot_int > 224 or slot_int < 0:
            return False
        return True

    def turn(self, player):
        print(f"{player}'s turn.")
        slot = input("Please insert your starting point (0-224): ")
        hor_vert = input(
            "Please specify if the word is vertical (v) or horizontal (h): ")
