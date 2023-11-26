

def parent_function(person, coins):
    #coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else: 
            print("\n" + person + " is out of coins.")
    return play_game

kelvin = parent_function("Kelvin", 5)
ward = parent_function("Ward", 3)

kelvin()
ward()
ward()
ward()