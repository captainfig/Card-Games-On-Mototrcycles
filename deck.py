import constants as C, player, parse, random, card

class Deck:
	def __init__(self, deckList, player):
		self.deck = deckList
		self.player = player

	def shuffle(self):
		self.deck = random.sample(self.deck, len(self.deck))

	def initialDraw(self):
		while len(self.player.getHand()) < C.HAND_SIZE:
			self.drawCard()

	def createCardObj(self, cardInfo):
		return card.Card(cardInfo)

	def drawCard(self, num):
		for i in range(num):
			topCard = self.deck[0]
			self.player.hand.append(self.createCardObj(parse.getCard(topCard)))
			self.deck.remove(self.deck[0])