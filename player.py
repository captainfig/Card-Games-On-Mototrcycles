import constants as C
import random, sqlite3, card, parse

class Player():
	def __init__(self, name, deckList):
		self.name = name
		self.deck = Deck(deckList);
		self.hand = []
		self.drawRate = 1

	def getHand(self):
		return self.hand

	def getDeck(self):
		return self.deck.deck

	def getName(self):
		return self.name

	def getDrawRate(self):
		return self.drawRate;

	def drawCard(self, n):
		for i in range(n):
			self.hand.append(self.deck.getCard(0)) # Pop top card, append to hand

	def popCard(self, card):
		self.hand.remove(card)

	def shuffleDeck(self):
		self.deck.shuffle()

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
		return self.deck.pop(index); # Get any card by its placement in the deck

	def printContents(self):
		i = 0
		for card in self.deck:
			print("[" + str(i) + "] " + card.name)
			i = i + 1