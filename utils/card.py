# In card.py:

# Create a class called Symbol with two attributes:

# color which is a string.
# icon which is a single character out of this list [♥, ♦, ♣, ♠].
# 1.2 Card
# In the same file, create a class Card that inherits from Symbol and add an attribute:

# value which is a string (one of ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K'])


# 3. A complete deck
# Create a Deck class that contains:

# An attribute cards which is going to contain a list of instances of Card.
# A fill_deck() method that will fill cards with a complete card game (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [♥, ♦, ♣, ♠]). Your deck should contain 52 cards at the end.
# A shuffle() method that will shuffle all the list of cards.
# A distribute() that will take a list of Player as parameter and will distribute the cards evenly between all the players.
