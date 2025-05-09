""" 
function that will determine a randomly generated scenario the result will
pop out an animal event.

"""

import random # choose a random animal event
import level_checker 
import ademir_function
import Abe_function

def Ren_function(scenario):
    print(scenario)
  
  # make a budget
  # make insult neutral
  # add more actions
    

status = True
while status:
    animal = random.choice(ademir_function.animals) # pick a random animal
    actions = random.sample(sorted(ademir_function.p_action_good), k=2) # pick two random good actions
    actions = actions + (random.sample(sorted(ademir_function.p_action_bad), k=2)) # pick two random bad actions, and combine with the good actions

    
    # scenarios to pick from randomly
    scenario_tpl = ((f"You see a {animal}, do you {", ".join(actions)} it?"), 
                    (f"You see a {animal}, they are fighting! do you {", ".join(actions)} it?"),
                    (f"You see a {animal}, they are crying... do you {", ".join(actions)} it?"))

    # randomly chooses a scenario from scenario_tpl
    Ren_function(random.choice(scenario_tpl)) 

    # User response
    user_response = input()
    
    print("***********************")
    
    # update animal affection/satisfaction score
    ademir_function.update_affection(animal, ademir_function.animals_dict, user_response)
    print("Updated pet score: ", ademir_function.animals_dict[animal])
    
    # buget
    #Abe_function.status_checker(budget, statisfaction)
    
    # check if game over
    status= Abe_function.status_checker(100, ademir_function.animals_dict[animal])
    
    # check what level the player is at
    #whoaLevel = level_checker.win_condition
    
    
