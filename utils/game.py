from .card import Deck, Card
from .player import Player
from .game_utils import GameUtils
from .config import VALUE_LIST, ICON_LIST, COLOR_LIST 
class Board:
    def __init__(self):
        self.players = [] #contain all the players that are playing.
        self.turn_count = 0 #contain the last card played by each player.
        self.active_cards = [] # contain the last card played by each player.
        self.history_cards = [] # contain all the cards played since the start of the game, except for active_cards.
    
    def add_player(self):
        utils = GameUtils()
        while True:
            number_of_players = input("🪑 Enter number of players: ")
            utils.check_quit(number_of_players)
            try:
                number_of_players_int = int(number_of_players)
                break  
            except ValueError:
                print("❌ Invalid input. Please enter whole numbers only.\n")
        self.players = [] 
        for i in range(number_of_players_int):
            player_name = input(f"Please enter player's name or ('Enter'for Player {i+1})").strip()
            utils.check_quit(player_name)
            if not player_name:
                player_name = f"Player {i+1}"
            self.players.append(player_name)
        for player in self.players:
            self.scores[player] = 0
        return self.players
    
    def card_value(self,card):
        value_icon = ICON_LIST.index(card.icon)
        value_card = VALUE_LIST.index(card.value)
        return (value_icon, value_card)
    
    def card_compare(self):
        base_power = (-1,-1)
        winner_index = -1
        for i, card in enumerate(self.active_cards):
            value = self.card_value(card)
            if value > base_power:
                base_power = value
                winner_index = i
        return winner_index
    
    def add_score(self, winner):
        self.scores[winner] += 1
        
    def end_game(self):
        winner = max(self.scores, key=self.scores.get)
        print(f"🌟====================================🌟")
        print(f"{winner} is the winner with a score of {self.scores[winner]}")
        print(f"🌟====================================🌟")
    
    def start_game(self):
        deck = Deck()
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
            winner_index = self.card_compare()
            winner_player = self.players[winner_index]
            self.add_score(winner_player)

            print(f"✨ Active card: {", ".join(str(card) for card in self.active_cards)}")
            print(f"🏆 Winner of turn {self.turn_count}: '{winner_player}' with card {self.active_cards[winner_index]}")
            print(f"🌟========= End of turn : {self.turn_count} =========🌟")
        self.end_game()
        
  

    
    
                
                
    
        
            
            
                


       
        