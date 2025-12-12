
# This file contains the Tkinter interface for the quiz app
 # Import the Tkinter library for GUI
import tkinter as tk 
# Import the Quiz logic class
from quiz_logic import Quiz  
# Import the list of questions
from quiz_questions import quiz_questions  

# Main GUI application class
class QuizApp:
	def __init__(self, master):
		# Store the main window
		self.master = master  
		# Set window title
		self.master.title("Welcome to Menna's General Knowledge Quiz!")  
		 # Create a Quiz object to manage questions and scoring

		self.quiz = Quiz() 
		# Add all questions from the imported list to the Quiz object
		for q in quiz_questions:
			self.quiz.add_question(q["question"], q["answer"])

		# Track the current question index
		self.current_question = 0 
		# Track the user's score
 
		self.score = 0  
		# Create and pack a label to display the current question
		self.question_label = tk.Label(master, text="")
		self.question_label.pack()

		# Create and pack an entry widget for user input
		self.answer_entry = tk.Entry(master)
		self.answer_entry.pack()

		# Create and pack a button to submit the answer
		self.submit_btn = tk.Button(master, text="Submit", command=self.check_answer)
		self.submit_btn.pack()

		# Create and pack a label to display feedback/results
		self.result_label = tk.Label(master, text="")
		self.result_label.pack()

		# Display the first question
		self.next_question()  

	def next_question(self):
		# If there are more questions, display the next one
		if self.current_question < len(self.quiz.questions):
			# Get the question text
			q = self.quiz.questions[self.current_question]["question"]  
			# Update the label
			self.question_label.config(text=q)  
			 # Clear the entry box
			self.answer_entry.delete(0, tk.END) 
			 # Clear previous feedback
			self.result_label.config(text="") 
		else:
			# If no more questions, show the final score and hide input widgets
			self.question_label.config(text="Quiz finished!")
			# Remove the widget for entering answers 
			self.answer_entry.pack_forget()
			self.submit_btn.pack_forget()
			# show the final score
			self.result_label.config(text=f"Final score: {self.score}/{len(self.quiz.questions)}")

	def check_answer(self):
		# Get the user's answer from the entry box
		user_answer = self.answer_entry.get()
		# Get the correct answer for the current question
		correct = self.quiz.questions[self.current_question]["answer"]
		# Compare answers (case-insensitive)
		if user_answer.strip().lower() == correct.lower():
			# Increment score if correct
			self.score += 1  
			# Show positive feedback
			self.result_label.config(text="Correct!")  
		else:
			 # Show correct answer
			self.result_label.config(text=f"Wrong! Correct: {correct}") 
			  # Move to the next question
		self.current_question += 1
		# Wait 1 second, then show next so that the user has time to see the feedback
		self.master.after(1000, self.next_question)  



