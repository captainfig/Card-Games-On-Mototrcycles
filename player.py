import constants as C
import random, sqlite3, deck
class Player():
	def __init__(self, name, deckList):
		self.name = name
		self.deck = deck.Deck(deckList, self);
		self.hand = []

	def getHand(self):
		return self.hand

	def getDeck(self):
		return self.deck

	def getName(self):
		return self.name

	def startGame(self):
		self.deck.shuffle()
		self.deck.drawCard(3)

	def printHand(self):
		str = self.hand[0].toString()
		for i in range(len(self.hand)):
			if i > 0:
				str += ' | ' + self.hand[i].toString()
		return str


