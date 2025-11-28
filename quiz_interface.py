# import the Quiz class from quiz_mod.py
from quiz_mod import Quiz 
#import tkinter as tk
import tkinter as tk
quiz = Quiz()
# Add questions to the quiz
quiz.add_question("What tech uses sound waves to detect objects?", "Sonar")
quiz.add_question("In pounds, how much did a third-class ticket on the Titanic cost?", "7")
quiz.add_question("Guernica is a famous painting by which artist?", "Picasso")
quiz.add_question("What is the capital of Australia?", "Canberra")
quiz.add_question("What is the largest planet in our solar system?", "Jupiter")
quiz.add_question("How many mins are in a half a day?", "720")
quiz.add_question("What is the chemical symbol for gold?", "Au")
# Start the quiz
quiz.start_quiz()