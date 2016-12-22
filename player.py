import constants as C
import random, sqlite3, deck, hand

class Player():
	def __init__(self, name, deckList):
		self.name = name
		self.deck = deck.Deck(deckList);
		self.hand = hand.Hand(self.deck)

	def getHand(self):
		return self.hand.hand

	def getDeck(self):
		return self.deck.deck

	def getName(self):
		return self.name

	def startGame(self):
		self.deck.buildDeck()
		self.deck.shuffle()
		self.hand.drawCard(C.HAND_SIZE)
		

	def printHand(self):
		return self.hand.toString()


