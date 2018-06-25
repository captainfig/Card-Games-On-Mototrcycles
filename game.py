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


class CardSprite(cocos.sprite.Sprite):
    def __init__(self, card):
        super(CardSprite, self).__init__("cards/cardtemp.png", anchor=(0, 0))
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


class MenuLayer(cocos.menu.Menu):

    is_event_handler = True

    def __init__(self, _player):
        super(MenuLayer, self).__init__("Game Menu")
        self.items = [cocos.menu.MenuItem('Draw Card', self.draw_card),
                      cocos.menu.MenuItem('New Hand', self.new_game),
                      cocos.menu.MenuItem('Exit', self.on_quit)]
        self.create_menu(self.items)
        self.position = (200, 0)
        self.player = _player

    def draw_card(self):
        self.player.drawCard(1)

    def new_game(self):
        self.player.reset_hand()
        self.player.reset_deck()
        self.player.startGame()

    def on_quit(self):
        exit()


class GameLayer(cocos.layer.Layer):
    def __init__(self, _player):
        super(GameLayer, self).__init__()
        self.position = (0, 0)
        self.player = _player
        self.add(BackgroundLayer(), 0, "Background")

    def update(self):
        self.get("Hand").display_hand()

    def on_mouse_release(self, x, y, buttons, modifiers):
        self.update()


player = player.Player("Yugi", c.DEFAULT_DECK)  # Pass list of card IDs for Deck object to turn into Cards

cocos.director.director.init(1600, 900)
default_scene = cocos.scene.Scene(GameLayer(player), MenuLayer(player))
cocos.director.director.run(default_scene)
