import constants as c
import random, sqlite3, card, parse


class Player:

    def __init__(self, name, deckList):
        self.name = name
        self.decklist = deckList
        self.deck = Deck(self.decklist)
        self.hand = []
        self.startGame()

    @property
    def getHand(self):
        return self.hand

    def getDeck(self):
        return self.deck.deck

    def getName(self):
        return self.name

    def drawCard(self, n):
        if len(self.hand) <= c.HAND_MAX - n:
            for i in range(n):
                self.hand.append(self.deck.getCard(0))

    def reset_game(self):
        self.reset_hand()
        self.reset_deck()
        self.startGame()

    def reset_hand(self):
        self.hand.clear()
        self.hand = []

    def reset_deck(self):
        self.deck.clear()
        self.deck = Deck(self.decklist)

    def startGame(self):
        self.deck.shuffle()
        self.drawCard(c.HAND_SIZE)

    def printHand(self):
        handStr = ''
        for i in range(len(self.hand)):
            handStr += self.hand[i].name + ', '
        return handStr


class Deck:

    def __init__(self, deckList):
        self.deckList = deckList
        self.deck = []
        for cardID in self.deckList:
            self.deck.append(card.Card(parse.getCard(cardID)))

    def shuffle(self):
        self.deck = random.sample(self.deck, len(self.deck))

    def getCard(self, index):
        return self.deck.pop(index);

    def clear(self):
        self.deck.clear()

    def printContents(self):
        for card in self.deck:
            print(card.name)
