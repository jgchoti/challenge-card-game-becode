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
        num_cards = len(self.cards)
        print(f"🚀 {self.name} has {self.cards}")
        if len(self.cards) > 1:
            try: 
                user_response = int(input(f"Enter number of card you want to select? [1 - {num_cards}]: "))
                if not (1<=user_response<=num_cards):
                    user_response = random.randint(1, num_cards)
                    print("❌ Invalid input. the card will be choose randomly")
            except:
                user_response = random.randint(1, num_cards)
                print("❌ Invalid input. the card will be choose randomly")
            selected_card = self.cards[user_response -1] 
        elif len(self.cards) == 1:
            selected_card = self.cards[0] 
        else:
            print("❌ no card left")
            
        
        self.history.append(selected_card)
        self.cards.remove(selected_card)
        print(f"{self.name} (turn {self.turn_count}) played: {selected_card}.")
        return selected_card
    
   
