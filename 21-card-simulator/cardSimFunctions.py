import random

# Array of all cards in the deck
cardDeck = ["AS", "KS", "QS", "JS", "TS", "9S", "8S", "7S", "6S", "5S", "4S", "3S", "2S", "AH", "KH", "QH", "JH", "TH", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H", "AC", "KC", "QC", "JC", "TC", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C", "AD", "KD", "QD", "JD", "TD", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D"]

# Pick 21 random, non duplicate cards from the deck
def pickCards(num):
    cards = []
    while len(cards) < num:
        card = cardDeck[random.randint(0, len(cardDeck)-1)]
        if card not in cards:
            cards.append(card)
    return cards


def makeColumns(deck):
    col1 = []
    col2 = []
    col3 = []

    for i in range(0, len(deck)):
        if i % 3 == 0:
            col1.append(deck[i])
        elif i % 3 == 1:
            col2.append(deck[i])
        elif i % 3 == 2:
            col3.append(deck[i])

    return col1, col2, col3

def printColumns(deck):
    col1, col2, col3 = makeColumns(deck)
    for i in range(len(col1)):
        print(col1[i], col2[i], col3[i])


def stack(bottom, middle, top):
    stack = []
    stack.extend(top)
    stack.extend(middle)
    stack.extend(bottom)
    return stack