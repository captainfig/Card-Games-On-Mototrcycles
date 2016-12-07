import constants as C
import random, sqlite3, player, parse

deck=[1,2,3,4,5,6,7,8,9,10] # Because only 10 cards exist, use placeholder deck

# Create deck for players
player1 = player.Player(deck) 
player2 = player.Player(deck)

# Start game for players
player1.startGame()
player2.startGame()

# Print hands of both players (for demo purposes)
print("Player 1")
parse.printHand(player1.getHand())
print("Player 2")
parse.printHand(player2.getHand())
