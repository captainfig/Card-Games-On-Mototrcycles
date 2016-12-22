import constants as C, player, parse, random
class Hand(object):
	"""docstring for ClassName"""
	def __init__(self, deck):
		self.deck = deck
		self.hand = []

	def drawCard(self, n):
		for i in range(n):
			self.hand.append(self.deck.drawTopCard())

	def toString(self):
		handStr = ''
		for i in range(len(self.hand)):
			handStr += self.hand[i].name + ', '
		return handStr
