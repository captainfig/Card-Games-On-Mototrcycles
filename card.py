import constants as C, player, parse, random

class Card():
	"""docstring for Card"""
	def __init__(self, cardInfo):
		self.id = cardInfo[C._ID]
		self.name = cardInfo[C._NAME]
		self.type = cardInfo[C._TYPE]
		self.power = cardInfo[C._POWER]
		self.flavor = cardInfo[C._FLAVOR]

	def toString(self):
		return "Level " + str(self.power) + " " + self.name

	def activate(self):
		pass
		# this will activate the script associated with the card id