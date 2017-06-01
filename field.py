class Field():
	def __init__(self):
		self.field = [Zone() for x in range(5)]

	def playCard(self, card, zone):
		self.field[zone].playCard(card)

	def destroyCard(self, zone):
		self.field[zone].clearCard()

	def gameInfo(self):
		return [len(self.player.deck), len(self.player.hand)]

	def printContents(self):
		for zone in self.field:
			if not zone.isEmpty():
				print(zone.contents.name)

class Zone():
	def __init__(self):
		self.contents= None;

	def playCard(self, card):
		self.contents = card;

	def clearCard(self):
		self.contents = None;

	def isEmpty(self):
		return self.contents is None