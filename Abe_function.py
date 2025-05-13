# #My function is called status_check(). What is does is check the status of 
# #player's budget and satisfaction score. If the budget ever goes below 0 or 
# #satisfaction score ever goes below 60 then the game is over and player loses 
# #the game. The function will return True and the game keeps going. Once the 
# # function returns False then the game is over. 


budget = 1000

#Abe's function
def status_checker(budget):
    """Takes the budget and checks if it goes below 0

    Args:
        budget (int): the starting budget in integer/dollars

    Returns:
        True/False: If the budget is good then it returns True otherwise it 
        return False
    Side effects:
        Prints a game over statement or returns True.
    """
    if budget < 0:
        print("Game over: You ran out of money")
        return False
    else:
        return True