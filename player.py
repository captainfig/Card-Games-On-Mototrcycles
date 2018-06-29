import constants as c
import random
import card
import parse


class Player:
    def __init__(self, name, deck_list):
        self.name = name
        self.deck_list = deck_list
        self.deck = Deck(self.deck_list)
        self.hand = []
        self.start_game()

    def draw_card(self, n):
        if len(self.hand) <= c.HAND_MAX - n:
            for i in range(n):
                self.hand.append(self.deck.draw_card())

    def remove_card(self, _card):
        self.hand.remove(_card)

    def reset_game(self):
        self.hand.clear()
        self.deck.reset()
        self.start_game()

    def start_game(self):
        self.deck.shuffle()
        self.draw_card(c.HAND_SIZE)

    def print_hand(self):
        hand_str = ''
        for i in range(len(self.hand)):
            hand_str += self.hand[i].name + ', '
        return hand_str


class Deck:
    def __init__(self, deck_list):
        self.deckList = deck_list
        self.deck = []
        self.populate_deck()

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return str(self.deck)

    def populate_deck(self):
        for cardID in self.deckList:
            self.deck.append(card.Card(parse.getCard(cardID)))

    def reset(self):
        self.deck.clear()
        self.populate_deck()

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)

    def get_card(self, index):
        return self.deck.pop(index)

    def add_card(self, _card):
        self.deck.append(_card)
