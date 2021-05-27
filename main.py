# main.py
import random

print("Welcome to the game of Blackjack.")
crdNames = {1: "Ace", 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: "Jack", 12: "Queen", 13: "King"}
tLoop = True


def ranCard():
    deck = []
    for i in range(2):
        ranNum = random.randint(1, 13)
        if ranNum == 1:
            deck.append("Ace")
        elif ranNum == 11:
            deck.append("Jack")
        elif ranNum == 12:
            deck.append("Queen")
        elif ranNum == 13:
            deck.append("King")
        else:
            deck.append(ranNum)
    return (deck)


def deckSum(deck):
    deckSum = 0
    for i in range(len(deck)):
        if deck[i] == "Queen" or deck[i] == "Jack" or deck[i] == "King":
            deckSum += 10
        elif deck[i] != "Ace":
            deckSum += deck[i]
    for i in range(len(deck)):
        if deck[i] == "Ace":
            if 21 - deckSum >= 11:
                deckSum += 11
            else:
                deckSum += 1
    return (deckSum)


def appendCrd(deck):
    ranNum = random.randint(1, 13)
    if ranNum == 1:
        deck.append("Ace")
    elif ranNum == 11:
        deck.append("Jack")
    elif ranNum == 12:
        deck.append("Queen")
    elif ranNum == 13:
        deck.append("King")
    else:
        deck.append(ranNum)
    return (deck)


while tLoop:
    play = input("\nPress Enter to play or Q to quit\n")
    if play.lower() == "q":
        tLoop = False
        continue
    deck = ranCard()
    busted = False
    print("Here is your hand:")
    print(deck)
    while True:
        Hs = input("\nType in H to hit or S to stay: ")
        if Hs.lower() == "h":
            print("Here is your hand:")
            deck = appendCrd(deck)
            print(deck)
            if deckSum(deck) > 21:
                print("You busted")
                busted = True
                break
        if Hs.lower() == "s":
            break
    if busted == True:
        continue
    else:
        dDeck = ranCard()
        print("\nHere is the dealer's:")
        print(dDeck)
        while deckSum(dDeck) < 17:
            dDeck = appendCrd(dDeck)
            print("\nThe dealer hit. Here is the dealer's new hand")
            print(dDeck)
        if deckSum(dDeck) > 21:
            print("The dealer busted, you win")
        elif deckSum(dDeck) > deckSum(deck):
            print("The dealer won")
        elif deckSum(dDeck) == deckSum(deck):
            print("It's a tie")
        else:
            print("You won")