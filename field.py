class Field:
	def __init__(self):
		self.field = [[Zone("monster") for x in range(5)] for y in range(2)]

	def playCard(self, card):
		for x in range(len(self.field)):
			pass

	def gameInfo(self):
		return [len(self.player.getDeck()), len(self.player.getHand)]

	def getField(self):
		return field

	def printField(self):
		for i in range(len(self.field)):
			print("Field: ["+str(i)+"]("+str(self.field[i].power)+") "+self.field[i].name+" | ")

class Zone():
	def __init__(self, card_type):
		self.card_type = card_type;
		self.contained_card = None;

	def playCard(self, card):
		self.contained_card = card;

	def clearCard(self):
		self.contained_card = None;

	def isEmpty():
		if(contained_card is None):
			return true;