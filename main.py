import constants as C
import random, sqlite3, player, parse, field

deck=[1,2,3,4,5,6,7,8,9,10] # Because only 10 cards exist, use placeholder deck

# Create deck for players
player1 = player.Player("Yugi", deck) 
player2 = player.Player("Kaiba", deck)

# Start game for players
player1.startGame()
player2.startGame()

field1 = field.Field(player1)
field2 = field.Field(player2)

# Print hands of both players
def handDemo():
	print("Player 1")
	print(player1.printHand())
	print("Player 2")

def cardEffectDemo():
	pass