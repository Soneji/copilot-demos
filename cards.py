#!/usr/bin/env python3
# make a list of all 52 cards with "10" for ten
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
# make a list of the suits
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
# make a list of the cards
deck = []
# make a list of the cards
for suit in suits:
    for card in cards:
        deck.append(str(card) + " of " + suit)

# shuffle the deck
import random
random.shuffle(deck)

print(deck)

# ask how many people are playing
num_players = int(input("How many people are playing? "))
# make a list of players
players = []
# add player name object to the list 
for i in range(num_players):
    players.append({"name": input("What is the name of player " + str(i + 1) + "? "), "hand": []})
    

print(players)


# deal 7 unique cards to each player
for i in range(7):
    for player in players:
        player["hand"].append(deck.pop())

# print the hands
for player in players:
    print(player["name"] + "'s hand: " + str(player["hand"]))

# cards = [r+s for r in '23456789TJQKA' for s in 'SHDC']
# print(cards)
