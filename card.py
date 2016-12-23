import constants as C, player, parse, random

class Card():
	"""docstring for Card"""
	def __init__(self, cardInfo):
		self.id = int(cardInfo[C.CARD_ID])
		self.name = cardInfo[C.CARD_NAME]
		self.flavor = cardInfo[C.FLAVOR_TEXT]
		self.image = cardInfo[C.CARD_IMAGE]

	def toString(self):
		return self.name