#!/usr/bin/bash

"""
Program Name: dice_roller.py
Purpose: A randomized dice roller game.
Author: Aidan Simard
Date: 3/10/2026
Version: 1.0
"""

import random
# This part is just asking for the inputs for how many dice's there will be and how many faces each die has
num_dice = int(input("Enter the number of dice: "))
die_faces  = int(input("Enter the number of dice faces: "))

# this part is basically summarizing the results: the min value is for every one dice and the max value multiples by the die number and face.
min_val = num_dice * 1
max_val = num_dice * die_faces

# roll result is basically a variable being created to show the results.
roll_result = random.randint(min_val, max_val)

print("The result of the dice roll is: ", roll_result)

if roll_result == max_val:
    print("Congratulations, you rolled the max value!")
