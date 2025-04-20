# Aiden Anderson's function
# algorithm that checks the level the player is at, if player can sustain level,
# they win
# what's needed:
# - way to check level
# - way to check how long the eplayer has been at a certain level
# - way to associate staying at the level with winning the game

def level_checker(current_level, previous_level, same_level_rounds):
    """Tracks how many rounds a person have been at a particular level
    """
    
    if current_level == previous_level:
        same_level_rounds += 1
    else:
        # if the level has changed, will go back to one
        same_level_rounds = 1

    return same_level_rounds


print(level_checker(2, 2, 5))