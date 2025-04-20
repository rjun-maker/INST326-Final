""" 
Zoo keeper simulator!

"""

""" 
function that will determine a randomly generated scenario the result will
pop out an animal event.

"""

import random # choose a random index

def my_function(scenario):
    print(scenario)
    
scenariolist = [] # should I use a list? Or a diff container data set??
    
my_function("You walk up to the panda bear exhibit and see that a baby panda \
             is crying. Do you A. Give it a banana or B. Punch it")

userresponse = input("Type A or B")

if userresponse == "B":
    print("You clicked B ")
    
elif userresponse == "A":
    print("You clicked A ")
    
else:
    print("Sorry please retry it.")
