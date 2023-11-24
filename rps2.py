import sys
import random
from enum import Enum
# value = input("Please enter a value:\n")
# print(value)

class RPS(Enum):
    ROCK = 1
    BTS = 2
    BLACKPINK = 3
    
playagain = True
while playagain:
    playerchoice =  input("Enter...\n1. for Rock. \n2. for BTS. \n3. for Blackpink. \nEnter number here:")
    player = int(playerchoice)

    if player < 1 | player > 3:
        sys.exit("You must enter 1, 2, or 3!.")
    
    computerchoice = random.choice("123")
    computer = int(computerchoice)


    print("\nYou choose " + str(RPS(player)).replace('RPS.','') + ".")
    print("\nComputer choose " + str(RPS(computer)).replace('RPS.','') + ".")


    if player > computer:
        print("You win!".center(30,'+'))
    elif player < computer:
        print("Computer wins!".center(30, '-'))
    else:
        print("Tie game!".center(30,'='))
        
    playagain = input("\nPlay Again! \nY for Yes! N for No!\nType Y or N here:")
    if playagain.lower() == "y":
        continue
    else:
        print("Thank you for playing!")
        playagain = False
sys.exit("Bye! See you again!")