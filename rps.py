import sys
import random
from enum import Enum
# value = input("Please enter a value:\n")
# print(value)

class RPS(Enum):
    ROCK = 1
    BTS = 2
    BLACKPINK = 3
    
print(RPS(2))
print(RPS.ROCK)
print(RPS['ROCK'])
print(RPS.BTS.value)
# sys.exit()

print("")
playerchoice =  input("Enter...\n1. for Rock. \n2. for BTS. \n3. for Blackpink. \nEnter number here:")
player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, or 3!.")
computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You choose " + str(RPS(player)).replace('RPS.','') + ".")
print("Computer choose " + str(RPS(computer)).replace('RPS.','') + ".")
print("")

if player > computer:
    print("You win!".center(30,'+'))
elif player < computer:
    print("Computer wins!".center(30, '-'))
else:
    print("Tie game!".center(30,'='))