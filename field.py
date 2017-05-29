class Field():
	def __init__(self):
		self.field = [Zone() for x in range(5)]

	def playCard(self, card):
		x = 0
		while not self.field[x].isEmpty():
			x = x+1
		self.field[x].playCard(card)

	def destroyCard(self, card):
		for zone in self.field:
			if zone.getCard() == card:
				zone.clearCard()

	def gameInfo(self):
		return [len(self.player.getDeck()), len(self.player.getHand())]

	def getField(self):
		return self.field

	def printField(self):
		for zone in self.field:
			if not zone.isEmpty():
				print(zone.getCard().name)

class Zone():
	def __init__(self):
		self.contained_card = None;

	def playCard(self, card):
		self.contained_card = card;

	def clearCard(self):
		self.contained_card = None;

	def getCard(self):
		return self.contained_card

	def isEmpty(self):
		return self.contained_card is None

class Grave():
	def __init__(self):
		self.grave = []

	def sendToGrave(self, card):
		self.grave.append(card)

	def getGrave(self):
		return self.grave

	def printGrave(self):
		for card in self.grave:
			print(card.name)