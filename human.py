class Participants():
    def __init__(self,name:str,balance:int):
        self.name = name
        self.balance = balance

class Player(Participants):
    def __init__(self, name:str, hand:list, bet: int=50,balance:int=50):
        super().__init__(
            name, balance
        )
        #run validations
        assert 50 <=bet<= 1000, f"You can't bet below 50 or bet over 1000"
        assert balance >= bet, f"You can't go betting with a balance of {balance}"

        self.bet = bet
        self.hand= {self.name:hand}  #to get every player their own hand

    def count_balance(self,win):
        win_conditions = {1:0.5,2:1,0:-1} #win condition and gain/loss dictionary
        self.bet = self.bet * win_conditions[win] #earnings from the bet
        self.balance += self.bet
        return self.bet, self.balance

class Dealer(Participants): #inherit just in case I want to make the dealer not automated
    def __init__(self, hand:list=None):
        self.name = "Robot Dealer"
        self.hand = hand
    