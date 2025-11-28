
# Import the tkinter library for creating graphical user interfaces
import tkinter as tk

# Define a class for the quiz application
class QuizApp:
    def __init__(self, master):
        # Store the main window (root)
        self.master = master
        # Set the window title
        self.master.title("Quiz")

        # List of questions and answers (each is a dictionary)
        self.questions = [
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "Capital of France?", "answer": "Paris"}
        ]
        # Track the user's score
        self.score = 0
        # Track which question the user is on
        self.current = 0

        # Create a label to display the question
        self.question_label = tk.Label(master, text="")
        self.question_label.pack()

        # Create an entry box for the user to type their answer
        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()

        # Create a button to submit the answer
        self.submit_btn = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_btn.pack()

        # Create a label to show feedback (correct/wrong)
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        # Show the first question
        self.next_question()

    # Function to display the next question or finish the quiz
    def next_question(self):
        if self.current < len(self.questions):
            # Get the current question text
            q = self.questions[self.current]["question"]
            # Update the question label
            self.question_label.config(text=q)
            # Clear the answer entry box
            self.answer_entry.delete(0, tk.END)
            # Clear the result label
            self.result_label.config(text="")
        else:
            # If no more questions, show final score and hide input widgets
            self.question_label.config(text="Quiz finished!")
            self.answer_entry.pack_forget()
            self.submit_btn.pack_forget()
            self.result_label.config(text=f"Final score: {self.score}/{len(self.questions)}")

    # Function to check the user's answer
    def check_answer(self):
        # Get the user's answer from the entry box
        user_answer = self.answer_entry.get()
        # Get the correct answer for the current question
        correct = self.questions[self.current]["answer"]
        # Compare answers (case-insensitive)
        if user_answer.strip().lower() == correct.lower():
            self.score += 1  # Increase score if correct
            self.result_label.config(text="Correct!")
        else:
            self.result_label.config(text=f"Wrong! Correct: {correct}")
        # Move to the next question after a short delay
        self.current += 1
        self.master.after(1000, self.next_question)

# This code runs the quiz app if the script is executed directly
if __name__ == "__main__":
    root = tk.Tk()           # Create the main window
    app = QuizApp(root)      # Create the quiz application
    root.mainloop()          # Start the Tkinter event loop
