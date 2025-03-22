from datetime import datetime

from models import FamilyTree, Person

# Used ChatGPT to make a fictitious family tree which is placed into a python dictionary:
# Dict based on a persons relationship and children (if applicable)
# Each key - FamilyTree and Person relates to a class in models.py

john_smith2 = Person(29, "John", "Smith", datetime(1969, 5, 15), None)
john_smith = Person(1, "John", "Smith", datetime(1960, 5, 15), None)
emily_smith = Person(2, "Emily", "Smith", datetime(1962, 8, 22), None)
michael_smith = Person(3, "Michael", "Smith", datetime(1985, 1, 14), None)
sophia_smith = Person(4, "Sophia", "Smith", datetime(1987, 9, 11), None)
ethan_smith = Person(5, "Ethan", "Smith", datetime(2010, 3, 17), None)
ella_smith = Person(6, "Ella", "Smith", datetime(2012, 6, 30), None)
clara_smith = Person(7, "Clara", "Smith", datetime(1968, 1, 19), None)
benjamin_smith = Person(8, "Benjamin", "Smith", datetime(1993, 9, 27), None)
william_brown = Person(9, "William", "Brown", datetime(1980, 7, 4), None)
amelia_brown = Person(10, "Amelia", "Brown", datetime(1983, 10, 20), None)
lucas_brown = Person(11, "Lucas", "Brown", datetime(2005, 12, 30), None)
mia_brown = Person(12, "Mia", "Brown", datetime(2008, 9, 14), None)
george_smith = Person(13, "George", "Smith", datetime(1965, 4, 22), None)
lily_johnson = Person(14, "Lily", "Johnson", datetime(1968, 8, 10), datetime(2018, 6, 12))
sarah_jones = Person(15, "Sarah", "Jones", datetime(1970, 3, 12), None)
jake_smith = Person(16, "Jake", "Smith", datetime(1995, 7, 19), None)
alice_smith = Person(17, "Alice", "Smith", datetime(2005, 12, 1), None)
emma_smith = Person(18, "Emma", "Smith", datetime(1963, 9, 30), None)
robert_parker = Person(19, "Robert", "Parker", datetime(1960, 11, 21), datetime(2015, 5, 11))
james_baker = Person(20, "James", "Baker", datetime(1962, 4, 18), None)
david_parker = Person(21, "David", "Parker", datetime(1990, 5, 15), None)
olivia_baker = Person(22, "Olivia", "Baker", datetime(1998, 11, 2), None)
frank_brown = Person(23, "Frank", "Brown", datetime(1955, 3, 29), datetime(2019, 12, 15))
linda_clark = Person(24, "Linda", "Clark", datetime(1958, 5, 12), None)
tom_adams = Person(25, "Tom", "Adams", datetime(1985, 10, 3), None)
chris_miller = Person(26, "Chris", "Miller", datetime(1987, 1, 22), None)
anna_adams_miller = Person(27, "Anna", "Adams-Miller", datetime(2020, 6, 30), None)
casandra_brown = Person(28, "Casandra", "Brown", None, None)  # No Birthdate; not born

# rather than basing it on a persons name, could have used their id for the keys
# but this is more readable and easier to understand -- for me at least
family_members = {
    john_smith.id: FamilyTree(
        person=john_smith,
        spouse=emily_smith,
        children=[michael_smith, sophia_smith, ethan_smith, ella_smith, benjamin_smith],
        siblings=[george_smith, emma_smith]
    ),
    john_smith2.id: FamilyTree(
        person=john_smith2,
        siblings=[john_smith]
    ),
    emily_smith.id: FamilyTree(
        person=emily_smith,
        spouse=john_smith,
        former_spouses=[william_brown],
        children=[michael_smith, sophia_smith, ethan_smith, ella_smith]
    ),
    michael_smith.id: FamilyTree(
        person=michael_smith,
        father=john_smith,
        mother=emily_smith,
        siblings=[sophia_smith, ethan_smith, ella_smith]
    ),
    sophia_smith.id: FamilyTree(
        person=sophia_smith,
        father=john_smith,
        mother=emily_smith,
        siblings=[michael_smith, ethan_smith, ella_smith]
    ),
    ethan_smith.id: FamilyTree(
        person=ethan_smith,
        father=john_smith,
        mother=emily_smith,
        siblings=[michael_smith, sophia_smith, ella_smith]
    ),
    ella_smith.id: FamilyTree(
        person=ella_smith,
        father=john_smith,
        mother=emily_smith,
        siblings=[michael_smith, sophia_smith, ethan_smith]
    ),
    clara_smith.id: FamilyTree(
        person=clara_smith,
        spouse=john_smith,
        children=[benjamin_smith]
    ),
    benjamin_smith.id: FamilyTree(
        person=benjamin_smith,
        father=john_smith,
        mother=clara_smith
    ),
    william_brown.id: FamilyTree(
        person=william_brown,
        spouse=amelia_brown,
        former_spouses=[emily_smith],
        children=[lucas_brown, mia_brown]
    ),
    amelia_brown.id: FamilyTree(
        person=amelia_brown,
        father=frank_brown,
        spouse=william_brown,
        children=[lucas_brown, mia_brown]
    ),
    lucas_brown.id: FamilyTree(
        person=lucas_brown,
        father=william_brown,
        mother=amelia_brown,
        siblings=[mia_brown]
    ),
    mia_brown.id: FamilyTree(
        person=mia_brown,
        father=william_brown,
        mother=amelia_brown,
        siblings=[lucas_brown]
    ),
    george_smith.id: FamilyTree(
        person=george_smith,
        spouse=sarah_jones,
        former_spouses=[lily_johnson],
        children=[jake_smith, alice_smith],
        siblings=[john_smith, emma_smith]
    ),
    lily_johnson.id: FamilyTree(
        person=lily_johnson,
        former_spouses=[george_smith],
        children=[jake_smith]
    ),
    sarah_jones.id: FamilyTree(
        person=sarah_jones,
        spouse=george_smith,
        children=[alice_smith]
    ),
    jake_smith.id: FamilyTree(
        person=jake_smith,
        father=george_smith,
        mother=lily_johnson,
        siblings=[alice_smith]
    ),
    alice_smith.id: FamilyTree(
        person=alice_smith,
        father=george_smith,
        mother=sarah_jones,
        siblings=[jake_smith]
    ),
    emma_smith.id: FamilyTree(
        person=emma_smith,
        spouse=james_baker,
        former_spouses=[robert_parker],
        children=[david_parker, olivia_baker],
        siblings=[john_smith, george_smith]
    ),
    robert_parker.id: FamilyTree(
        person=robert_parker,
        former_spouses=[emma_smith],
        children=[david_parker]
    ),
    james_baker.id: FamilyTree(
        person=james_baker,
        spouse=emma_smith,
        children=[olivia_baker]
    ),
    david_parker.id: FamilyTree(
        person=david_parker,
        father=robert_parker,
        mother=emma_smith,
        siblings=[olivia_baker]
    ),
    olivia_baker.id: FamilyTree(
        person=olivia_baker,
        father=james_baker,
        mother=emma_smith,
        siblings=[david_parker]
    ),
    frank_brown.id: FamilyTree(
        person=frank_brown,
        spouse=linda_clark,
        children=[amelia_brown, casandra_brown]
    ),
    linda_clark.id: FamilyTree(
        person=linda_clark,
        spouse=frank_brown,
        children=[amelia_brown, casandra_brown]
    ),
    tom_adams.id: FamilyTree(
        person=tom_adams,
        spouse=chris_miller,
        children=[anna_adams_miller]
    ),
    chris_miller.id: FamilyTree(
        person=chris_miller,
        spouse=tom_adams,
        children=[anna_adams_miller]
    ),
    anna_adams_miller.id: FamilyTree(
        person=anna_adams_miller,
        father=tom_adams,
        mother=chris_miller
    ),
    casandra_brown.id: FamilyTree(
        person=casandra_brown,
        father=frank_brown,
        mother=linda_clark
    ),
}
