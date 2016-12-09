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