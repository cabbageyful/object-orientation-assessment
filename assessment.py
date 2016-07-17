
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
# Parts 2 through 5:
# Create your classes and class methods


class AbstractStudent(object):
    """Returns student first & last name, address in a dictionary. """

    def __init__(self, first_name, last_name, address):
        """Creates new student as an object in the program."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

        # Creates dictionary for each student with the label & info.

        self.info = {
            'first name': self.first_name,
            'last name': self.last_name,
            'address': self.address,
        }


jasmine = AbstractStudent('Jacqui', 'Console', '888 Binary Ave')


class AbstractQuestion(object):
    """Template for adding separate questions as their own object w/ answer. """

    def __init__(self, question, answer):
        """Adds the question & answer attributes to each new object."""

        self.question = question
        self.answer = answer

        # Will show the question & correct answer in a dictionary.

        self.correct_answer = {
            'question': self.question,
            'correct_answer': self.answer
        }


trick = AbstractQuestion('What is your favorite color?', 'Nobody cares.')


class AbstractExam(object):
    """Template for creating an exam. """

    def __init__(self, exam_name):

        self.exam_name = exam_name
        self.questions = []   # Empty list to add question objects.

        self.grading_guide = {
            'name': self.exam_name,
            'questions': self.questions
        }


        





