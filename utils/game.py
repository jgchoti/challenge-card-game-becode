from .card import Deck
from .player import Player
from .config import VALUE_LIST, ICON_LIST, COLOR_LIST 
class Board:
    def __init__(self, players : list[str], turn_count: int, active_cards: list, history_cards:list):
        self.players = players #contain all the players that are playing.
        self.turn_count = turn_count #contain the last card played by each player.
        self.active_cards = active_cards # contain the last card played by each player.
        self.history_cards = history_cards # contain all the cards played since the start of the game, except for active_cards.
    
    def add_player(self):
        while True:
            try:
                number_of_players = int(input("🪑 Enter number of players: "))
                break  
            except ValueError:
                print("❌ Invalid input. Please enter whole numbers only.\n")
        self.players = [] 
        for i in range(number_of_players):
            player_name = input(f"Please enter player's name or ('Enter'for Player {i+1})").lower().strip()
            if not player_name:
                player_name = f"Player {i+1}"
            self.players.append(player_name)
        return self.players
    
    def start_game(self):
        deck = Deck(COLOR_LIST, ICON_LIST, VALUE_LIST )
        print(f"\n▶️ Start the game...\n")
        # Fill a Deck
        deck.fill_deck()
        # Distribute the cards of the Deck to the players.
        player_distribute = deck.distribute(self.players)
        # Make each Player play() a Card, where each player should only play 1 card per turn,
        
        print(f"🚀 Welcome!", ", ".join(self.players ))
        print(f"🌟===================================🌟")
        for i in range(len(player_distribute[self.players[0]])):
            self.active_cards = []
            if self.turn_count != 0:
                print(f"🗑️ Number of cards already played in previous rounds: {len(self.history_cards)}")
            for player in self.players:
                player = Player(player, player_distribute [player], self.turn_count + 1)
                card = player.play()
                self.active_cards.append(card)
                self.history_cards.append(card)
                
            self.turn_count += 1
            print(f"✨ Active card: {self.active_cards}")
            print(f"🌟========= End of turn : {self.turn_count} =========🌟")  
            
                    
                
                
                
    
        
            
            
                


       
        