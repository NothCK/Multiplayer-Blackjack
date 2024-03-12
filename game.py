import time
from deck import Deck, Hand
from human import Dealer, Player

class Game():
    def __init__(self,names:list, bets:list,balances:list, num_of_decks:int=1,num_of_players:int=1):
        #run validations
        assert num_of_decks >= 1, f"You got to play with a minimum of 1 deck"
        assert 1<=num_of_players<= 7, f"There must be a total of 1 to 7 players in a game"

        self.num_of_decks = num_of_decks
        self.num_of_players = num_of_players
        self.deck = Deck(num_of_decks)
        self.names = names
        self.bets = bets
        self.balances = balances
        
    def setup_dealer(self):
        hand2 = self.deck.deal_cards()
        self.dealer = Dealer(hand2)
        self.dealer_hand = Hand(self.deck, hand2)

    def setup_players(self):
        self.setup_dealer()
        self.players = []
        self.players_hand = []

        for name,bet,balance in zip(self.names,self.bets,self.balances):   #insert name,bet,balance into the classes
            hand = self.deck.deal_cards()
            player = Player(name,hand,bet,balance)
            player_hand = Hand(self.deck,hand)
            self.players.append(player)
            self.players_hand.append(player_hand)
        
    
    def game_opening(self): #OPENING CARDS
        self.setup_players()
        print(f"*** {self.dealer.name} first card is ['{self.dealer.hand[0]}']")
        time.sleep(1)
        for player in self.players: 
            print(f">>> {player.name} card is", player.hand[player.name])
            time.sleep(2)

    def players_turn(self): 
        for player,player_hand in zip(self.players.copy(),self.players_hand.copy()):#use copy so the deletion wont affect the iteration
            while player_hand.count_value() < 22:
                if player_hand.count_value() == 21:
                    print(f"BLACKJACK! {player.name} WINS".center(100,'-'))
                    player.count_balance(1) 
                    print(f"{player.name} won a total of {player.bet}! {player.name} balance is now {player.balance}")
                    if len(self.players) == 1:
                        exit()
                    else:
                        self.players.remove(player)
                        self.players_hand.remove(player_hand)
                        time.sleep(3)
                    break
                    
                hit_stay = input(f">>> Does {player.name} want to hit or stay? \n").upper()
                if hit_stay == "HIT":
                    time.sleep(0.5)
                    print(">>> Here is your card", player_hand.hit())
                    time.sleep(3)
                elif hit_stay == "STAY":
                    time.sleep(1)
                    break             
            else:
                print(f"{player.name} card value is over 21, BUST!!".center(100,'-'))
                time.sleep(2)
                player.count_balance(0)
                print(f"{player.name} lost a total of {player.bet}! {player.name} balance is now {player.balance}")
                time.sleep(3)
                if len(self.players) == 1:
                        exit()
                else:
                    self.players.remove(player)
                    self.players_hand.remove(player_hand)

    def dealer_turn (self):#DEALER REVEAL AND HIT  
        self.players_turn()
        print(f"*** Okay {self.dealer.name} is opening the cards \n {self.dealer.hand}")
        time.sleep(1)
        while self.dealer_hand.count_value() < 17:
            print(f"*** {self.dealer.name} hasn't reached 17 so its going to hit! \n {self.dealer_hand.hit()}")
            print(f"*** {self.dealer.name} total value is {self.dealer_hand.count_value()}")
            time.sleep(3)

    def determine_winner(self):  #DETERMINING THE WINNERS FROM THE REMAINING PLAYERS
        self.dealer_turn()
        for player,player_hand in zip(self.players,self.players_hand):
            if self.dealer_hand.count_value() > 21:
                print(f"{self.dealer.name} BUST, {player.name} WINS".center(100,'-'))
                player.count_balance(2)
                print(f"{player.name} won a total of {player.bet}! {player.name} balance is now {player.balance}")
                time.sleep(2)
            elif player_hand.count_value() > self.dealer_hand.count_value():
                print(f"{player.name} WINS".center(100,'-'))
                player.count_balance(2)
                print(f"{player.name} won a total of {player.bet}! {player.name} balance is now {player.balance}")
                time.sleep(2)
            elif player_hand.count_value() == self.dealer_hand.count_value():
                print("TIE!".center(100,'-'))
                print(f"Due to a tie {player.name} didn't lose nor earn money!")
                time.sleep(2)
            else:
                print(f"{self.dealer.name} WINS".center(100,'-'))        
                player.count_balance(0)
                print(f"{player.name} lost a total of {player.bet}! {player.name} balance is now {player.balance}")
                time.sleep(2)
        
