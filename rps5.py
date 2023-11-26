import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():

        class RPS(Enum):
            ROCK = 1
            BTS = 2
            BLACKPINK = 3
            
        playerchoice =  input("Enter...\n1. for Rock. \n2. for BTS. \n3. for Blackpink. \nEnter number here:")
        if(playerchoice not in ["1", "2", "3"]):
            print("You must enter 1, 2, or 3!.")
            return play_rps()
        player = int(playerchoice)
        
        computerchoice = random.choice("123")
        computer = int(computerchoice)


        print("\nYou choose " + str(RPS(player)).replace('RPS.','').title() + ".")
        print("\nComputer choose " + str(RPS(computer)).replace('RPS.','').title() + ".")

        def rules(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            if player > computer:
                player_wins += 1
                return "You win!".center(30,'+')
            elif player < computer:
                computer_wins += 1
                return "Computer wins!".center(30, '-')
            else:
                return "Tie game!".center(30,'=')
        
        game_result = rules(player, computer)
        print(game_result)
        
        nonlocal game_count
        game_count +=1
        
        print("\nGame count: " + str(game_count))
        print("\nPlayer Wins: " + str(player_wins))
        print("\nComputer Wins: " + str(computer_wins))
        print("\nPlay Again?")
        
        while True:
            playagain = input("\nY for Yes! N for No!\nType Y or N here:")
            if playagain.lower() not in ["y","n"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("Thank you for playing!")
            sys.exit("Bye! See you again!")

    play_rps()
    
rps()