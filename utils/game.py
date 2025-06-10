from .card import Deck
from .player import Player
from .config import VALUE_LIST, ICON_LIST, COLOR_LIST 
players_list = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

class Board:
    def __init__(self, players : list[str], turn_count: int, active_cards: list, history_cards:list):
        self.players = players #contain all the players that are playing.
        self.turn_count = turn_count #contain the last card played by each player.
        self.active_cards = active_cards # contain the last card played by each player.
        self.history_cards = history_cards # contain all the cards played since the start of the game, except for active_cards.
    
    def start_game(self):
        deck = Deck(COLOR_LIST, ICON_LIST, VALUE_LIST )
        print("▶️ Start the game...")
        # Fill a Deck
        deck.fill_deck()
        # Distribute the cards of the Deck to the players.
        player_distribute = deck.distribute(self.players)
        # Make each Player play() a Card, where each player should only play 1 card per turn, 
        print(f"🚀 Welcome!", ", ".join(players_list))
        for i in range(len(player_distribute[players_list[0]])):
            self.active_cards = []
            if self.turn_count != 0:
                print(f"🗑️ Number of cards already played in previous rounds: {len(self.history_cards)}")
            for player in players_list:
                player = Player(player, player_distribute [player], self.turn_count + 1)
                card = player.play()
                self.active_cards.append(card[0])
                self.history_cards.append(card[0])
                
            self.turn_count += 1
            print(f"✨ Active card: {self.active_cards}")
            print(f"🌟========= End of turn : {self.turn_count} =========🌟")  
            
            
                


       
        