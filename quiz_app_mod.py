
# Import the tkinter library for creating graphical user interfaces
import tkinter as tk

from quiz_interface import QuizApp
# # Define a class for the quiz application window
# class QuizApp:
#     def __init__(self, master):
#         # Store the main window (root)
#         self.master = master
#         # Set the window title
#         self.master.title("Welcome to Menna's General Knowledge Quiz!")

#         # Create a Quiz object to manage questions and scoring
#         self.quiz = Quiz()
#         # Add questions from the imported list
#         for q in quiz_questions:
#             self.quiz.add_question(q["question"], q["answer"])

#         # Track which question the user is currently on
#         self.current_question = 0
#         # Track the user's score
#         self.score = 0

#         # Create a label to display the current question
#         self.question_label = tk.Label(master, text="")
#         self.question_label.pack()

#         # Create an entry box for the user to type their answer
#         self.answer_entry = tk.Entry(master)
#         self.answer_entry.pack()

#         # Create a button to submit the answer
#         self.submit_btn = tk.Button(master, text="Submit", command=self.check_answer)
#         self.submit_btn.pack()

#         # Create a label to show feedback (correct/wrong)
#         self.result_label = tk.Label(master, text="")
#         self.result_label.pack()

#         # Show the first question
#         self.next_question()

#     # Function to display the next question or finish the quiz
#     def next_question(self):
#         # If there are more questions left
#         if self.current_question < len(self.quiz.questions):
#             # Get the current question text
#             q = self.quiz.questions[self.current_question]["question"]
#             # Update the question label with the current question
#             self.question_label.config(text=q)
#             # Clear the answer entry box
#             self.answer_entry.delete(0, tk.END)
#             # Clear the result label
#             self.result_label.config(text="")
#         else:
#             # If no more questions, show final score and hide input widgets
#             self.question_label.config(text="Quiz finished!")
#             self.answer_entry.pack_forget()
#             self.submit_btn.pack_forget()
#             self.result_label.config(text=f"Final score: {self.score}/{len(self.quiz.questions)}")

#     # Function to check the user's answer
#     def check_answer(self):
#         # Get the user's answer from the entry box
#         user_answer = self.answer_entry.get()
#         # Get the correct answer for the current question
#         correct = self.quiz.questions[self.current_question]["answer"]
#         # Compare answers (case-insensitive)
#         if user_answer.strip().lower() == correct.lower():
#             self.score += 1  # Increase score if correct
#             self.result_label.config(text="Correct!")
#         else:
#             self.result_label.config(text=f"Wrong! Correct: {correct}")
#         # Move to the next question after a short delay
#         self.current_question += 1
#         self.master.after(1000, self.next_question)

# This code runs the quiz app if the script is executed directly
if __name__ == "__main__":
    root = tk.Tk()           # Create the main window
    app = QuizApp(root)      # Create the quiz application
    root.mainloop()          # Start the Tkinter event loop

