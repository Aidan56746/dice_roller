#!/usr/bin/bash

"""
Program Name: dice_roller.py
Purpose: A randomized dice roller game.
Author: Aidan Simard
Date: 3/10/2026
Version: 1.1
"""

import random

while True:
    num_dice = 0
    while num_dice <= 0:
        num_dice = int(input("Enter a number of dice(must be greater than 0): "))
        if num_dice <= 0:
            print("Invalid input. Please put a prompt greater than 0.")

    die_faces = 0
    while die_faces <= 0:
        die_faces = int(input("Enter the number of faces(must be greater than 0):"))
        if die_faces <= 0:
            print("Invalid input. Please put a prompt greater than 0.")

        min_val = num_dice * 1
        max_val = num_dice * die_faces

        roll_result = random.randint(min_val, max_val)

        print("The result of of your roll:" , roll_result)

        if roll_result == max_val:
            print("You rolled the max value!")
        elif roll_result == min_val:
            print("You rolled the min value!")

    repeat = input ("Do you want to roll again? (y/n): ")
    if repeat == "y":
        print("Roll Again!")

    elif repeat == "n":
        break
