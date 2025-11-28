#create a Quiz class to manage quiz questions and scoring
class Quiz:
    def __init__(self):
        # Initialize an empty list to store questions and answers
        self.questions = []
        # Initialize the user's score to zero
        self.score = 0

#create a function that appends questions and answers to a list
    def add_question(self, question, answer):
        # Add a tuple containing the question and its correct answer to the list
        self.questions.append({"question": question, "answer": answer})
# create a function that starts the quiz and tracks the score
    def start_quiz(self):
        # Display a welcome message at the start of the quiz
        print("Welcome to Menna's General Knowledge Quiz!")
        # Loop through each question and answer pair
        for qa in self.questions:
            question = qa["question"]
            answer = qa["answer"]
            # Prompt the user for their answer
            user_answer = input(question + " ")
            # Check if the user's answer matches the correct answer (case-insensitive)
            if user_answer.lower() == answer.lower():
                print("Correct!")  # Inform the user they are correct
                self.score += 1    # Increment the score
            else:
                # Inform the user of the correct answer if they are wrong
                print(f"Wrong! The correct answer is: {answer}")
        # After all questions, display the user's final score
        print(f"Your final score is: {self.score}/{len(self.questions)}")