#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: October 12, 2022
# This program asks the user for a random number from
# 0 to 9 and checks if it is the same as the correct
# number that is generated
import random


def main():
    # Get the users input for a number 0 to 9
    user_num = int(input("Enter a number from 0 to 9: "))

    # Generates a random number from 0 to 9
    random_number = random.randint(0, 9)

    # checks if user input is equal to random number
    if user_num == random_number:
        print("You guessed correctly!")
    else:
        # changes the random number into a string
        # then prints it
        random_number = str(random_number)
        print("The correct answer was " + random_number)


if __name__ == "__main__":
    main()
