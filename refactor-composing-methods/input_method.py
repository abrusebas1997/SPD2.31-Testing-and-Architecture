LEGAL_DRINKING_AGE = 21

class Person:
    def __init__(self, my_age):
        self.age = my_age

    def can_access_nightclub(self):
        """Checks Person age against the LEGAL_DRINKING_AGE."""
        if self.age >= LEGAL_DRINKING_AGE:
            print("Allowed to enter.")
        else:
            print("Access denied to minors.")

person = Person(20.9)
person.can_access_nightclub()
