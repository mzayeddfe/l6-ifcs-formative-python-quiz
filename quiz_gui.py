
# This file contains the Tkinter interface for the quiz app
import tkinter as tk
from quiz_logic import Quiz
from quiz_questions import quiz_questions

class QuizApp:
	def __init__(self, master):
		self.master = master
		self.master.title("Welcome to Menna's General Knowledge Quiz!")
		self.quiz = Quiz()
		for q in quiz_questions:
			self.quiz.add_question(q["question"], q["answer"])
		self.current_question = 0
		self.score = 0
		self.question_label = tk.Label(master, text="")
		self.question_label.pack()
		self.answer_entry = tk.Entry(master)
		self.answer_entry.pack()
		self.submit_btn = tk.Button(master, text="Submit", command=self.check_answer)
		self.submit_btn.pack()
		self.result_label = tk.Label(master, text="")
		self.result_label.pack()
		self.next_question()
	def next_question(self):
		if self.current_question < len(self.quiz.questions):
			q = self.quiz.questions[self.current_question]["question"]
			self.question_label.config(text=q)
			self.answer_entry.delete(0, tk.END)
			self.result_label.config(text="")
		else:
			self.question_label.config(text="Quiz finished!")
			self.answer_entry.pack_forget()
			self.submit_btn.pack_forget()
			self.result_label.config(text=f"Final score: {self.score}/{len(self.quiz.questions)}")
	def check_answer(self):
		user_answer = self.answer_entry.get()
		correct = self.quiz.questions[self.current_question]["answer"]
		if user_answer.strip().lower() == correct.lower():
			self.score += 1
			self.result_label.config(text="Correct!")
		else:
			self.result_label.config(text=f"Wrong! Correct: {correct}")
		self.current_question += 1
		self.master.after(1000, self.next_question)



