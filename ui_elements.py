import cocos
import constants as c


# An invisible button
class GameButton(cocos.cocosnode.CocosNode):
    def __init__(self, x, y, w, h):
        super(GameButton, self).__init__()
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.top_left = self.x - (self.width / 2), self.y + (self.height / 2)
        self.top_right = self.x + (self.width / 2), self.y + (self.height / 2)
        self.bot_left = self.x - (self.width / 2), self.y - (self.height / 2)
        self.bot_right = self.x + (self.width / 2), self.y - (self.height / 2)

    def on_click(self):
        pass

    def on_release(self):
        pass

    def check_click(self, x, y):
        if x > self.top_left[0] and y < self.top_left[1]:
            if x < self.bot_right[0] and y > self.bot_right[1]:
                return True
        return False

    def get_top_left(self):
        return self.top_left

    def get_bot_right(self):
        return self.bot_right


# A menu button based on GameButton
class MenuButton(GameButton):
    def __init__(self, text, x, y):
        super(MenuButton, self).__init__(x, y, 150, 50)
        self.label = cocos.text.Label(text=text,
                                      font_name='Times New Roman',
                                      font_size=14,
                                      anchor_x='center', anchor_y='center')
        self.add(cocos.sprite.Sprite("resources/button_1.png"), 0, "Background")
        self.add(cocos.sprite.Sprite("resources/button_1_p.png"), 1, "Press")
        self.get("Press").visible = False
        self.add(self.label, 2)

    def on_click(self):
        self.get("Press").visible = True

    def on_release(self):
        self.get("Press").visible = False


# Create card image
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