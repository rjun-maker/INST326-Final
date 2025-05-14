""" 
Zoo keeper simulator! Made by Team RAAA (Renee Jun, Aiden Anderson, 
Ademir Ferreyra, and Abdurakhmon (Abe) Tukhtasinov)

"""

import random 
from level_checker import LevelChecker 
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
    """ 
    
    Primary author: Renee Jun and Abdurakhmon (Abe) Tukhtasinov
    
    Techniques: use of key function sorted() and f strings containing 
    expressions
    
    Description: Function that randomizes a scenario and 2 good choices, 2 bad 
    choices, and a silly choice the player can choose. There is a scenrio_tpl 
    that has 4 different prompts that pop up. It also calls for the
    get_budget_impact function and update_affection function to keep track
    of the player's budget and affection.
    
    Args:

        scenario: Different scenarios the player can choose from
    
    Returns:
        A print statement showing which scenario and choices the player can pick
    
    """
    print(scenario)
  
budget = 100
affection = 100
player = LevelChecker()
status = True
while status:
    animal = random.choice(ademir_function.animals) # pick a random animal
    
    actions = random.sample(sorted(ademir_function.p_action_good),\
        k=2) # pick two random good actions
    
    actions = actions + (random.sample(sorted(ademir_function.p_action_bad),\
        k=2)) # pick two random bad actions, and combine with the good actions
    
    actions = actions + (random.sample(sorted(ademir_function.p_action_silly),\
        k=1))
    
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
    ademir_function.update_affection(animal, ademir_function.animals_dict, \
        user_response)
    
    # update the budget impact
    budget_change = ademir_function.get_budget_impact(user_response)
    budget += budget_change
    
    # implemented level checker's function
    new_level = min(ademir_function.animals_dict[animal] // 10 + 1, 10)
    player.update_level(new_level)
    print(player)

    if player.win_condition():
        print("You win!")
        break
        
    print("Updated pet score: ", ademir_function.animals_dict[animal])
    print(f"Current budget: ${budget} \n")
    status = Abe_function.status_checker(budget)
    
    
    
#########################################################################################################

#def with parameters

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


#comments
silly_comments = ["lol that was silly", 
                  "trees died for this.",
                  "this is why we can't have nice things",
                  "you think you're all that huh..."]

good_comments = ["aww so sweet",
                 "want a cookie?",
                 "you're basically an animal whisperer",
                 "W zookeper",
                 "They’re wagging their tail... or fins? wait what's a tail"]

bad_comments = ["why would you do that :(",
                "...why?",
                "do better...",
                "APOLOGIZE WITH TEARS. NOW. "]


def get_budget_impact(action):
    """ 
    
    Primary author: Ademir Ferreyra
    
    Techniques: ////
    
    Description: This function will take the action from the user and randomly 
    pick an impact on the player budget. 
    
    Args:
        action (str): the potential action/choice a player makes
    
    Returns:
        Random interval that is low or high
    
    """
    if action not in budget_impact:
        return 0
    low, high = budget_impact[action]
    return random.randint(low, high)


def update_affection(animal_name, animals_dict, player_action):
    """
    Primary author: Ademir Ferreyra
    
    Techniques: keyword arguments
    
    Description: Function that raises ValueErrors if the animal_name or 
    player_action doesn't match the set actions presented. It also gets the 
    current affeciton level

    Args:
        animal_name (str): name of animal
        animal_dict (str): dictionary storing animals and their affection levels
        player_action (str): action player made
        
    Returns:
        new_affection: updates animal dictionary and adds the change to the
        old affection to be the new affection
    """

#building blocks of an algorithm
#two concerns
    if animal_name not in animals_dict:
        raise ValueError(f"{animal_name} could not be found in the zoo")

    if player_action not in p_action_good:
        if player_action not in p_action_bad:
                if player_action not in p_action_silly:
                    raise ValueError(f"Unknown Action: {player_action}")
    
#get the current affection level
    current_affection = animals_dict[animal_name]
    if player_action in p_action_good:
        change = p_action_good[player_action]
        print(random(good_comments or silly_comments))
    elif player_action in p_action_bad:
        change = p_action_bad[player_action]
        print(random(bad_comments or silly_comments))
    elif player_action in p_action_silly:
        change = p_action_silly[player_action]
        print(random(bad_comments or silly_comments))
    

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

def status_checker(budget):
    """ 
    
    Primary author: Abdurakhmon (Abe) Tukhtasinov and Renee Jun
    
    Techniques: conditional expression
    
    Description: Checks the status of player's budget and satisfaction score. 
    If the budget ever goes below 0 or satisfaction score ever goes below 40 
    then the game is over and player loses the game. The function will return 
    True and the game keeps going. Once the function returns False then the 
    game is over.
    
    Args:
        budget (int): references the global budget variable
        
    Returns:
        Either a print statement showing the game over or a True which
        continues the game 
    
    """
    
    False if budget > 0 else False, print("Game over: You ran out of money")
    
    
