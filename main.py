import constants as C
import player, field, actions

deckList=[1,2,3,4,5,6,7,8] # Because only 10 cards exist, use placeholder deck

# Create deck for players
player1 = player.Player("Yugi", deckList)
field1 = field.Field()

# Create variable for p1's field
p1_field = field1.field

# List of all actions taken
action_list = actions.ActionLog()

def gameStart():
	# Function that creates player, deck, and hand objects, shuffles the deck and draws a starting hand
	
	pass


def deckTest():
	# Shuffle deck
	print("Decklist") 
	player1.deck.printContents()
	print("\nShuffling...")
	player1.shuffleDeck()
	print("New order...\n")
	player1.deck.printContents()

	# Draw cards
	print("\nDrawing...")
	action_list.push(actions.DrawHand(player1))
	action_list.pop()
	print("Remaining Cards")
	player1.deck.printContents()
	print("\nHand")
	player1.hand.printContents()

	# Draw phase
	print("\nDrawing 1 Card")
	action_list.push(actions.DrawCard(player1))
	action_list.pop()
	player1.hand.printContents()

	# Play 2 cards from hand, in zones 0 and 1
	cardToPlay1 = player1.hand.contents[2]
	cardToPlay2 = player1.hand.contents[0]
	print("\nPlaying " + str(cardToPlay1.name) + " & " + str(cardToPlay2.name))

	action_list.push(actions.PlayCardFromHand(player1, field1, cardToPlay1, 0))
	action_list.pop()
	action_list.push(actions.PlayCardFromHand(player1, field1, cardToPlay2, 1))
	action_list.pop()

	player1.hand.printContents()
	print("\nField...")
	field1.printContents()

	# Destroy card in zone 0
	print("\nDestroying " + str(field1.field[0].contents.name) + "...")
	action_list.push(actions.DestroyCard(player1, field1, 0))
	action_list.pop()

	print("\nField...")
	field1.printContents()
	print("\nGrave...")
	player1.grave.printContents()


##gameStart()
deckTest()