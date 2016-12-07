''''
This file is designed to handle all db access
''''

import sqlite3, constants as C

con = sqlite3.connect('cards.db')
c = con.cursor()

# Game commands

def printHand(hand):
    for i in range(C.HAND_SIZE): # Get actual entries from db
        handCards = c.execute("SELECT * FROM {table} WHERE {idf}={my_id}".\
                              format(table="cards", idf='id', my_id=hand[i]))
        print(c.fetchall())


# Admin commands

def createCard(id, name, flavor, type, effect1, effect2, effect3):
    card = (id, name, flavor, type, effect1, effect2, effect3)
    c. execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?)", card)