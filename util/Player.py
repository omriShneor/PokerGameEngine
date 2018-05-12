class Player:
    def __init__(self,stack,name="sasi"):
        """
        returns an instance of Player
        :param stack: must be initialized to a non positive value
        :param name: the name of the player,default value is sasi.
        """
        if stack is None or stack < 0:
            raise ValueError("Initiale stack must not be None or negative")
        self._name = name
        self._cards = []
        self._stack = stack
        self.chips_invested_in_bet = 0

    def __str__(self):
        print("Player %s has %f chips remaining in he's stack, the players hand is:" % (self._name, self._stack))
        for card in self._cards:
            str(card)

    def __repr__(self):
        print("Player(%f,%s)" % (self._stack,self._name))

    def gain_money(self,sum):
        self._stack += sum

    def lose_money(self,sum):
        """
        decreases the value of initial_stack by sum amount where sum is a long value.
        if the initial_stack<sum then a ValueError is thrown
        :param sum: the value to decrease initial_stack with
        """
        if self._stack < sum:
            raise ValueError("Player %s has lost all of he's money." % (self._name,))
        else:
            self._stack -= sum

    def recieve_card(self,card):
        """
        sets self.hand=cards, where cards is a tuple of Card objects
        :param cards: a list of 2 cards.
        """
        if len(self._cards) >= 2:
            raise ValueError("number of cards in the hand should be 2 at most.")
        self._cards.append(card)

    def discard_hand(self):
        self._cards = []

    def act(self,bet):
        #TODO: create the logics of act
        return bet

    def update_chips_invested_in_bet(self,value):
        self.chips_invested_in_bet = value - self.chips_invested_in_bet
