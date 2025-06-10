import random
from typing import List
from .config import VALUE_LIST, ICON_LIST, COLOR_LIST 

class Symbol:
    def __init__(self, color: str, icon: str):
        self.color = color
        self.icon = icon

    def __str__(self):
        return f"symbol {self.color} {self.icon}"
     
class Card(Symbol):    
    def __init__(self, color: str, icon, value: str):
        super().__init__(color, icon)
        self.value = value
        self.card = [icon, color, value]
    def __str__(self):
        return f"{self.card}"
    def __repr__(self):
        return self.__str__()

# An attribute cards which is going to contain a list of instances of Card.
# A fill_deck() method that will fill cards with a complete card game (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [♥, ♦, ♣, ♠]). Your deck should contain 52 cards at the end.
# A shuffle() method that will shuffle all the list of cards.
# A distribute() that will take a list of Player as parameter and will distribute the cards evenly between all the players.
class Deck():
    def __init__(self):
        self.cards = [] 
    
    def fill_deck(self):
        deck = []
        for icon in ICON_LIST:
            for value in VALUE_LIST:
                if icon == "♥" or icon == "♦":
                    color = COLOR_LIST[0]
                else:
                    color = COLOR_LIST[1]
                deck.append(Card(color, icon, value))
        self.cards = deck
        return deck
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    
    def distribute(self, list_players):
        self.shuffle()
        number_player = len(list_players)
        num_card_per_player = len(self.cards) // number_player
        players_with_card = {}
        for i, player in enumerate(list_players):
            start = i * num_card_per_player
            end = start + num_card_per_player
            players_with_card[player] = self.cards[start:end]
        num_undistributed_cards = len(self.cards) % number_player
        undistributed_cards = self.cards[-num_undistributed_cards:]
        if num_undistributed_cards != 0:
            print(f"‼️ There is {num_undistributed_cards} cards left on the table : {undistributed_cards}")
       
        return players_with_card
    

