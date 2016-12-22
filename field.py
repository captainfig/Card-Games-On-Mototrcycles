class Field:
	def __init__(self):
		self.field = []

	def playCard(self, card):
		self.field.append(card)

	def gameInfo(self):
		return [len(self.player.getDeck()), len(self.player.getHand())]

	def getField(self):
		return field

	def printField(self):
		for i in range(len(self.field)):
			print("Field: ["+str(i)+"]("+str(self.field[i].power)+") "+self.field[i].name+" | ")