import random
attempts = 0

def calculate(user_number, real_number):
    """When user's guess isn't correct, tell them if it's
     too big or too small.
     - user_number: user's last guess
     - real_number: the correct number"""
    if user_number > real_number: print("Too high!")
    elif user_number < real_number: print("Too low!")

# Select a number randomly
numbers = list(range(1, 100+1))
number = int(random.choice(numbers))

# Choose the game level
level = input('What level would you like [easy/hard]? ')
if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5
print(f"You have {attempts} attempts!\n")

# Start the game
while attempts != 0:
    
    # Type the guessed number
    guess = int(input('Guess a number between 1-100: '))
    # Decrease an attempt
    attempts -= 1
    
    # If it was correct, print they won
    if guess == number:
        print(f"\nYou've won! The answer was {number}.\n")
        attempts = 0
    
    # Determine when they lose
    elif attempts == 0 and guess != number:
        print(f"\nYou've lost! The answer was {number}.\n")
    
    # If not, continue the game 
    else: 
        calculate(guess, number)
        continue

    break
