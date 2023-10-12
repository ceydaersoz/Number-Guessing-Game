# Number Guessing Game
# In this game, the user tries to guess a randomly generated number between 1 and 100 within 6 attempts.


import random
random_number = random.randint(1, 100)
attempts = 6

for attempt in range(attempts):
    guess = int(input("What is my secret number: "))
    if guess == random_number:
        print("Correct guess!!! The secret number is:", random_number)
        break
    else:
        if guess > random_number:
            print("Guess a smaller number. Remaining attempts:", attempts - 1)
        elif guess < random_number:
            print("Guess a larger number. Remaining attempts:", attempts - 1)
        
        attempts -= 1
else:
    print("You have used all 6 attempts. The correct answer was:", random_number)




# The computer will try to find the number you selected with 8 rights.
# You keep a number and let the computer try to find it, you will direct the computer by saying up and down after each guess.

import random

random_number = random.randint(1, 100)

min_number = 1
max_number = 100
attempts = 8

user_number = int(input("Think of a number: (between 1 and 100)"))

for attempt in range(attempts):
    print("Computer's guess: ", random_number)
    feedback = int(input("Is the computer's guess correct? (1: Correct 2: Higher 3: Lower)"))

    if feedback == 1:
        print("The computer correctly guessed your number!!", user_number, random_number)
        break
    elif feedback == 2:
        min_number = random_number
        random_number = random.randint(min_number, 100)
    elif feedback == 3:
        max_number = random_number
        random_number = random.randint(1, max_number)

    attempts -= 1
else: 
    print("You have used all 8 attempts. The correct answer was:", user_number)
