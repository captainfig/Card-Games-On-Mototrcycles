import cocos, pyglet
import constants as c
from cocos.actions import *
import player


## This file is all the cocos2d layer stuff

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


class GameButton(cocos.sprite.Sprite):
    def __init__(self, text, x, y):
        super(GameButton, self).__init__("resources/button_1.png")
        self.label = cocos.text.Label(text=text,
                                      font_name='Times New Roman',
                                      font_size=14,
                                      anchor_x='center', anchor_y='center')
        self.x = x
        self.y = y
        self.add(self.label, 2)
        self.top_left = self.x - (self.width / 2), self.y + (self.height / 2)
        self.top_right = self.x + (self.width / 2), self.y + (self.height / 2)
        self.bot_left = self.x - (self.width / 2), self.y - (self.height / 2)
        self.bot_right = self.x + (self.width / 2), self.y - (self.height / 2)
        self.add(cocos.sprite.Sprite("resources/button_1_p.png"), 1, "Press")
        self.get("Press").visible = False

    def on_click(self):
        self.get("Press").visible = True

    def on_release(self):
        self.get("Press").visible = False

    def check_click(self, x, y):
        if x > self.top_left[0] and y < self.top_left[1]:
            if x < self.bot_right[0] and y > self.bot_right[1]:
                return True
        return False

    def get_top_left(self):
        return self.top_left

    def get_bot_right(self):
        return self.bot_right


class CardSprite(cocos.sprite.Sprite):
    def __init__(self, card):
        super(CardSprite, self).__init__("resources/cardtemp.png", anchor=(0, 0))
        card_name = self.create_label(card.name, 14)
        card_attack = self.create_label(str(card.attack), 12)
        card_defense = self.create_label(str(card.defense), 12)
        card_image = cocos.sprite.Sprite(card.image, anchor=(0, 0))

        card_name.position = (11, 253)
        card_attack.position = (130, 50)
        card_defense.position = (130, 30)
        card_image.position = (c.IMG_LEFT, c.IMG_BOTTOM)

        self.add(card_name)
        self.add(card_attack, 2)
        self.add(card_defense, 2)
        self.add(card_image)

    def create_label(self, text, size):
        return cocos.text.Label(text,
                                font_name='Times New Roman',
                                font_size=size,
                                bold=True,
                                color=(0, 0, 0, 255),
                                anchor_x='left', anchor_y='top')


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
            new_card = CardSprite(player_card)
            new_card.position = (i * (new_card.width + c.CARD_DIST), 0)
            self.add(new_card)
            i = i+1


class GameLayer(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self):
        super(GameLayer, self).__init__()
        self.position = (0, 0)
        self.player = player.Player("Yugi", c.DEFAULT_DECK)  # Pass list of card IDs for Deck object to turn into Cards

        self.background = BackgroundLayer()
        self.hand_interface = HandLayer(self.player)
        self.draw_button = GameButton('Draw Card', 200, 150)
        self.new_game_button = GameButton('New Game', 350, 150)
        self.quit_button = GameButton('Exit', 500, 150)

        self.add(self.background, 0, "Background")
        self.add(self.hand_interface, 1, "Hand")

        self.card_num = cocos.text.Label(str(len(self.hand_interface.hand)),
                                         font_size=18,
                                         x=800,
                                         y=150,
                                         color=(0, 0, 0, 255))
        self.add(self.card_num, 1, "card num")

        self.add(self.draw_button)
        self.add(self.new_game_button)
        self.add(self.quit_button)

    def update(self):
        self.card_num.element.text = str(len(self.hand_interface.hand))
        self.card_num.element.x = 800
        self.card_num.element.y = 150
        self.hand_interface.display_hand()

    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.draw_button.check_click(x, y):
            self.draw_button.on_click()
        elif self.new_game_button.check_click(x, y):
            self.new_game_button.on_click()
        if self.quit_button.check_click(x, y):
            self.quit_button.on_click()

    def on_mouse_release(self, x, y, buttons, modifiers):
        if self.draw_button.check_click(x, y):
            self.draw_button.on_release()
            self.player.drawCard(1)
        elif self.new_game_button.check_click(x, y):
            self.new_game_button.on_release()
            self.reset()
        if self.quit_button.check_click(x, y):
            self.quit_button.on_release()
            exit()
        self.update()

    def reset(self):
        self.player.reset_game()
        self.remove("Hand")
        self.hand_interface = HandLayer(self.player)
        self.add(self.hand_interface, 1, "Hand")



cocos.director.director.init(c.WIN_W, c.WIN_H)
default_scene = cocos.scene.Scene(GameLayer())
cocos.director.director.run(default_scene)
