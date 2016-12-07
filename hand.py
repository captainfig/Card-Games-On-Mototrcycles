import pygame, sqlite3, random

deck=[1,2,3,4,5,6,7,8,9,10]
handSize = 3

con = sqlite3.connect('cards.db')
c = con.cursor()

def drawHand(deck):
    hand = random.sample(deck, handSize)
    for i in range(handSize):
        handCards = c.execute("SELECT * FROM {table} WHERE {idf}={my_id}".\
                              format(table="cards", idf='id', my_id=hand[i]))
        print(c.fetchall())
