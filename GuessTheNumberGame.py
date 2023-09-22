import random

def guess_the_number():
    number = random.randint(1, 100)
    guess = 0
    print("You need to Guess the number!\n")
    while guess != number:
        guess = int(input("Enter Guess a number : "))
        if guess < number:
            print("Guess higher!")
        elif guess > number:
            print("Guess lower!")
        else:
            print("You won!")
            return 0  # User wins
    
    return 1  # User loses

