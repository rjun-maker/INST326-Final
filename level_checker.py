# Aiden Anderson's function
# algorithm that checks the level the player is at, if player can sustain level,
# they win
# what's needed:
# - way to check level
# - way to check how long the player has been at a certain level
# - way to associate staying at the level with winning the game


# checks level, 5 rounds = 1 level, will move on to next level
# win condition is level 10 for 5 rounds

def level_checker(current_level, previous_level, same_level_rounds):
    """Tracks how many rounds a person have been at a particular level
    
    Args:
        current_level (int): current level of the player
        previous_level (int): level of the player in the former round
        same_level_rounds (int): how many rounds the player has done at their
        current level
    
    Returns:
        int: update count of rounds at player's current level
    """
    
    if current_level == previous_level:
        same_level_rounds += 1
    else:
        # if the level has changed, will go back to one
        same_level_rounds = 1

    return same_level_rounds


def win_condition(current_level, duration):
    """determines in player wins by staying at max level for 5 rounds
    
    Args:
        current_level (int): player's current level
        same_level_rounds (int): how many rounds the player has stayed at the
        current level
    
    Returns
        bool: Returns true if player is  at level 10 for 5 rounds
    """
    return current_level == 10 and duration >= 5

print(level_checker(2, 2, 5))

WIN_GOAL = 5
duration = 4

if win_condition(duration, WIN_GOAL):
    print("You win")
    