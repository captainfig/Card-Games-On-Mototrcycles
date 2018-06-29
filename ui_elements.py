import cocos
import constants as c


class TextBox(cocos.cocosnode.CocosNode):
    def __init__(self, text, size, x=0, y=0, color=c.BLACK, anchor_x='center', anchor_y='center'):
        super(TextBox, self).__init__()
        self.label = cocos.text.Label(text=text,
                                      font_name=c.F_TIMES,
                                      font_size=size,
                                      color=color,
                                      anchor_x=anchor_x, anchor_y=anchor_y)
        self.position = (x, y)
        self.add(self.label)

    def change_text(self, text):
        self.label.element.text = text


class GameCounter(TextBox):
    def __init__(self, text, to_count, x, y):
        self.to_count = to_count
        self.text = text
        super(GameCounter, self).__init__(self.text + ' ' + str(len(self.to_count)), 18, x, y)

    def update(self):
        self.change_text(self.text + ' ' + str(len(self.to_count)))


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
        self.text = TextBox(text, 14, 0, 0, c.WHITE)
        self.add(cocos.sprite.Sprite("resources/button_1.png"), 0, "Background")
        self.add(cocos.sprite.Sprite("resources/button_1_p.png"), 1, "Press")
        self.get("Press").visible = False
        self.add(self.text, 2)

    def on_click(self):
        self.get("Press").visible = True

    def on_release(self):
        self.get("Press").visible = False


# Graphic for card text
class CardBlock(cocos.cocosnode.CocosNode):
    def __init__(self, x, y, w, h):
        super(CardBlock, self).__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h


# Create card image
class CardSprite(cocos.sprite.Sprite):
    def __init__(self, card):
        super(CardSprite, self).__init__("resources/cardtemp.png", anchor=(0, 0))
        card_name = TextBox(card['name'], 14, 11, 253, anchor_x='left', anchor_y='top')
        card_attack = TextBox(card['attack'], 12, 130, 50, anchor_x='left', anchor_y='top')
        card_defense = TextBox(card['defense'], 12, 130, 30, anchor_x='left', anchor_y='top')
        card_image = cocos.sprite.Sprite(card['image'], anchor=(0, 0))

        # card_name.position = (11, 253)
        # card_attack.position = (130, 50)
        # card_defense.position = (130, 30)
        card_image.position = (c.IMG_LEFT, c.IMG_BOTTOM)

        self.add(card_name)
        self.add(card_attack, 2)
        self.add(card_defense, 2)
        self.add(card_image)
