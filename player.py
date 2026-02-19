class Player:
    def __init__(self, name: str = "", score: int = 0, letters: list | None = None):
        self.name = name
        self.score = score
        if letters is None:
            self.letters = []

    def __str__(self):
        # Ideally each person should not be able to see the other person's letters.
        return f"""
        Player: {self.name}
        Score : {self.score}
        Letters: {self.letters}
        """
