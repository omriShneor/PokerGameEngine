from random import randint
from .Card import Card


class Deck:
    def __init__(self):
        self._cards = [Card(suit, value) for suit in ["Spades", "Clubs", "Hearts", "Diamonds"] for value in range(2, 14)]


    def shuffle(self):
        """
        shuffles the values in self.cards list using Fisher–Yates shuffle Algorithm, runs in O(n)
        :return: returns self
        """
        for i in range(len(self._cards)-1,0,-1):
            r = randint(0,i)
            self._cards[i],self._cards[r] = self._cards[r],self._cards[i]


    def deal_card(self):
        """
        deals a card from the top of the deck
        :return: returns a Card instance from the top of the deck and removes it from the deck
        """
        return self._cards.pop(0)

    def __str__(self):
        """
        prints all the cards in the Deck.
        :return: no return value
        """
        return '[%s]' % ', '.join(map(str, self._cards))

    def __repr__(self):
        return "Deck()"

    def __getitem__(self, position):
        return self._cards[position]

