

class Roll:
    
    def __init__(self, name: str, wins: list=[], loses: list=[]):
        self.name = name
        self.wins = wins
        self.loses = loses

    def check_win(self, opposing_roll) -> bool:
        return opposing_roll in wins:

class Player:

    def __init__(self, name: str):
        self.name = name

