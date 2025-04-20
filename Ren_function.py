""" 
function that will determine a randomly generated scenario the result will
pop out an animal event.

"""

import random # choose a random animal event

def Ren_function(scenario):
    print(scenario)
    
scenario_tpl = ("You see that the penguins are looking hungry. Do you A, feed"
" them or B, ignore them?"), 

("You see that the giraffes are fighting. Do you A, break up the fight or B"
" join the fight?"),

("You see that the lions look very bored. Do you A, jump in the cage or B"
 " give them a toy?"), 

("You see that the gorilla is looking thirsty. Do you A, give it mud or B"
" give it new water?"), 

("You see that the baby panda is crying. Do you A, give it to its mom or B"
 " kick it?")

#scenario_tpl = 1, 2, 3, 4

random.choice(scenario_tpl)

Ren_function(random.choice(scenario_tpl))

userresponse = input("Type A or B ")

if userresponse == "A":
    print("You clicked A ")
    
elif userresponse == "B":
    print("You clicked B ") 
    
else:
    print("Sorry please retry it.")
