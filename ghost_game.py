'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

#Ghost game 
from random import randint 
print("ghost game")
feeling_brave=True
score = 0

while feeling_brave:
    ghost_door=randint(1,3)
    print("three door ahead...") 
    print(" a ghost begining one.")
    print("which door do you open ?")
    door=int(input("1, 2 or 3?"))
    if door == ghost_door:
        print()
        print("THE GHOST IS HERE!!!")
        print()
        score = 0
        feeling_brave = False
        break
    else:
        print()
        print("Phew! No ghost... The ghost was behind door "+str(ghost_door))
        print()
        score = score+1
        feeling_brave = True

        
