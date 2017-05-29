import constants as C
import random, sqlite3, player, parse, field, actions

def gameStart():
	# Function that creates player, deck, and hand objects, shuffles the deck and draws a starting hand
	deckList=[1,2,3,4,5,6,7,8] # Because only 10 cards exist, use placeholder deck

	# Create deck for players
	player1 = player.Player("Yugi", deckList)
	field1 = field.Field()
	grave1 = field.Grave()

	# Create variable for p1's field
	p1_field = field1.getField()
	p1_grave = grave1.getGrave()

	# List of all actions taken
	action_list = actions.Turn()

	# Shuffle deck
	print("Decklist") 
	player1.deck.printContents()
	print("\nShuffling...")
	player1.shuffleDeck()
	print("New order...\n")
	player1.deck.printContents()

	# Draw cards
	print("\nDrawing...")
	action_list.push(actions.DrawCard(player1, 3))
	print("Remaining Cards")
	player1.deck.printContents()
	print("\nHand")
	print(player1.printHand())

	# Draw phase
	print("\nDrawing 1 Card")
	action_list.push(actions.DrawCard(player1, player1.getDrawRate()))
	print(player1.printHand())

	# Play 2 cards from hand
	cardToPlay1 = player1.getHand()[2]
	cardToPlay2 = player1.getHand()[0]
	print("\nPlaying " + str(cardToPlay1.name) + " & " + str(cardToPlay2.name))

	action_list.push(actions.PlayCardFromHand(player1, field1, cardToPlay1))
	action_list.push(actions.PlayCardFromHand(player1, field1, cardToPlay2))

	print(player1.printHand())
	print("\nField...")
	field1.printField()

	# Destroy 1 card on field
	cardToDestroy = p1_field[0].getCard()
	print("\nDestroying " + str(cardToDestroy.name) + "...")

	action_list.push(actions.DestroyCard(player1, field1, cardToDestroy, grave1))

	print("\nField...")
	field1.printField()
	print("\nGrave...")
	grave1.printGrave()



gameStart()