import random 
class Deck():
    def __init__(self,num_decks:int):
        hearts = ["HEART ACE", "HEART 2", "HEART 3", "HEART 4", "HEART 5","HEART 6","HEART 7","HEART 8","HEART 9","HEART 10","HEART JACK", "HEART QUEEN", "HEART KING"]
        spades = ["SPADE ACE", "SPADE 2", "SPADE 3", "SPADE 4", "SPADE 5","SPADE 6","SPADE 7","SPADE 8","SPADE 9","SPADE 10","SPADE JACK", "SPADE QUEEN", "SPADE KING"]
        clubs = ["CLUB ACE", "CLUB 2", "CLUB 3", "CLUB 4", "CLUB 5","CLUB 6","CLUB 7","CLUB 8","CLUB 9","CLUB 10","CLUB JACK", "CLUB QUEEN", "CLUB KING"]
        diamonds = ["DIAMOND ACE", "DIAMOND 2", "DIAMOND 3", "DIAMOND 4", "DIAMOND 5","DIAMOND 6","DIAMOND 7","DIAMOND 8","DIAMOND 9","DIAMOND 10","DIAMOND JACK", "DIAMOND QUEEN", "DIAMOND KING"]
        decks = (hearts+spades+clubs+diamonds)*num_decks
        self.decks = decks
        self.shuffled = decks[:] #make a copy
        self.hand = []
        self.card_value = 0
    
    def __repr__(self) -> str:
        return f"{self.decks}"

    def __shuffle_cards(self):
        random.shuffle(self.shuffled)
    
    def deal_cards(self):
        self.__shuffle_cards()
        self.hand = self.shuffled[0:2]
        self.shuffled = self.shuffled[2:]
        return self.hand

class Hand():
    def __init__ (self,deck, hand:list):
        self.deck = deck
        self.hand = hand
        self.card_value = 0

    def count_value(self):
        #to count the value of each card
        self.card_value = 0
        for card in self.hand:
            valued = card.split()[1]
            if valued in ["JACK","QUEEN","KING",]:
                value = 10
            elif valued == "ACE":
                value = 11
            else:
                value = int(valued)
            self.card_value += value
        #to change ACE into 1 if total over 21
        for card in self.hand:
            if self.card_value > 21 and card.split()[1] == "ACE":
                self.card_value -= 10
        return self.card_value

    def hit(self):
        new_card = self.deck.shuffled[0:1]
        for hand in new_card:
            self.hand.append(hand)
            self.deck.shuffled.remove(hand)
        return self.hand

        


        


