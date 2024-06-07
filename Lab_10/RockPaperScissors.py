# CSC 1301 - Program 10
# Author: Hemant Kosaraju 
# Email: hkosaraju2@student.gsu.edu
# Section: Section 014 & CRN 84157

import random

print("\nThe Rock Paper Scissors Game \n")

rock = 2
paper = 3
scissors = 1

user_input = 0

while user_input != -1:
    user_input = int(input("Please enter 2 for rock, 3 for paper, 1 for scissors or -1 to quit: "))
    computer_choice = random.randint(1,3)
    if user_input != -1:
        if user_input == rock:
            print("\nYou chose rock")
        if user_input == paper:
            print("\nYou chose Paper")
        if user_input == scissors:
            print("\nYou chose scissors")
        if computer_choice == rock:
            print("\nThe computer chose rock")
        if computer_choice == paper:
            print("\nThe computer chose paper")
        if computer_choice == scissors:
            print("\nThe computer chose scissors")
        if user_input == rock:
            if computer_choice == scissors:
                print('\nCongratualtions you win!\n')
        if user_input == scissors:
            if computer_choice == paper:
                print('\nCongratualtions you win!\n')
        if user_input == paper:
            if computer_choice == rock:
                print('\nCongratualtions you win!\n')
        if computer_choice == rock:
            if user_input == scissors:
                print("\nSorry you lose!\n")
        if computer_choice == scissors:
            if user_input == paper:
                print("\nSorry you lose!\n")
        if computer_choice == paper:
            if user_input == rock:
                print("\nSorry you lose!\n")
        if user_input == computer_choice:
            print("\nThe match was a tie!\n")
print("\nGoodbye\n")