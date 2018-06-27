import player
import ui_elements as ui
import constants as c

import cocos
from cocos.actions import *

# This file is all the cocos2d layer stuff

# The Background
class BackgroundLayer(cocos.layer.ColorLayer):
    def __init__(self):
        super(BackgroundLayer, self).__init__(64, 64, 224, 255)
        self.player = player
        label = cocos.text.Label('Dueling Simulator',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        label.position = 800, 850
        self.add(label)
        scale = ScaleBy(1.1, duration=2)
        label.do(Repeat(scale + Reverse(scale)))


# Layer for player 1 hand
class HandLayer(cocos.layer.Layer):
    def __init__(self, _player):
        super(HandLayer, self).__init__()
        self.hand = _player.hand
        self.position = (c.HAND_X, c.HAND_Y)
        self.cards = []
        self.display_hand()

    def display_hand(self):
        i = 0
        for player_card in self.hand:
            new_card = ui.CardSprite(player_card)
            new_card.position = (i * (new_card.width + c.CARD_DIST), 0)
            self.add(ui.GameButton(new_card.x, new_card.y, new_card.width, new_card.height))
            self.add(new_card)
            i = i+1


# the main game interface
class GameLayer(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self):
        super(GameLayer, self).__init__()
        self.position = (0, 0)
        self.player = player.Player("Yugi", c.DEFAULT_DECK)  # Pass list of card IDs for Deck object to turn into Cards

        self.background = BackgroundLayer()
        self.hand_layer = HandLayer(self.player)

        self.draw_button = ui.MenuButton('Draw Card', 200, 150)
        self.new_game_button = ui.MenuButton('New Game', 350, 150)
        self.quit_button = ui.MenuButton('Exit', 500, 150)

        # displays hand size
        self.card_num = cocos.text.Label(str(len(self.hand_layer.hand)),
                                         font_size=18,
                                         x=800,
                                         y=150,
                                         color=(0, 0, 0, 255))

        self.add(self.background, 0, "Background")
        self.add(self.hand_layer, 1, "Hand")
        self.add(self.draw_button)
        self.add(self.new_game_button)
        self.add(self.quit_button)
        self.add(self.card_num, 1, "card num")

    def update(self):
        self.card_num.element.text = str(len(self.hand_layer.hand))
        self.card_num.element.x = 800
        self.card_num.element.y = 150
        self.hand_layer.display_hand()

    # For button click graphic
    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.draw_button.check_click(x, y):
            self.draw_button.on_click()
        elif self.new_game_button.check_click(x, y):
            self.new_game_button.on_click()
        if self.quit_button.check_click(x, y):
            self.quit_button.on_click()

# Check for button presses after mouse click
    def on_mouse_release(self, x, y, buttons, modifiers):
        if self.draw_button.check_click(x, y):
            self.draw_button.on_release()
            self.player.drawCard(1)
        if self.new_game_button.check_click(x, y):
            self.new_game_button.on_release()
            self.reset()
        if self.quit_button.check_click(x, y):
            self.quit_button.on_release()
            exit()
        self.update()

    # Create new board
    def reset(self):
        self.player.reset_game()
        self.remove("Hand")
        self.hand_layer = HandLayer(self.player)
        self.add(self.hand_layer, 1, "Hand")


# ----------------
# Run the interface
cocos.director.director.init(c.WIN_W, c.WIN_H)
default_scene = cocos.scene.Scene(GameLayer())
cocos.director.director.run(default_scene)
