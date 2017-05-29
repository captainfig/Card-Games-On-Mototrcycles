import constants as C
import player, field

## The idea here is to create an action for everything possible in the game
## Then cards will be programmed to be a series of these functions

## There is probably a way to make this so that player, field, and grave are not passed to each individual action

class Turn():
	def __init__(self):
		self.actions = []

	def push(self, action):
		self.actions.append(action)

	def pop(self):
		self.actions.pop()

	def is_empty(self):
		return (self.actions == [])

class Action():
	def __init__(self, player):
		self.player = player

	def action(self):
		pass

class DrawCard(Action):
	def __init__(self, player, n):
		super().__init__(player)
		self.action(n)

	def action(self, n):
		self.player.drawCard(n)

class PlayCardFromHand(Action):
	def __init__(self, player, field, card):
		super().__init__(player)
		self.field = field
		self.card = card
		self.action()

	def action(self):
		self.player.popCard(self.card)
		self.field.playCard(self.card)

class DestroyCard(Action):
	def __init__(self, player, field, card, grave):
		super().__init__(player)
		self.field = field
		self.card = card
		self.grave = grave
		self.action()

	def action(self):
		self.field.destroyCard(self.card)
		self.grave.sendToGrave(self.card)





