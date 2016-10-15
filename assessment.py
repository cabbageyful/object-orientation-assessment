
"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    Abstraction: Reduces complexity by creating a simplified version to create from,
        like a template.

    Encapsulation: Reduce repetition and duplicate code that ends up performing
        the same purpose in different places on different things.

    Polymorphism: Flexibility to have similar but differing types of things.

2. What is a class?

    It is a type of thing. It is a data type, which can be a list, tuple, or file.
    It is a prototype of an object and can help to organize multiple
    but similar or related objects or subclasses.

3. What is an instance attribute?

    It is a piece of data that exists on the specfic instance/object of a class,
    not on the class itself.

4. What is a method?

    A function that exists as a class attribute and can be called on instances
    created from the class.

5. What is an instance in object orientation?

    It is an object or specific instance created from a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is data on the class and belongs to all subclasses or
   instances created from the class. An instance attribute is set on the
   instance itself. You would use a class attribute if you know that it is an
   attribute of all subclasses, such as an was_animal attribute on a Meat class.
   However, you would use an instance attribute if it only belongs to that instance,
   such as a can_make_BLT attribute on a bacon instance of Meat.

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

        self.master_q_a = {
            'question': self.question,
            'correct answer': self.answer,
        }

    def ask_question(self):

        student_guess = raw_input(self.question + ' > ')
        student_guess = student_guess.strip()
        if isinstance(self.answer, int):
            try:
                student_guess = int(student_guess)
            except TypeError:
                return False
        elif isinstance(self.answer, float):
            try:
                student_guess = float(student_guess)
            except TypeError:
                return False
        elif isinstance(self.answer, str):
            self.answer = self.answer.lower()
            student_guess = student_guess.lower()

        if self.answer == student_guess:
            return True
        else:
            return False


class AbstractExam(AbstractQuestion):
    """Template for creating an exam. """

    def __init__(self, exam_name, questions=[]):

        self.exam_name = exam_name
        self.exam_questions = questions

    def add_question(self, question, answer):
        """Adds a new question & the answer to the exam instance."""

        new_question = AbstractQuestion(question, answer)

        self.exam_questions.append(new_question)

    def take_exam(self):

        correct_responses = 0

        for q in self.exam_questions:
            test_q = q.ask_question()
            if test_q is True:
                correct_responses += 1

        score = float(correct_responses) / len(self.exam_questions) * 100

        return 'You got {} correct out of {} total, your grade is {:.2f}%'.format(
               correct_responses, len(self.exam_questions), score)
