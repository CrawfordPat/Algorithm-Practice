import cardSimFunctions as csf

def main():
    numOfCards = int(input("How many cards do you want in the deck: "))
    deck = csf.pickCards(numOfCards)

    numOfLoops = int(input("How many times do you want to stack the columns: "))
    finalPos = (numOfCards // 3) + 4

    for i in range(numOfLoops):
        deck = cardLoop(deck)
        print("\n")

    userCard = str(input("Is your card the " + str(deck[finalPos]) + " (y/n): "))

    if userCard == "y":
        print("Great!")
    else:
        print("Shoot!")

def cardLoop(deck):
    col1, col2, col3 = csf.makeColumns(deck)
    csf.printColumns(deck)

    whichColumn = int(input("Which column is your card in: "))
    if whichColumn == 1:
        stack = csf.stack(col2, col1, col3)
    elif whichColumn == 2:
        stack = csf.stack(col3, col2, col1)
    elif whichColumn == 3:
        stack = csf.stack(col1, col3, col2)
    else:
        print("Invalid input")
        return
    
    return stack

main()