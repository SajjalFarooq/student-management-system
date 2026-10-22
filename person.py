# person.py
# Mini definition: A base class is a parent class that other classes inherit from.
# Person stores only the data that every person has, so Student can reuse it
# instead of writing the same code again.


class Person:
    """A base class for a person."""

    def __init__(self, name):
        # self.name is an instance attribute: data stored in this object only.
        self.name = name

    def introduce(self):
        # This method returns a simple introduction using the stored name.
        return f"I am {self.name}."
