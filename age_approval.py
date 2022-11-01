#!/usr/bin/env python3

# Created by: Kyanh Pham
# Created on: Oct 2022
# This program sees if grandma approves of your age.

import constants


def main():

    # This function sees if they can date

    # Input
    age_string = input("Please enter your age: ")
    print("")

    # Process and Output
    try:
        age_int = int(age_string)
        if age_int > constants.MINIMUM_AGE and age_int < constants.MAXIMUM_AGE:
            print("You are an acceptable age!")
        elif age_int < constants.ZERO:
            print("That is not a valid age!")
        else:
            print("You are not an acceptable age!")
    except ValueError:
        print("{0}, is not a valid input!".format(age_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
