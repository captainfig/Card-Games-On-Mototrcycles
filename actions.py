import constants as C
import player, field

## The idea here is to create an action for everything possible in the game
## Then cards will be programmed to be a series of these functions

## There is probably a way to make this so that player, field, and grave are not passed to each individual action

class ActionLog():
	def __init__(self):
		self.actions = []

	def push(self, action):
		self.actions.append(action)

	def pop(self):
		self.actions.pop().action()

	def is_empty(self):
		return (self.actions == [])

class Action():
	def __init__(self, player):
		self.player = player

	def action(self):
		pass

	def response(self):
		pass

class DrawHand(Action):
	def action(self):
		self.player.drawCard(3)

class DrawCard(Action):
	def action(self):
		self.player.drawCard(1)

class PlayCardFromHand(Action):
	def __init__(self, player, field, card, zone):
		super().__init__(player)
		self.field = field
		self.card = card
		self.zone = zone

	def response(self):
		pass
		

	def action(self):
		self.player.hand.removeCard(self.card)
		self.field.playCard(self.card, self.zone)

class DestroyCard(Action):
	def __init__(self, player, field, zone):
		super().__init__(player)
		self.field = field
		self.zone = zone

	def action(self):
		self.player.grave.sendToGrave(self.field.field[self.zone].contents)
		self.field.destroyCard(self.zone)
		





