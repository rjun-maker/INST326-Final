#### Ren_function.py ####
""" 
function that will determine a randomly generated scenario the result will
pop out an animal event.

"""

import random # choose a random animal event
import level_checker 
import ademir_function
import Abe_function


print("""========================================================================
███████╗░█████╗░░█████╗░██╗░░██╗███████╗███████╗██████╗░███████╗██████╗░
╚════██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
░░███╔═╝██║░░██║██║░░██║█████═╝░█████╗░░█████╗░░██████╔╝█████╗░░██████╔╝
██╔══╝░░██║░░██║██║░░██║██╔═██╗░██╔══╝░░██╔══╝░░██╔═══╝░██╔══╝░░██╔══██╗
███████╗╚█████╔╝╚█████╔╝██║░╚██╗███████╗███████╗██║░░░░░███████╗██║░░██║
╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
░██████╗██╗███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔════╝██║████╗░████║██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
╚█████╗░██║██╔████╔██║██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
░╚═══██╗██║██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
██████╔╝██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

🦁🐯🐵🐸🐧🐘🦓🦒🐍🐢🐨🐼🐷🐮🐔🐊🦘🐺🦙🐫🦛🐦🐴🦔🐻‍❄️🐬🦆🦉🐿️🦇🐠🦞🪱🐙🦑🦐🦢
========================================================================""")


def Ren_function(scenario):
  print(scenario)
  
budget = 1000
  # make insult neutral
  # add more actions
    

status = True
while status:
    animal = random.choice(ademir_function.animals) # pick a random animal
    actions = random.sample(sorted(ademir_function.p_action_good), k=2) # pick two random good actions
    actions = actions + (random.sample(sorted(ademir_function.p_action_bad), k=2)) # pick two random bad actions, and combine with the good actions
  
    
    # scenarios to pick from randomly
    joined_actions = ", ".join(actions)
    scenario_tpl = (
      f"You see a {animal}, do you {joined_actions} it?", 
      f"You see a {animal}, they are fighting! do you {joined_actions} it?",
      f"You see a {animal}, they are crying... do you {joined_actions} it?",
      f"You see a {animal}, they are bazingaing... do you {joined_actions} it?"
    )


    # randomly chooses a scenario from scenario_tpl
    Ren_function(random.choice(scenario_tpl)) 

    # User response
    while True:
      user_response = input().lower()
      valid_actions = [action.lower() for action in actions]
      if user_response in valid_actions:
        break
      else:
        print("Invalid input. Try again.")  
    
    print("***********************")
    
    # update animal affection/satisfaction score
    ademir_function.update_affection(animal, ademir_function.animals_dict, user_response)
    
    # update the budget impact
    budget_change = Abe_function.get_budget_impact(user_response) # something is wrong with this... Attirbute Error
    budget += budget_change
    
    print("Updated pet score: ", ademir_function.animals_dict[animal])
    print(f"Current budget: ${budget} \n")
    status = Abe_function.status_checker(budget)

    
    # check if game over
   
    
    
    # check what level the player is at
    #whoaLevel = level_checker.win_condition
    
    
#########################################################################################################

####  ademir_function.py ######

# Final Project interim deliverable - Ademir Ferreyra

#def with parameters
import random

p_action_good = {
    "pet" : 5,
    "feed" : 10,
    "play" :15,
    "cuddle": 20 
    }
p_action_silly = {
    'b*tch slap' : -50, 
    'swim?' : 0, 
    'EAT' : -10000, 
    'bazinga!' : 100000
    }
p_action_bad = {
    "slap": -15,
    "ignore": -5,
    "kick": -20,
    "insult": -10
    }

animals = ["Tiger", "Elephant", "Shark", "Penguin", "Panda"]
affection = 50

#dictionary for animals  
animals_dict = {animal: affection for animal in animals}

#adding budget impact
budget_impact = {
    "pet" : (-10, -1),
    "feed" : (-100, -1),
    "play" :(-30, 30),
    "cuddle": (0, 20),
    "b*tch slap" : (-200, -1), 
    "swim?" : (-100, 100), 
    "EAT" : (-10000, 0), 
    "bazinga!" : (-1000, 1000), 
    "slap": (-100, 100),
    "ignore": (-100, 100),
    "kick": (-100, 100),
    "insult": (-100, 100)
}

#This function will take the action from user and randomly pick an impact
#on the player budget. 
def get_budget_impact(action):
    if action not in budget_impact:
        return 0
    low, high = budget_impact[action]
    return random.randint(low, high)


def update_affection(animal_name, animals_dict, player_action):
    """_summary_

    Args:
        animal_name (str): name of animal
        animal_dict (str): dictionary storing animals and their affection levels
        player_action (str): action player made
    """

#building blocks of an algorithm
#two concerns
    if animal_name not in animals_dict:
        raise ValueError(f"{animal_name} could not be found in the zoo")

    if player_action not in p_action_good:
        if player_action not in p_action_bad:
            raise ValueError(f"Unknown Action: {player_action}")
    
#get the current affection level
    current_affection = animals_dict[animal_name]
    if player_action in p_action_good:
        change = p_action_good[player_action]
    elif player_action in p_action_bad:
        change = p_action_bad[player_action]
    

#keep affection between 0-100
    new_affection = current_affection + change
    if current_affection > 100:
        new_affection = 100
    elif current_affection < 0:
        new_affection = 0
   
    #update dictionary
    animals_dict[animal_name] = new_affection

    return new_affection

#########################################################################################################

### Abe_function #####
#My function is called status_check(). What is does is check the status of 
#player's budget and satisfaction score. If the budget ever goes below 0 or 
#satisfaction score ever goes below 40 then the game is over and player loses 
#the game. The function will return True and the game keeps going. Once the 
# function returns False then the game is over. 


budget = 1000
#My function  
def status_checker(budget):
    if budget < 0:
        print("Game over: You ran out of money")
        return False
    else:
        return True



#dummy function to simulate what a round could look like. The function returns
#the boolean value of my function status_checker.
'''
def dummy_round(budget):
    print("Scenario: Pandas need more food. Spend $200 to buy food?")
    print(f"Current budget: ${budget}")
    
    dummy_decision = input("Do you want to spend money? y/n   ")
    
    if dummy_decision == 'y':
        budget = budget - 200
    else:
        budget = budget + 100
    
    return status_checker(budget)

#Dummy function to start the game. If status_checker returns False then this 
#function ends the game.   
def dummy_start_game():
    print("Zoo simulator")
    if dummy_round(budget):
        print("You survived")
    else:
        print("Game over")

if __name__ == "__main__":  
    dummy_start_game()
'''       
       
        
    
