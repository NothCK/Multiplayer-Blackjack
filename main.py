import time
from game import Game

play = input("Do you want to play?(Y/N)\n").upper()
if play in ["Y","YES"]:
    #Input necessary attributes
    while True:
        try:
            num_of_decks = int(input("How many decks you want to use? (minimum of 1): \n "))
            break
        except:
            print("### Please insert the appropriate numbers ###")
    num_of_players = int(input("How Many Players? (1-7): "))
    time.sleep(0.5)
    if 1<=num_of_players<=7:
        bets = []
        balances = []
        player_names = []
        check_names = set() #used to check if the name is unique or not
        for _ in range (1,num_of_players+1):     
            print(f"### Player {_}".upper())
            #ensure unique names for every player
            while True:
                name = input("Enter player name: ").capitalize()
                if name not in check_names:
                    check_names.add(name)
                    player_names.append(name)
                    break
                else:
                    print("*** Name already exists. Please enter a different name.")
            #insert player's balance and bet
            try:
                bet = int(input("Place Bet (minimal 50$ / max 1000$):"))
                bets.append(bet)
                balance = int(input("Balance :"))
                balances.append(balance)
            except ValueError as e:
                print("Numbers only", e)
                exit()
        time.sleep(1)
    else:
        raise Exception("The Number of Players is incorrect")

    #Input all the information to the Game Class 
    game = Game(player_names,bets,balances,num_of_decks,num_of_players)

    print("THE GAME NOW STARTS".center(100,'-'))
    time.sleep(1)
    game.game_opening()
    game.determine_winner()
    

elif play in ["N","NO"]:
    print("Okay, have a great day")
    exit()
else:
    raise Exception("Y or N ???")


