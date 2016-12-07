class Field:
	def __init__(self, player):
		self.field = []
		self.player = player

	def summonCreature(self, card):
		self.field.append(card)

	def gameInfo(self):
		return [len(self.player.getDeck()), len(self.player.getHand())]

	def getField(self):
		return field

	def toString(self):
		return str(self.player.getName()) + '\'s Field: ' + self.getField() + '| DECK: ' + len(self.player.getDeck()) +
		'| HAND: ' + len(self.player.getHand())