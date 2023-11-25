import sys
import random
from enum import Enum

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


    if player > computer:
        print("You win!".center(30,'+'))
    elif player < computer:
        print("Computer wins!".center(30, '-'))
    else:
        print("Tie game!".center(30,'='))
    
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