#My function is called status_check(). What is does is check the status of 
#player's budget and satisfaction score. If the budget ever goes below 0 or 
#satisfaction score ever goes below 60 then the game is over and player loses 
#the game. The function will return True and the game keeps going. Once the 
# function returns False then the game is over. 


budget = 1000
satisfaction = 100

#My function  
def status_checker(budget, satisfaction):
    if budget < 0:
        print("Game over: You ran out of money")
        return False
    if satisfaction < 60:
        print("Animals are angry. Game over")
        return False
    print("Everything good so far.")
    return True

#dummy function to simulate what a round could look like. The function returns
#the boolean value of my function status_checker.
def dummy_round(budget, satisfaction):
    print("Scenario: Pandas need more food. Spend $200 to buy food?")
    print(f"Current budger: ${budget}")
    print(f"Current satisfaction_score: {satisfaction}")
    
    dummy_decision = input("Do you want to spend money? y/n   ")
    
    if dummy_decision == 'y':
        budget = budget - 200
        satisfaction = satisfaction + 5   
    else:
        satisfaction = satisfaction - 5
    
    return status_checker(budget, satisfaction)

#Dummy function to start the game. If status_checker returns False then this 
#function ends the game.   
def dummy_start_game():
    print("Zoo simulator")
    if dummy_round(budget, satisfaction):
        print("You survived")
    else:
        print("Game over")

if __name__ == "__main__":  
    dummy_start_game()
       
       
        
