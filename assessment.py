
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

        self.q_and_a = {
            'Question:': self.question,
            'Correct Answer:': self.answer,
        }

        # Tried to get to show the question & correct answer in a dictionary here, cou.


class AbstractExam(AbstractQuestion):
    """Template for creating an exam. """

    exam_questions = []   # Empty list to add question objects.

    def __init__(self, exam_name):

        self.exam_name = exam_name

    def add_question(self, prompt, correct_answer):
        """Adds a new question & the answer to the exam instance."""

        self.prompt = prompt
        self.correct_answer = correct_answer
        self.new_question = super(AbstractExam, self).__init__(question=self.prompt, answer=self.correct_answer)

        # adds the new question to the list of exam questions
        self.exam_questions.append(self.q_and_a)


