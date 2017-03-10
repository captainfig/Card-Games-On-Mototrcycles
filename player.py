import constants as C
import random, sqlite3, card, parse

class Player():
	def __init__(self, name, deckList):
		self.name = name
		self.deck = Deck(deckList);
		self.hand = []

	def getHand(self):
		return self.hand.hand

	def getDeck(self):
		return self.deck.deck

	def getName(self):
		return self.name

	def drawCard(self, n):
		for i in range(n):
			self.hand.append(self.deck.getCard(0))
			print("Draw " + str(i+1))
			self.deck.printContents()

	def startGame(self):
		self.deck.shuffle()
		self.drawCard(C.HAND_SIZE)
		
	def printHand(self):
		handStr = ''
		for i in range(len(self.hand)):
			handStr += self.hand[i].name + ', '
		return handStr	

class Deck:
	def __init__(self, deckList):
		self.deckList = deckList
		self.deck = []
		for i in range(C.DECK_SIZE):
			for cardID in self.deckList:
				self.deck.append(card.Card(parse.getCard(cardID)))

	def shuffle(self):
		self.deck = random.sample(self.deck, len(self.deck))

	def getCard(self, index):
		return self.deck.pop(index);

	def printContents(self):
		for card in self.deck:
			print(card.name)