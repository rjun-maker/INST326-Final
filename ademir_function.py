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

#comments
silly_comments = ["lol that was silly", 
                  "trees died for this.",
                  "this is why we can't have nice things",
                  "you think you're all that huh...",
                  "CAN YOU STOP",
                  "I'm calling my lawyers."]

good_comments = ["aww so sweet",
                 "want a cookie?",
                 "you're basically an animal whisperer",
                 "W zookeper",
                 "They’re wagging their tail... or fins? wait what's a tail",
                 "doing your job for once!",
                 "I told my therapist about us"]

bad_comments = ["why would you do that :(",
                "...why?",
                "do better...",
                "APOLOGIZE WITH TEARS. NOW. ",
                "wait is this even legal",
               "can you not",
               "i see you"]

animals = ["Tiger", "Elephant", "Shark", "Penguin", "Panda"]
affection = 50

#dictionary for animals  
animals_dict = {animal: affection for animal in animals}

#############################################################################
# Abe's changes
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
#Abe's function
def get_budget_impact(action):
    """Takes an action and picks a random integers from budget_impacts

    Args:
        action (dic): dictionary of values

    Returns:
        int: based on the action, it returns a random integer
    
    Side effects:
        Returns an integer
    """
    if action not in budget_impact:
        return 0
    low, high = budget_impact[action]
    return random.randint(low, high)
#############################################################################


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
            if player_action not in p_action_silly:
                raise ValueError(f"Unknown Action: {player_action}")
    
#get the current affection level
    current_affection = animals_dict[animal_name]
    if player_action in p_action_good:
        change = p_action_good[player_action]
        print(random.choice(good_comments))
    elif player_action in p_action_silly:
        change = p_action_silly[player_action]
        print(random.choice(silly_comments))
    elif player_action in p_action_bad:
        change = p_action_bad[player_action]
        print(random.choice(bad_comments))
    

    

#keep affection between 0-100
    new_affection = current_affection + change
    if current_affection > 100:
        new_affection = 100
    elif current_affection < 0:
        new_affection = 0
   
    #update dictionary
    animals_dict[animal_name] = new_affection

    return new_affection
