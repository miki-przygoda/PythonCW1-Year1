# Imports from file made by Mikolaj
from functions import (
    options,
    # parents_and_grandparents as pag,
    # immediate_and_extended_family as ief,
    siblings_and_cousins as sac,
    birthday_calendar as bcal,
    average_age as age,
    number_of_children as noc,
    all_members as am,
    print_line,
)



options() # Displays all the options like shows below
#     What feature would you like to access:
#     1) Parents and Grandparents -- Not a part of this repo
#     2) Immediate and Extended Family -- Not a part of this repo
#     3) Siblings and Cousins
#     4) Birthdays and Birthday Calendar
#     5) Average Age
#     6) Number of Children
#     7) Display All family members
#     8) Exit



choice = 0  # Initial value setting
while True: # Will continue to run until the user exits using choice 8
    try:
        choice = input("Please enter a number between 1 and 8: ")
        match int(choice):
            case 1: # Parents and Grandparents
                print_line()
                # pag()
                print("This feature was written by my school partner -- not a part of this repo")
                print("Done...")
                options()
            case 2: # Immediate and Extended Family
                print_line()
                # ief()
                print("This feature was written by my school partner -- not a part of this repo")
                print("Done...")
                options()
            case 3: # Siblings and Cousins
                print_line()
                sac()
                print("Done...")
                options()
            case 4:  # Birthdays and Birthday Calendar
                print_line()
                bcal()
                print("Done...")
                options()
            case 5:  # Average Age
                print_line()
                age()
                print("Done...")
                options()
            case 6:  # Number of Children
                print_line()
                noc()
                print("Done...")
                options()
            case 7:  # Display All family members
                print_line()
                am()
                print("Done...")
                options()
            case 8:  # Exit
                print("Exiting...")
                print_line()
                # Stops the program
                exit(0)
            case _:  # Invalid input
                print("Invalid input. Please enter a number between 1 and 8...")
                options()
    except ValueError: # In case a different data type is provided a ValueError will be raised
        print("Invalid input. Please enter an integer between 1 and 8...")
        options()
