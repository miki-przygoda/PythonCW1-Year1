from datetime import datetime

from family_tree import family_members as fm
from models import FamilyTree

"""
What feature would you like to access:
    1) Parents and Grandparents - School partner -- not a part of this repo
    2) Immediate and extended family - School partner -- not a part of this repo
    3) Siblings and Cousins - Done
    4) Birthdays and Birthday Calendar - Done
    5) Average Age - Done
    6) Number of Children - Done
    7) Display All family members - Done
    8) Exit - Done
"""

"""
F1 - School partner
F2 - Mikolaj
F3 - Mikolaj

We need functions to:
F1a:
    Select an individual and return their parents
    Select an individual and return their grandchildren - children of their children
F1b:
    Select an individual and return their immediate family - their parents, siblings, spouse and children(many)
    Select an individual and return their extended family - anyone that is alive; their aunts,uncles and cousins
F2a:
    Select an individual and return their siblings
    Select an individual and return their cousins
F2b:
    Select all individuals and display their birthday
    Ignoring the year of birth, sort the birthdays in order to create a birthday calendar;
    If more than one person has a birthday on one day merge them
F3a:
    Integrate two branches to form the full family tree.
    Create an integrated program which contains both branches
    Test the output of the program with the individuals from the other branch
    Find the average age of death of any dead people from both branches combined
F3b:
    Find the number of children for each individual
    Find the average number of children per person in the each family tree
"""

def print_line(): # Purely visual function to print a line of dashes a certain number of times which makes changing it easier
    print("-" * 60)



def options(): # Prints the interface for the user to select one of the options available
    print_line()
    print("""
What feature would you like to access:
    1) Parents and Grandparents -- Not available
    2) Immediate and extended family -- Not available
    3) Siblings and Cousins
    4) Birthdays and Birthday Calendar
    5) Average Age of Death
    6) Number of Children
    7) Display All family members
    8) Exit
    """)
    print_line()



def all_members(): # Prints all the family members in the family tree
    for person_id, info in fm.items():
        person = info.person
        # Printing details from the Person object
        print("First Name:", person.first_name)
        print("Last Name:", person.surname)
        print_line()



#F2a: - Done - Mikolaj
def siblings_and_cousins(): # Takes a user input to select either siblings or cousins of a person of their choosing
    choice = 0
    while choice < 1 or choice > 2:
        print("""     1) Siblings 
     2) Cousins
Please enter your choice: """)
        try: # ensures that the user enters a numeric value
            print_line()
            choice = int(input("Which option would you like to access: "))
            print_line()
            if 1 <= choice <= 2:
                family_member = find_family_tree_by_member()
                # used to find the family member by their first name and checks for multiple instances of the same name

                if choice == 1: # Siblings
                    siblings = family_member.siblings if family_member.siblings else "N/A"
                    if siblings != "N/A": # if siblings exist
                        sibling_names = ", \n".join(f"{sibling.first_name} {sibling.surname}" for sibling in siblings)
                        print(f"{family_member.full_name()} has {len(siblings)} siblings and their names are: \n{sibling_names}") # prints the siblings of the family member on new lines
                        print_line()
                    else:
                        print(f"{family_member.full_name()} has no siblings.") # in case the family member has no siblings
                        print_line()


                if choice == 2: # Cousins
                    cousins = [] # defining the list in which the cousins will be stored
                    father = family_member.father # finding the father of the family member
                    mother = family_member.mother # finding the mother of the family member
                    extended_family = [] # defining the list in which the extended family will be stored -
                    # the fathers and mothers siblings and their children which are the cousins of the family member
                    # we find the people by id and then append them to the list
                    if father and father.id in fm:
                        # appends the extended family list with the persons father's siblings
                        extended_family.extend(fm[father.id].siblings if fm[father.id].siblings else [])
                    if mother and mother.id in fm:
                        # appends the extended family list with the persons mother's siblings
                        extended_family.extend(fm[mother.id].siblings if fm[mother.id].siblings else [])
                    for relative in extended_family:
                        if relative.id in fm:
                            # for each person in the extended family list filled with the persons aunts and uncles it finds their children if they have any
                            children = fm[relative.id].children
                            if children:
                                cousins.extend(children)
                    if cousins:
                        cousin_names = ", \n".join(f"{cousin.first_name} {cousin.surname}" for cousin in cousins)
                        print(f"{family_member.full_name()} has {len(cousins)} cousins and their names are: \n{cousin_names}")
                        print_line()
                    else:
                        print(f"{family_member.full_name()} has no cousins.")
                        print_line()
            else:
                print("That's not one of the choices...")
                print_line()
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            print_line()



#F2b: - Done - Mikolaj
def birthday_calendar():
    count = 0
    choice = 0
    while choice < 1 or choice > 2:
        print("""     1) All Birthdays \n     2) Sort Birthdays
Please enter your choice: """)
        try:
            print_line()
            choice = int(input("Which option would you like to access: "))
            print_line()
            if 1 <= choice <= 2:
                if choice == 1:
                    for person_id, info in fm.items():
                        person = info.person
                        if person.date_of_birth is None:
                            count = count + 1 # Counting how many people have not been born yet...
                            pass
                        else:
                            person_birthday = (person.date_of_birth.strftime("%d/%m"))
                            print(f"{person.first_name} {person.surname}'s birthday is on: \n{person_birthday}")
                            print_line()

                    print(str(count) + " person(s) has not been born yet...")
                    print_line()
                if choice == 2:
                    b_days = []
                    repeats = [0] # To be used if there are multiple people with the same birthday
                    current = None
                    for person_id, info in fm.items():
                        person = info.person
                        if person.date_of_birth is not None:
                            person_birthday = person.date_of_birth.strftime("%d %B")
                            b_days.append((person.full_name(), person_birthday, repeats))
                    b_days.sort(key=lambda x: datetime.strptime(x[1], "%d %B"))
                    i = 0
                    without_repeats = []
                    while i < len(b_days):
                        current = b_days[i]
                        current_person = current[0]
                        current_birthday = current[1]
                        repeats = 1

                        while i + 1 < len(b_days) and b_days[i + 1][1] == current_birthday:
                            current_person += f" and {b_days[i + 1][0]}"
                            repeats = repeats + 1
                            i = i + 1

                        without_repeats.append((current_person, current_birthday, repeats))
                        i = i + 1

                    for element in without_repeats:
                        month_and_day = element[1]
                        month = month_and_day[3:]
                        day = month_and_day[:2]
                        person = element[0]
                        if month != current:
                            current = month
                            print(f"\n{current}:")
                        print(f"{person}'s birthday is on: {day}")
                    print_line()
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            print_line()



#F3a: - Done - Mikolaj
def average_age():
    count = 0 # defining the count, to count how many people have died
    age_sum = 0 # defining the sum of the ages of the people who have died
    # These two will be used to find the average age of death - sum of all ages at death divided by the number of people who died

    for person_id, info in fm.items():
        person = info.person
        if person.date_of_death is None:
            continue

        count = count + 1

        print(f"{person.full_name()} died at the age of, {person.age()}")
        age_sum += person.age() # adding the age of the person to the sum of the ages of the people who have died
    average_age_of_death = age_sum / count # dividing by the number of people to get the average age of death
    print(f"So the average age of death is: {round(average_age_of_death)}")
    print_line()



#F3b: - Done - Mikolaj
def number_of_children(): # Prints the number of children each family member has
    while True:
        family_member = find_family_tree_by_member()
        children = family_member.children if family_member.children else "N/A"

        if children != "N/A":
            children_names = ", \n".join(f"{children.first_name} {children.surname}" for children in children)
            print(f"{family_member.full_name()} has {len(children)} children and their names are: \n{children_names}")
            print_line()
        else:
            print(f"{family_member.full_name()} has no children.")
            print_line()
        break



def find_family_member_by_first_name(first_name: str) -> FamilyTree | None | list[FamilyTree]:
    # Searches for a family member in the dictionary by their first name.
    # Stores names matching the firstname in the dict in the list
    repeats = [] # List to store the family members with the same first name
    for member in fm.values():
        if member.person.first_name.lower() == first_name.lower():
            repeats.append(member)
            continue
    if len(repeats) == 1: # if only one member is found
        first = repeats.pop(0)
        return first # return the first member found as a FamilyTree object
    if len(repeats) > 1:
        return repeats # return the list of members with the same first name
    return None # return None if no member is found



def find_family_tree_by_member() -> FamilyTree:
    """
    A function to check for the existence of the chosen family member by first name,
    then checks for multiple instances of the same name of a family member and checks with the user which one they meant.
    The function will return a FamilyTree object which can be stored as a variable and called/used in other functions.
    This allows us to access the class methods and attributes of the FamilyTree object and use them.
    """

    while True:
        member_name = input("Please enter the name of a family member: ")
        family = find_family_member_by_first_name(member_name)
        if family is None:
            if member_name == "":
                print("You didn't even try to enter a name...")
            else:
                print(f"{member_name} does not exist in the family tree...")
            continue
        if isinstance(family, list): # Used the web to find this builtin function to check if the object is a list
            if len(family) > 1:
                print(f"There are multiple family members with the name {member_name}.")
                print("Please select one of the following:")
                print_line()
                # for count, member in enumerate(family, start=1): # Starting at 1 as lists start at 0,
                # and we want to display 1 as the first option to the user
                #     print(f"{count}) Name: {member.person.first_name} {member.person.surname} and their ID: {member.person.id}")
                while True:
                    try: # catch in case a non-numeric value is entered
                        for count, member in enumerate(family , start=1):   
                            print(f"{count}) Name: {member.person.first_name} {member.person.surname} and their ID: {member.person.id}")
                        member_num = int(input("Please enter the number next to the right family member: "))
                        print_line()
                        if 1 <= member_num <= len(family): # We make sure that the number falls between one and the length of the list
                            return family[member_num - 1] # We return the family member that the user selected - we need to take away 1 as lists start at 0
                            # and we displayed the options starting at 1
                        else:
                            print("Not one of the options, please try again...")
                            print_line()
                    except ValueError:
                        print_line()
                        print("Invalid input, please enter an integer...")
                        print_line()
        else:
            return family

# Wanted to make functions to find each individual relation of a given family member but decided it would add unnecessary complexity to the program
"""
# Done
def parents():
    family_member = find_family_tree_by_member()
    both_parents = []
    if family_member is not None:
        both_parents.append(family_member.father.first_name)
        both_parents.append(family_member.mother.first_name)
        both_parents_joint = ' and '.join(both_parents)
        print(f"{family_member.person.first_name}'s parents are {both_parents_joint}")
        # return both_parents_joint
    else:
        return None

# Started
def siblings():
    family_member = find_family_tree_by_member()
    family_members_siblings = set()
    if family_member is not None:
        family_members_siblings.add(family_member.siblings)
        if family_member.mother is not None:
            from_mother = family_member.mother
            siblings_from_mother = from_mother.FamilyTree.siblings
            family_members_siblings.add(siblings_from_mother)
        if family_member.father is not None:
            from_father = family_member.father
            siblings_from_father = from_father.FamilyTree.siblings
            family_members_siblings.add(siblings_from_father)

        all_siblings_joint = ' and '.join(family_members_siblings)
        print(f"{family_member.person.first_name}'s siblings are {all_siblings_joint}")
    else:
        return None

# To be made
def children():
    pass

# To be made
def cousins():
    pass

# To be made
def aunts_and_uncles():
    pass

# To be made
def grandparents():
    pass
"""