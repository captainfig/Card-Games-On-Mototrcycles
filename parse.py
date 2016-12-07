'''
This file is designed to handle all db access
'''

import sqlite3, constants as C

con = sqlite3.connect('cards.db')
s = con.cursor()

# Game commands

def printHand(hand):
    for i in range(C.HAND_SIZE): # Get actual entries from db
        handCards = s.execute("SELECT {name} FROM {table} WHERE {idf}={my_id}".\
                              format(name="NAME" table="cards", idf='ID', my_id=hand[i]))
        print(s.fetchall())

def printField(field):
	for i in range(len(field)): # Get actual entries from db
        fieldCards = s.execute("SELECT {name} FROM {table} WHERE {idf}={my_id}".\
                              format(name="NAME" table="cards", idf='ID', my_id=field[i]))
        print(s.fetchall())
# Admin commands

def createCard(id, name, flavor, type, effect1, effect2, effect3):
    card = (id, name, flavor, type, effect1, effect2, effect3)
    c.execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?)", card)