import constants as C
import random, sqlite3
class Player():
	def __init__(self, name, deck):
		self.name = name
		self.deck = deck;
		self.hand = []

	def initialShuffle(self):
		self.deck = random.sample(self.deck, len(self.deck))

	def initialDraw(self):
		while len(self.hand) < C.HAND_SIZE:
			self.drawCard()

	def drawCard(self):
		self.hand.append(self.deck[0])
		self.deck.remove(self.deck[0])

	def getHand(self):
		return self.hand

	def getDeck(self):
		return self.deck

	def getName(self):
		return self.name

	def startGame(self):
		self.initialShuffle()
		self.initialDraw()

