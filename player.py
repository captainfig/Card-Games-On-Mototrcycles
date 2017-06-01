import constants as C
import random, card

class Player():
	def __init__(self, name, deckList):
		self.name = name
		self.deck = Deck(deckList);
		self.hand = Hand()
		self.grave = Grave()

	def drawCard(self, n):
		for i in range(n):
			self.hand.addCard(self.deck.getCard(0)) # Pop top card, append to hand

	def shuffleDeck(self):
		self.deck.shuffle()

class Hand:
	def __init__(self):
		self.contents = []

	def addCard(self, card):
		self.contents.append(card)

	def removeCard(self, card):
		self.contents.remove(card)

	def printContents(self):
		i = 0
		for card in self.contents:
			print("[" + str(i) + "] " + card.name)
			i = i + 1

class Deck:
	def __init__(self, deckList):
		self.deckList = deckList
		self.contents = []
		for cardID in self.deckList:
			self.contents.append(card.Card(card.getCardInfo(cardID)))

	def shuffle(self):
		self.contents = random.sample(self.contents, len(self.contents))

	def getCard(self, index):
		return self.contents.pop(index); # Get any card by its placement in the deck

	def printContents(self):
		i = 0
		for card in self.contents:
			print("[" + str(i) + "] " + card.name)
			i = i + 1

class Grave():
	def __init__(self):
		self.contents = []

	def sendToGrave(self, card):
		self.contents.append(card)

	def printContents(self):
		for card in self.contents:
			print(card.name)