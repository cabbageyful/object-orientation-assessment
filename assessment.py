
"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    Abstraction: Reduces complexity by 

    Encapsulation: 

    Polymorphism:

2. What is a class?

    It is a type of thing. It is a data type, which can be a list, tuple, or file.
    It is a prototype of an object and can help to organize multiple
    but similar or related objects or subclasses.

3. What is an instance attribute?

    It is a characteristic of an instance/object of a class. The instance attribute
    does not belong to the 

4. What is a method?

    A function that exists as a class attribute. 

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.


"""

class AbstractStudent(object):
    """Template for student info. """

    def __init__(self, first_name, last_name, address):
        
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
# Parts 2 through 5:
# Create your classes and class methods
