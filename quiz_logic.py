
# Define a Quiz class to manage quiz questions and scoring
class Quiz:
    def __init__(self):
        # Initialize an empty list to store questions and answers
        self.questions = []
        # Initialize the user's score to zero
        self.score = 0

    # Add a question and its answer to the quiz
    def add_question(self, question, answer):
        self.questions.append({"question": question, "answer": answer})