class Student(object):
    """Class for students information"""

    def __init__(self, first_name, last_name, address):
        """Initialize student information"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Class for question & correct answer"""

    def __init__(self, question, correct_answer):
        """Initialize question & correct answer"""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Print question to console and get back user answer. 

        Return True if answer correct, else return False"""

        print self.question
        user_input = raw_input("Add a question: ")
        return user_input == self.answer


class Exam(object):
    """Class for exams (i.e. midtern, final exams)""" 

    def __init__(self, exam_name):
        """Initialize exam information"""

        self.exam_name = exam_name
        self.question = []

    def add_question(self, question, correct_answer):
        """Takes in question & correct answer; adds to exam's question list, .question"""

        add_question = Question(question, correct_answer)

        self.question.append(add_question)

    def administrator(self):
        """Administers the exam questions to return exam score"""

        score = 0

        for question in self.question:
            if answer == question.ask_and_evaluate():
                score += 1
            return score


def take_test(exam, student):
    """Administers exam and assigns score to the student instance"""

    # 


def example():
    """Creates exam, adds questions, creates student, and administers test"""

    # create exam
    exam = exam('final')

    # add questions to exam
    exam.add_question("What is the capital of Egypt?", "Cairo")
    exam.add_question("Where is the Empire State building located?", "New York City")
    exam.add_question("What is 5 + 4?", "9")

    # create student
    student = student('Christina', 'Long', 'Broderick Street')

    # administer exam
    take_test(exam, student)
