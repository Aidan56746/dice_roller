#!/usr/bin/bash

"""
Program Name: dice_roller.py
Purpose: A randomized dice roller game.
Author: Aidan Simard
Date: 3/10/2026
Version: 1.2
"""

import random

#basically this part is just asking for the prompts and making sure the user can't put a number equal or less than 0
def get_numdice():
    while True:
        num = int(input("Enter number of dice: "))
        if num > 0:
            return num
        print("Must be at least 1!")


def get_diefaces():
    while True:
        faces = int(input("Enter number of faces: "))
        if faces > 0:
            return faces
        print("Must be at least 1!")

#this part is just for fact checking just to clarify the output for the script
def roll_dice(num_dice, die_faces):
    return random.randint(num_dice, num_dice * die_faces)


def is_max_score(roll, max_val):
    return roll == max_val


# Main Part of the program, basically if the user wishes to continue the script, and the various prints 
def main():
    playing = "y"
    while playing.lower() == "y":
        dice = get_numdice()
        faces = get_diefaces()
        result = roll_dice(dice, faces)

        print("You rolled:" ,result)

        if is_max_score(result, dice * faces):
            print("CONGRATULATIONS! Max score!")

        playing = input("Roll again? (y/n): ")
main()
