import sqlite3
conn = sqlite3.connect('cards.db')
c = conn.cursor()

def createCard(id, name, flavor, type, effect1, effect2, effect3):
    card = (id, name, flavor, type, effect1, effect2, effect3)
    c. execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?)", card)

