#!/usr/bin/env python3

# created by Youngjun Kim
# created on May 2021
# This program checks if your age is acceptable to date my grandchild


def main():
    # this function checks if your age is acceptable to date my grandchild
    
    # input
    integer_as_string = input("Enter your age: ")
    print("")
    
    # process & output
    try:
        integer_as_number = int(integer_as_string)
        
        if integer_as_number < 25:
            print("You are too young!")
        elif integer_as_number > 40:
            print("You are too old!")
        else:
            print("You are accepted to date my grandchild.")
    except Exception:
        print("That was not valid input.")


if __name__ == "__main__":
    main()
