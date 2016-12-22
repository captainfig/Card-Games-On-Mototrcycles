import constants as C, player, parse, random, card

class Deck:
	def __init__(self, deckList):
		self.deckList = deckList
		self.deck = []

	def shuffle(self):
		self.deck = random.sample(self.deck, len(self.deck))

	def buildDeck(self):
		for i in range(C.DECK_SIZE):
			for cardID in self.deckList:
				self.deck.append(card.Card(parse.getCard(cardID)))

	def getTopCard(self):
		return self.deck[0]

	def drawTopCard(self):
		top = self.getTopCard()
		self.deck.remove(top)
		return top