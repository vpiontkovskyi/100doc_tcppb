"""
A simple text-based adventure game.
This program is a text-based adventure game where the player makes a sequence
of choices to uncover a treasure. The game includes multiple paths and endings
based on user decisions. The objective of the player is to find the treasure
while avoiding obstacles and wrong paths.
"""


"""
Shorter version and as expected in course.
"""
ascii_art =r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
welcome_message = (f"Welcome to Treasure Island. \n"
                   f"Your mission is to find the treasure.")
print(f"{ascii_art}{welcome_message}")

choice1 = input("You are at a crossroad, where do you want to go? Type 'left' or 'right'.").lower()
if choice1 == "right":
    print("You fell in to a hole. Game Over.")
elif choice1 == "left":
    choice2 = input("You are come to a lake. There is an island in the middle of the lake. "
                    "Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if choice2 == "swim":
        print("You got attacked by an angry trout. Game Over.")
    elif choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. "
                        "One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3 == "red":
            print("Its a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You enter a room of a beasts. Game Over.!")
        elif choice3 == "blue":
            print("You found a treasure. You won!")
        else:
            print("You chose an invalid colour. Game Over.")
    else:
        print("You chose an invalid option. Game Over.")
else:
    print("You chose an invalid option. Game Over.")
