import os
import random
import time
import TicTacToeGame
import GuessTheNumberGame
#from PIL import Image
# Show map
#img = Image.open('Map.png')
#img.show()
# Input Username
username = input("Please Enter your name: ")
# formatting username
#formatted_username = f"\033[1m{username}\033[0m"
def rainbow_text(text):
    rainbow_colors = ["\033[91m", "\033[93m", "\033[92m", "\033[94m", "\033[95m", "\033[96m"]
    rainbow_text = ""
    for i, char in enumerate(text):
        rainbow_text += rainbow_colors[i % len(rainbow_colors)] + char
    return rainbow_text + "\033[0m"
formatted_username = rainbow_text(username)
bold_red_text = "\033[1;31mWARNING - Never approach the Compiler without collecting all the required code items.\033[0m"
# Display starting menu
def prompt():
    print("Hey there, Adventurer! \n\n\
A critical task has emerged, and only one person can code it - the Legendary Coder - " + formatted_username + "!\n\n\
Your mission is to collect scattered pieces of code from different websites and bring them to the Compiler,\n\
known as CortexShredder.\n\n"+ bold_red_text + "\nCortexShredder is infamous for mercilessly shredding unprepared coders!\n\n\
Controls:\n'go {direction}' (travel north, south, east, or west)\n\
'put {code_item}' (to add code fragments to your collection.)\n")

    input("Press any key to continue...")


# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Map
rooms = {
    'Start Point': {'North': 'STACK OVERFLOW', 'South': 'DEVDOCS', 'East': 'GITHUB'},
    'STACK OVERFLOW': {'South': 'Start Point', 'Item': 'Syntax Stars'},
    'DEVDOCS': {'North': 'Start Point', 'East': 'GFG', 'Item': 'Looping Lollipops'},
    'GITHUB' : {'West': 'Start Point', 'North': 'QUORA', 'East': 'CortexShredder', 'Item': 'Debugging Diamonds'},
    'QUORA' : {'South': 'GITHUB', 'East': 'CODE REVIEW', 'Item': 'Variable Vortex Crystals'},
    'CODE REVIEW': {'West': 'QUORA', 'Item': 'Conditional Cookies'},
    'GFG': {'West': 'DEVDOCS', 'Item': 'Function Feathers'},
    'CortexShredder': {'West': 'GITHUB', 'Boss': 'Compiler'}
    }
 
# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

# Tracks current room
current_room = "Start Point"

# Tracks last move
msg = ""

clear()
prompt()

# Gameplay loop
while True:

    clear()

    # Display player info
    print(f"You are in the {current_room}\nCollected list : {inventory}\n{'-' * 27}")

    # Display msg
    print(msg)

    # Item indicator
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:

            if nearby_item[-1] == 's':
                print(f"You see {nearby_item}")

            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}")

            else:
                print(f"You see a {nearby_item}")
    
    # Boss encounter
    if "Boss" in rooms[current_room].keys():

        if len(inventory) < 6:
            lines = [
            "CortexShredder  - do you know how would a tree without look like!?\n",
            formatted_username + "	- No\n",
            "CortexShredder  - do you know how would a mobile without incoming and outgoing services be like!?\n",
            formatted_username + "	- No\n",
            "CortexShredder  - do you know how would a server without network like!?\n",
            formatted_username + "	- No\n",
            "CortexShredder  - It will be lame, useless and full of errors just like your code!!\n",
            "DESTROYED\n",
            "GAME OVER"
            ]
            for line in lines:
                print(line)
                time.sleep(2)
            break

        else:
            lines = [
            "CortexShredder  - do you know how would a plant full of flower look like!?\n",
            formatted_username + "	- No\n",
            "CortexShredder  - do you know how would a Programmer who aced all the validation tests feel like!?\n",
            formatted_username + "	- No\n",
            "CortexShredder  - do you know how website with no lag or downtime feels like!?\n",
            formatted_username + "	- No\n",
            "CortexShredder  - It feels Beautiful, Successful and Flawless just your code!!\n",
            "CortexShredder  - I have a gift for you!! CODE - Diwali@Nagarro2023\n",
            "YOU CAN NOW OPEN YOUR DIWALI GIFT (SurpriseGift.pdf) USING THIS CODE \n",
            "MISSION COMPLETE\n",
            "YOU WIN"
            ]
            for line in lines:
                print(line)
                time.sleep(2)
            break

    # Accepts player's move as input
    user_input = input("Enter your move:\n")

    # Splits move into words
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    # Reset item and direction
    item = "Item"
    direction = "null"

    # Second word is object or direction
    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = " ".join(item).title()

    # Moving between rooms
    if action == "Go":

        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}"

        except:
            msg = "You can't go that way."
    
    # Picking up items
    elif action == "Get":
        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:
                    security_check=1
                    security_check = random.randint(0, 1)
                    if(security_check == 0):
                        inventory.append(rooms[current_room]["Item"])
                        print("You've successfully proven your humanity!\n The digital guardians of the website welcome you to collect the " +  rooms[current_room]["Item"] +". Your journey continues")
                        time.sleep(3)
                        msg = f"Added {item} to List!"
                    else:
                        while(security_check):
                            print("The digital guardians of the website raise their virtual eyebrows, finding you suspicious!\nTo prove you're still a HUMAN prepare for a challenge!")
                            game_choice = random.randint(0, 1)
                            if(game_choice):
                                security_check = TicTacToeGame.play_tic_tac_toe()
                                time.sleep(1)
                            else:
                                security_check = GuessTheNumberGame.guess_the_number()
                                time.sleep(1)
                            if(security_check == 0):
                                print("You've successfully proven your humanity!\n The digital guardians of the website welcome you to collect the " +  rooms[current_room]["Item"] +". Your journey continues")
                                time.sleep(3)
                                inventory.append(rooms[current_room]["Item"])
                                msg = f"Added {item} to List!"
                else:
                    msg = f"You have already collected {item}"
            
            else: 
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"
    
    # Exit program
    elif action == "Exit":
        break

    # Any other commands invalid
    else:
        msg = "Invalid command"
