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

status = True
while status:
    animal = random.choice(ademir_function.animals) # pick a random animal
    actions = random.sample(sorted(ademir_function.p_action_good), k=2) # pick two random good actions
    actions = actions + (random.sample(sorted(ademir_function.p_action_bad), k=2)) # pick two random bad actions, and combine with the good actions
  
#############################################################################
  # Abe's changes
  # I simplfied the scenarios   
    # scenarios to pick from randomly
    joined_actions = ", ".join(actions)
    scenario_tpl = (
      f"You see a {animal}, do you {joined_actions} it?", 
      f"You see a {animal}, they are fighting! do you {joined_actions} it?",
      f"You see a {animal}, they are crying... do you {joined_actions} it?",
      f"You see a {animal}, they are bazingaing... do you {joined_actions} it?"
    )
#############################################################################

    # randomly chooses a scenario from scenario_tpl
    Ren_function(random.choice(scenario_tpl)) 

#############################################################################
 # Abe's Changes
 # I made change to user_response so that it wont crash if wrong answer is given   
    # User response
    while True:
      user_response = input().lower()
      valid_actions = [action.lower() for action in actions]
      if user_response in valid_actions:
        break
      else:
        print("Invalid input. Try again.")  
#############################################################################
 
    
    print("***********************")
    
    # update animal affection/satisfaction score
    ademir_function.update_affection(animal, ademir_function.animals_dict, user_response)
    
#############################################################################
  # Abe's changes
  #I made this line of code to impact the change the budget. 
    # update the budget impact
    budget_change = ademir_function.get_budget_impact(user_response)
    budget += budget_change
 #############################################################################
  
    print("Updated pet score: ", ademir_function.animals_dict[animal])
    print(f"Current budget: ${budget} \n")
    status = Abe_function.status_checker(budget)

    
    # check if game over
   
    
    
    # check what level the player is at
    #whoaLevel = level_checker.win_condition
