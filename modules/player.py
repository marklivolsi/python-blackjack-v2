class Player:
    def __init__(self, number=1, name='Player 1', chips=1000):
        self.number = number
        self.name = name
        self.chips = chips
        self.hands = []

    def __repr__(self):
        return self.name


class Hand:
    def __init__(self):
        self.cards = []
        self.wager = 0
        self.points = 0

    def __repr__(self):
        return str(self.cards)
