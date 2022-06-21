#Number Guessing Game.
#Guesses are made until all numbers are guessed.
#The game reveals whether the closest unguessed number is higher or lower than each guess.
#Numbers are distinct.
#Typing 'q' quits the game.

import os
import sys
import random
MIN = 0
MAX = 10
NUM_VALUES = 3

def handle_guess(guess, values):
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present
    
	# copy values list to new_vals list
	# so the original values list is untouched
    new_vals = values.copy()
	
    # convert guess to type int before looking in list
    guessint = int(guess)
    
    # if number is found in list, remove number from list, exit function
    # if number is not found, call find_closest(), exit function
    try:
        if new_vals.index(guessint) >= 0:
            new_vals.remove(guessint)
            print (f'You found {guess}! It was in the list')
            print(f'There are {len(new_vals)} values left.')
    except ValueError:
        find_closest(guess, new_vals)
    
    return new_vals


def find_closest(guess, values):
    # This function should return the value that is closest to `guess`
    guessint = int(guess)
    closest = sorted(values, key=lambda x: abs(x - guessint))[0]
    
    if closest > guessint:
        print('The closest value is higher')
    else:
        print('The closest value is lower')
	
    return closest

def run_game(values):
    # While there are values to be guessed and the user hasn't quit (with 'q'),
    # the game should wait for the user to input their guess and then
    # reveal whether the closest number is lower or higher.
    print(f'Numbers are between {MIN} and {MAX} inclusive. There are {len(values)} values left.')
    guess = input('Guess: ')
    
    # Your code goes here.
    while len(values) > 0:
        if guess == "q":
            print('Thanks for playing! See you soon.')
            os._exit(1)
        else:
            values = handle_guess(guess, values)
            if len(values) == 0:
                print ("Congratulations! You won!")
            else:
                guess = input('Guess: ')
    

if __name__ == '__main__':
        
    # Generate a random list and run the game
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)
   
