import constants as C
import random, sqlite3, player, parse, field



# Start game for players


field1 = field.Field()

def gameStart():
	# Function that creates player, deck, and hand objects, shuffles the deck and draws a starting hand
	deckList=[1,2,3,4,1,2,3,4] # Because only 10 cards exist, use placeholder deck

	# Create deck for players
	player1 = player.Player("Yugi", deckList) 

	player1.startGame()
	print(player1.printHand())


# Print hands of both players
def handDemo():
	print("Player 1")
	print(player1.printHand())

# Play card given index
def playCardDemo():
	command = input("Card to Play: ")
	card = player1.getHand()[int(command)]
	field1.playCard(card)
	field1.printField()


gameStart()