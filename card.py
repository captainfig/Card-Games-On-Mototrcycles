import constants as c


class Card():
    def __init__(self, cardInfo):
        self.id = int(cardInfo[c.CARD_ID])
        self.name = cardInfo[c.CARD_NAME]
        self.image = cardInfo[c.CARD_IMAGE]
        self.card_type = cardInfo[c.CARD_TYPE]
        self.attribute = cardInfo[c.ATTRIBUTE]
        self.attack = cardInfo[c.ATK]
        self.defense = cardInfo[c.DEF]
        self.EFFECT = cardInfo[c.EFFECT]

    def __str__(self):
        return {'name': self.name,
                'image': self.image,
                'card type': self.card_type,
                'attribute': self.attribute,
                'attack': self.attack,
                'defense': self.defense}
