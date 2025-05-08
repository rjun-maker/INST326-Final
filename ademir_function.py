# Final Project interim deliverable - Ademir Ferreyra

#def with parameters


p_action_good = {
    "pet" : 5,
    "feed" : 10,
    "play" :15,
    "cuddle": 20 
    }
p_action_silly = {
    'pet' : 5, 
    'bitch slap' : -50, 
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

animals = ["Dog", "Cat", "Hamster", "Fish"]
affection = 50

#dictionary for animals  
animals_dict = {animal: affection for animal in animals}

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

    



