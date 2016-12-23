import cocos
from cocos.actions import *
import player

class bgLayer(cocos.layer.ColorLayer):
	def __init__(self):
		super(bgLayer, self).__init__(64,64,224,255)
		self.player = player
		label = cocos.text.Label('Dueling Simulator',
			font_name='Times New Roman',
			font_size=32,
			anchor_x='center', anchor_y='center')
		label.position = 320,240
		self.add(label)
		scale = ScaleBy(3, duration=2)
		label.do(Repeat(scale + Reverse(scale)))

class cardLayer(cocos.layer.ColorLayer):
	def __init__(self, player):
		super(cardLayer, self).__init__(64,64,224,255)
		self.player = player
		self.displayHand()

	def displayHand(self):
		hand = self.player.hand.hand
		for i in range(len(self.player.hand.hand)):
			card = hand[i].image
			sprite = cocos.sprite.Sprite(card)
			sprite.scale = 0.3
			sprite.position = (i * 200 + 100), 240
			self.add(sprite, z=1)

			label = cocos.text.Label(hand[i].name,
			font_name='Times New Roman',
			font_size=14,
			anchor_x='center', anchor_y='center')
			label.position = (i * 200 + 100), 390
			self.add(label)

cocos.director.director.init(1600, 900)
player1 = player.Player("Yugi", [1, 2, 3, 4, 5])
player1.startGame()
bgLayer = bgLayer()
hello_layer = cardLayer(player1)
#hello_layer.do(RotateBy(360, duration=10))

main = cocos.scene.Scene(hello_layer)

cocos.director.director.run(main)