import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        if rank == "J" or rank == "Q" or rank == "K":
           self.value = 10
        elif rank == "Ace":
            self.value = 11
        else:
            self.value = int(rank)

    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank

    def __str__(self):
        return self.rank + ' ' + self.suit
        
class Deck:

    def __init__(self):
        
        self.card_suit = ["(Hearts)", "(Diamonds)", "(Spades)", "(Clubs)"]
        self.card_rank = ["Ace", "2", "3", "4", "5", "6", "7", "8",
                          "9", "10", "J", "Q", "K"]
        self.deck = []

        for s in self.card_suit:
            for r in self.card_rank:
                self.deck.append(Card(s, r))
                
        random.shuffle(self.deck)

    def get_card(self):
        return self.deck.pop(random.randint(0, len(self.deck) - 1))

    def __str__(self):
        return self.deck.pop()
    
