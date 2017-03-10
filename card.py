import constants as C, player, parse, random

class Card():
	"""docstring for Card"""
	def __init__(self, cardInfo):
		self.id = int(cardInfo[C.CARD_ID])
		self.name = cardInfo[C.CARD_NAME]
		self.image = cardInfo[C.CARD_IMAGE]
		self.card_type = cardInfo[C.CARD_TYPE]
		self.attribute = cardInfo[C.ATTRIBUTE]
		self.attack = cardInfo[C.ATK]
		self.defense = cardInfo[C.DEF]
		self.EFFECT = cardInfo[C.EFFECT]

	def toString(self):
		return self.name