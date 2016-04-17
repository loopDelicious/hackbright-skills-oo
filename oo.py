"""Object-orientation Skills assessment"""

# Part 1: Discussion

# Answer each question in your own words.

# What are the three main design advantages that object orientation can provide?
    # Encapsulation
    # Abstraction
    # Polymorphism 

# Explain each concept.
    # Encapsulation is bundling similar functionality and attributes
    # Abstraction is knowing only what you need to know, and simplifying complexity
    # Polymorphism is building flexibility into programs 

# What is a class?
    # A class is like a type for objects that may have similar class attributes

# What is an instance attribute?
    # It's a function or trait that belongs to an instance (object)

# What is a method?
    # A function that belongs to a class

# What is an instance in object orientation?
    # An object that is instantiated within a parent class

# How is a class attribute different than an instance attribute? 
# Give an example of when you might use each.
    # Class attributes apply to an entire class, and will also apply to 
    # instances within a class unless specified otherwise.  Instance attributes
    # apply to the single instance and will precede any class attributes.  
    # If 
    # instance attributes have not been specified, attributes will defer to the
    # parent class attribues.  If all instances of a class have a similar 
    # attribute, it can be defined as a class attribute. If there is a unique 
    # attribute that applies only to an instance, like name, it can be defined 
    # as an instance attribute.
 
class Student:
    """ Student class"""

    def __init__(self, first_name, last_name, address):
        """Initialize an instance of Student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question:
    """Question class"""

    def __init__(self, question, answer):
        """Initialize an instance of Question class"""

        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        """Prompts the user to answer a question and returns True or False"""

        user_answer = raw_input(self.question)
        if user_answer.lower() == self.answer.lower():
            print "That's correct!"
            return True
        else:
            print "Sorry, no."
            return False


class Exam:
    """Exam class"""

    def __init__(self, name):
        """Initialize an instance of Exam class"""

        self.name = name
        self.questions = []


    def add_question(self, question, correct_answer):
        """Makes a question and adds to the exam's list of questions"""

        question_instance = Question(question, correct_answer)

        self.questions.append(question_instance)
       


    def administer(self):
        """Administer exam with all questions"""

        score = 0

        for question_instance in self.questions:
            instance_answer = question_instance.ask_and_evaluate()
            if instance_answer == True:
                score += 1

        return score

# Part 4: Create an actual exam!

def take_test(exam, student):
    """Runs a new test"""

    score = exam.administer()
    student.score = score


def example():
    """Creates and administers an exam"""

    example_exam = Exam("Capitals Exam")

    example_exam.add_question("What is the capital of California? ", "Sacramento")
    example_exam.add_question("What is the capital of Colorado? ", "Denver")
    example_exam.add_question("What is the capital of Illinois? ", "Springfield")

    example_student = Student("Joyce", "Lin", "San Francisco")

    example_student.score = example_exam.administer()

    print example_student.score


# Part 5: Inheritance
class Quiz(Exam):
    """Quizzes are pass/fail grading"""

    def administer(self):

        score = super(Quiz, self).administer()

        passing_mark = len(questions) / 2
        if score > passing_mark:
            print "You passed!"
            return True

        print "You failed!"
        return False



example()
 