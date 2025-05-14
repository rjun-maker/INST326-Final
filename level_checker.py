# Aiden Anderson's function
# algorithm that checks the level the player is at, if player can sustain level,
# they win
# what's needed:
# - way to check level
# - way to check how long the player has been at a certain level
# - way to associate staying at the level with winning the game


# checks level, 5 rounds = 1 level, will move on to next level
# the win condition is level 10 for 5 rounds

class LevelChecker:
    """
    Represents a player and tracks level progress and if they've won the game
    """

    def __init__(self):
        """
        Initializes the player with starting values
        """
        self.current_level = 1
        self.previous_level = 1
        self.same_level_rounds = 1

    def level_checker(self):
        """
        Updates how many rounds the player has stayed at the same level
        """
        if self.current_level == self.previous_level:
            self.same_level_rounds += 1
        else:
            self.same_level_rounds = 1

    def win_condition(self):
        """
        Checks if the player has won by staying at level 10 for 5 rounds

        Returns:
            bool: Returns true if the player is at level 10 and has stayed 
            for 5 rounds
        """
        return self.current_level == 10 and self.same_level_rounds >= 5

    def update_level(self, new_level):
        """
        Updates the current level and checks how long the player has stayed at 
        that level

        Args:
            new_level (int): The level for this round.
        """
        if new_level == self.current_level:
            self.same_level_rounds += 1
        else:
            self.same_level_rounds = 1
        self.current_level = new_level

    def __str__(self):
        return f"Level {self.current_level}, Rounds at current level: {self.same_level_rounds}"
    