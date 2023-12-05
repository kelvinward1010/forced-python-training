import sys
from rps import rps
from guess_number import guess_game


def play_game(name="Player"):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back the Menu")
        
        playerchoice = input(
            "\nPlease choose a game to play: \n1 = Guess Number\n2 = RPS game\nOr press \"x\" tp exit the menu.\n"
        )
        
        
        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name} please enter 1, 2, or x.")
            return play_game(name)
        
        welcome_back = True
        
        if playerchoice == "1":
            guess_play = guess_game(name)
            guess_play()
        elif playerchoice == "2":
            rps_play = rps(name)
            rps_play()
        else:
            print("\n{name} See you next time")
            sys.exit(f"Bye {name}!")


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
    
    print(f"\n{args.name}, welcome to the menu")
    play_game(args.name)