from util.Deck import Deck
from util.Player import Player
import random


class GameEngine:
    def __init__(self,initial_stack,players_names):
        self._players = [Player(initial_stack,name) for name in players_names]
        self._keepPlaying = 'y'
        self._ante = 0
        self._smallBlind = 0
        self._bigBlind = 0
        self._sbPosition = random.randint(0, len(self._players))
        self._bbPosition = (self._sbPosition + 1) % len(self._players)

    def run_engine(self):
        while self._keepPlaying == 'y':
            #init the round
            current_pot = 0
            board = []
            deck = Deck()
            deck.shuffle()

            #copy the list of players.
            players_in_hand = list(self._players)
            idx_to_speak = (self._bbPosition + 1) % len(players_in_hand)

            # everyone pays ante
            for player in players_in_hand:
                player.lose_money(self._ante)
                current_pot+=self._ante

            # big and small blind pay blinds
            players_in_hand[self._sbPosition].lose_money(self._smallBlind)
            current_pot+=self._smallBlind
            players_in_hand[self._bbPosition].lose_money(self._bigBlind)
            current_pot+=self._bigBlind

            # deal cards
            self.deal_cards(deck)

            for phase in ["Flop","Turn","River"]:
                current_bet = self._bigBlind if phase == "Flop" else 0
                self.cycle_players(current_bet,idx_to_speak,players_in_hand,current_pot)
                round_ended = self.check_if_round_ended(players_in_hand,current_pot)
                if round_ended is False:
                    self._keepPlaying = input("Do you want to keep playing? [y/n]")
                    continue

                if phase == "Flop":
                    for i in range(3):
                        self.board.append(deck.deal_card())
                else:
                    self.board.append(deck.deal_card())
                self.print_round_status(phase)

            #show down!!! :))
            #TODO: SHOWDOWN HERE :)
            self._keepPlaying = input("Do you want to keep playing? [y/n]")

    def check_if_round_ended(self,players_in_hand,current_pot):
        if players_in_hand == 1:
            players_in_hand[0].gain_money(current_pot)
            current_pot = 0
            return False
        return True

    def deal_cards(self,deck):
        for i in range(2):
            for player in self._players:
                player.recieve_card(deck.deal_card())

    def cycle_players(self,initial_bet,idx_to_speak,players_in_hand,current_pot):
        bet = initial_bet
        for i in range(len(players_in_hand)):
            player_to_speak = players_in_hand[(idx_to_speak + i) % (len(players_in_hand))]
            new_bet = player_to_speak.act(bet)
            current_pot += new_bet
            #the player decided to fold
            if new_bet == -1:
                player_to_speak.discard_hand()
                del players_in_hand[(idx_to_speak+i)%(len(players_in_hand))]
                if len(players_in_hand) == 1:
                    return
            #the player decided to raise, new cycle starts from the player that made the bet.
            elif new_bet > bet:
                self.cycle_players(new_bet,idx_to_speak+1%len(players_in_hand),players_in_hand)
            #the player decided to call the bet, continue the current cycle
            elif new_bet == bet:
                current_pot += bet

    def print_round_status(self,phase,players_in_hand,current_pot):
        print("Current Phase: " + phase)
        print("Players in hand: ")
        for player in players_in_hand:
            player.print_player_status()
        print("the board is: ")
        for card in self.board:
            card.print_card()



