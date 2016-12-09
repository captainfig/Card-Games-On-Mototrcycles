'''
This file is designed to handle all db access
'''

import sqlite3, constants as C

con = sqlite3.connect('cards.db')
s = con.cursor()

# Game commands

def getCard(cardID):
	query = s.execute("SELECT * FROM {table} WHERE {idf}={my_id}".
		format(table="cards", idf='ID', my_id=cardID))
	return list(s.fetchone())

# Admin commands

def createCard(id, name, flavor, type, effect1, effect2, effect3):
    card = (id, name, flavor, type, effect1, effect2, effect3)
    c.execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?)", card)