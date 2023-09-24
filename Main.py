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
bold_red_text = "\033[1;31mWARNING - Don't go to Headquarters without completing the task\033[0m"
# Display starting menu
def prompt():
    print("Hey there, Adventurer! \n\n\
In a world filled with sweetness and wonder, Manas and Manmohan have an extraordinary mission for you.\n\
They have decided to send delectable treats to friends scattered across the globe and \n\
have handpicked his most valiant and trusted envoy - none other than you, the legendary " + formatted_username + "!\n\n\
Your quest is to embark on a tantalizing journey, delivering these mouthwatering delights to every corner of the world.\n\n\
But that's not all! Once you've completed your mission and returned to the legendary Nagarro's Headquarters,\n\
an incredible surprise awaits you, courtesy of Manas and Manmohan themselves.\n "+ bold_red_text + 
"\nBuckle up, brave traveler, for a delicious and daring adventure awaits! Best of luck on your sweet expedition!\n\n\
Moves:\t'go {direction}' (travel north, south, east, or west)\n\
\t'put {company_code}' (to add code to the list of delivered sweets and mark as delivered.)\n")

    input("Press any key to continue...")


# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Map
rooms = {
    'Sweets Shop': {'North': 'Jeffery Preston Bezoz', 'South': 'Nithin Kamath & Nikhil Kamath', 'East': 'Ratan Naval Tata'},
    'Jeffery Preston Bezoz': {'South': 'Sweets Shop', 'Item': 'Amazon'},
    'Nithin Kamath & Nikhil Kamath': {'North': 'Sweets Shop', 'East': 'Timothy Donald Cook', 'Item': 'Zerodha'},
    'Ratan Naval Tata' : {'West': 'Sweets Shop', 'North': 'Satya Narayana Nadella', 'East': 'Nagarro Headquaters', 'Item': 'Tata'},
    'Satya Narayana Nadella' : {'South': 'Ratan Naval Tata', 'East': 'Elon Reeve Musk', 'Item': 'Microsoft'},
    'Elon Reeve Musk': {'West': 'Satya Narayana Nadella', 'Item': 'Spacex'},
    'Timothy Donald Cook': {'West': 'Nithin Kamath & Nikhil Kamath', 'Item': 'Apple'},
    'Nagarro Headquaters': {'West': 'Ratan Naval Tata', 'Boss': 'Dr. Manas Human & Dr. Manmohan Gupta'}
    }

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

# Tracks current room
current_room = "Sweets Shop"

# Tracks last move
msg = ""

clear()
prompt()

# Gameplay loop
while True:

    clear()

    # Display player info
    print(f"You are in the {current_room}\nDelivered list : {inventory}\n{'-' * 27}")

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
            "Dr. Manas Human    - Yahan se pachas pachas kos door gaon mein … jab koi new project aata hai, toh maa kehti hai bete nagarro ke pass chala … chala ja nahi toh ye project deploy nahi ho paega\n",
            "Dr. Manmohan Gupta - Itna bharosa kiya , phir bhi waapas aagaye... tofe vapis leke aa gae...Kya samaz kar aaye the? Sardar bahot kush hoga? Sabasi dega?\n",
            "Dr. Manas Human    - Tera kya hoga " + formatted_username + "?\n",
            formatted_username + ": Sardar...maine aapka namak khaya hai?\n",
            "Gabbar: To ab goli khaa...\n",
            formatted_username + ": Bhaaaag Dhanno bhaag aaj " + formatted_username + " ki izzat ka sawal hai\n OPPS!! YOU ARE DEAD"]
            for line in lines:
                print(line)
                time.sleep(2)
            break

        else:
            lines = [
            "Dr. Manmohan Gupta - Duniya ke kissi project ki requirement itnee pakki nahi ki Nagarro usse pura na kar sake \n",
            "Dr. Manas Human - Mogambo Khush Hua\n",
            "Dr. Manmohan Gupta - Tumhe aisa tofa milega, jisse Tumhara toh dil garden-garden ho jaega.\n",
            "Dr. Manas Human - Haan, Bilkul Yelo tijori ki chabhi aur lelo apna tofa\nCODE hai - Diwali@Nagarro2023\n",
            "YOU CAN NOW OPEN YOUR DIWALI GIFT (SurpriseGift.pdf) USING THIS CODE \n"]
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
    elif action == "Put":
        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:
                    security_check=1
                    security_check = random.randint(0, 1)
                    if(security_check == 0):
                        inventory.append(rooms[current_room]["Item"])
                        print("Security experts have confirmed your legendary status, " + formatted_username + ". They warmly welcome you to the " + rooms[current_room]["Item"] + " office with open arms.")
                        time.sleep(2)
                        msg = f"Delivered to {item}!"
                    else:
                        while(security_check):
                            print("The vigilant security expert at the door raises an eyebrow, finding you intriguing! \nTo prove you're the legendary " + formatted_username + ", prepare for a challenge, oh mighty hero! The game awaits!")
                            game_choice = random.randint(0, 1)
                            if(game_choice):
                                security_check = TicTacToeGame.play_tic_tac_toe()
                                time.sleep(1)
                            else:
                                security_check = GuessTheNumberGame.guess_the_number()
                                time.sleep(1)
                            if(security_check == 0):
                                print("Security experts have confirmed your legendary status, " + formatted_username + ". They warmly welcome you to the " + rooms[current_room]["Item"] + " office with open arms.")
                                time.sleep(2)
                                inventory.append(rooms[current_room]["Item"])
                                msg = f"Delivered to {item}!"
                else:
                    msg = f"You have already Delivered to {item}"
            
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
