import sys
import random
from enum import Enum

def rps(name="Player"):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal name
        class RPS(Enum):
            ROCK = 1
            BTS = 2
            BLACKPINK = 3
            
        playerchoice =  input(f"\n{name}, please enter...\n1. for Rock. \n2. for BTS. \n3. for Blackpink. \nEnter number here:")
        if(playerchoice not in ["1", "2", "3"]):
            print(f"{name}, you must enter 1, 2, or 3!.")
            return play_rps()
        player = int(playerchoice)
        
        computerchoice = random.choice("123")
        computer = int(computerchoice)


        print(f"\n{name}, you choose {str(RPS(player)).replace('RPS.','').title()}.")
        print(f"Computer choose {str(RPS(computer)).replace('RPS.','').title()}.\n")

        def rules(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            if player > computer:
                player_wins += 1
                return f"{name}, you win!".center(30,'+')
            elif player < computer:
                computer_wins += 1
                return "Computer wins!".center(30, '-')
            else:
                return "Tie game!".center(30,'=')
        
        game_result = rules(player, computer)
        print(game_result)
        
        nonlocal game_count
        game_count +=1
        
        print(f"\nGame count: {game_count}")
        print(f"\n{name} wins: {player_wins}")
        print(f"\nComputer wins: {computer_wins}")
        print(f"\nPlay Again?, {name}")
        
        while True:
            playagain = input("\nY for Yes! N for No!\nType Y or N here:")
            if playagain.lower() not in ["y","n"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print(f"Thank you {name} for playing!")
            sys.exit("Bye! See you again!")

    play_rps()
    


if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience!"
    )

    parser.add_argument(
        "-n","--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()
    
    play_rps_calling = rps(args.name)
    play_rps_calling()