# 2. A bunch of players
# In player.py create a class Player that contains these attributes:

# cards which is a list of Card. (you will need to import Card from card.py). In a real card game, this is equivalent to the cards that the player has in his hands.
# turn_count which is an int starting a 0.
# number_of_cards which is an int starting at 0.
# history which is a list of Card that will contain all the cards played by the player.
# And some methods:

# play() that will:
# randomly pick a Card in cards.
# Add the Card to the Player's history.
# Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
# Return the Card.
import random
class Player:
    def __init__(self, name: str = "", cards=None,turn_count: int = 1, number_of_cards: int = 0, history=None):
        if cards is None:
            cards = []
        if history is None:
            history = []
        self.name = name
        self.cards = cards
        self.number_of_cards = number_of_cards
        self.turn_count = turn_count
        self.history = history
        
    def play(self):
        selected_card = random.choice(self.cards) # randomly pick a Card in cards.
        self.cards.remove(selected_card)
        print(f"{self.name} (turn {self.turn_count}) played: {selected_card}.")
        return selected_card, self.cards, self.turn_count
    
