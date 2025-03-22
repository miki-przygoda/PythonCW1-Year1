from dataclasses import dataclass
from datetime import datetime, date
from typing import List



@dataclass
class Person: # defining what each person in the dict will be and what each person has to have to exist
    id: int # id - integer
    first_name: str # first name - string
    surname: str # surname - string
    date_of_birth: datetime | None # Could be an unborn child but doesnt have to be
    date_of_death: datetime | None # Could be a dead person but doesnt have to be
    
    def age(self) -> int: # using this function on a person class object will display their age
        if self.date_of_death is None:
            return date.today() - self.date_of_birth
        return int((self.date_of_death - self.date_of_birth).days / 365)

    def full_name(self, only_surname: bool = False) -> str: # using this function on a person class object will display their full name
        if len(self.surname) == 0:
            return f"{self.first_name}"
        if only_surname:
            return self.surname
        return f"{self.first_name} {self.surname}"




@dataclass
class FamilyTree: # defining what relations each person in the family tree has to have
    person: Person # the person in the family tree
    father: Person | None = None # their father - also a person
    mother: Person | None = None # their mother - also a person
    spouse: Person | None = None # their spouse - also a person
    former_spouses: List[Person] | None = None # their former spouses - also a person
    children: List[Person] | None = None # their children - a list of persons
    siblings: List[Person] | None = None # their siblings - a list of persons

    def full_name(self, only_surname: bool = False) -> str: # using this on a family tree object will display the full name of the person in the family tree
        return self.person.full_name(only_surname)


