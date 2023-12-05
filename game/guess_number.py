import sys
import random

def guess_game(name="Player"):
    game_count = 0
    player_wins = 0

    def guess_number():
        nonlocal name
            
        playerchoice =  input(f"\n{name}, guess which number I'm thinking of [1,2,3]. \nEnter number here:")
        if(playerchoice not in ["1", "2", "3"]):
            print(f"{name}, you must enter 1, 2, or 3!.")
            return guess_number()
        player = int(playerchoice)
        
        computerchoice = random.choice("123")
        computer = int(computerchoice)


        print(f"\n{name}, you choose {str(player)}.")
        print(f"I was thinking about number: {str(computer)}.\n")

        def rules(player, computer):
            nonlocal name
            nonlocal player_wins
            if player == computer:
                player_wins += 1
                return f"{name}, you win!".center(30,'+')
            else:
                return f"Sorry, {name}. Better luck next time!".center(30,'-')
        
        game_result = rules(player, computer)
        print(game_result)
        
        nonlocal game_count
        game_count +=1
        
        print(f"\nGame count: {game_count}")
        print(f"\n{name} wins: {player_wins}")
        print(f"\n{name} winning percentage: {player_wins/game_count:.2%}")
        print(f"\nPlay Again?, {name}")
        
        while True:
            playagain = input("\nY for Yes! N for No!\nType Y or N here:")
            if playagain.lower() not in ["y","n"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return guess_number()
        else:
            print(f"Thank you {name} for playing!")
            if __name__ == "__main__":
                sys.exit("Bye! See you again!")
            else:
                return

    guess_number()
    


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
    
    play_guess_number = guess_game(args.name)
    play_guess_number()