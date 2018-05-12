import random


class Card:
    def __init__(self,suit=None,value=None):
        if suit is None or value is None:
            self.suit = random.choice(["Spades", "Clubs", "Hearts", "Diamonds"])
            self.value = random.choice(range(2,15))
        else:
            self.suit = suit
            self.value = value

    def __str__(self):
        """
        prints a string representing the value and the suit of the card
        :return: no return value
        """
        cards = list(range(2,11)) + ["Jack","Queen","King","Ace"]
        print(str(cards[self.value]) + " of %s" % self.suit)

    def __repr__(self):
        print("Card(%d,%s)" % (self.value,self.suit))
