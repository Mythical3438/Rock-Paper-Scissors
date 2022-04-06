#!/usr/bin/env python3

import random
import time

from numpy import not_equal

inputs = ('rock', 'paper', 'scissors')

computer = 0
user = 0


    
while True:
    computer_inputs = random.choice(inputs)
    user_inputs = input('\n\nPlease type an input from this list... \n Rock \n Paper \n Scissors \n:').lower()
    
    if user == 2:
        print('\n\n---- Game Over! You Lose... LOSER! ----\n\n')
        break
            
    if computer == 2:
        print('\n\n----- Game Over!! You WIN!!! ----\n\n')
        break
    
    if user_inputs == computer_inputs:
            print(f'It was a tie! You had {user_inputs} and the computer had {computer_inputs}.')

    elif user_inputs == 'scissors' and computer_inputs == 'rock':
        print(f'You Lose, {computer_inputs} beats {user_inputs}')
        user += 1

    elif user_inputs == 'paper' and computer_inputs == 'scissors':
        print(f'You Lose, {computer_inputs} beats {user_inputs}')
        user += 1

    elif user_inputs == 'rock' and computer_inputs == 'paper':
        print(f'You Lose, {computer_inputs} beats {user_inputs}')
        user += 1

    else:
        print(f'You WIN!!!, {user_inputs} beats {computer_inputs}')
        computer += 1

    print('  -------------------------------------------')
    print(f'  | Player : {user} | Computer : {computer} |')
    print('  -------------------------------------------')


