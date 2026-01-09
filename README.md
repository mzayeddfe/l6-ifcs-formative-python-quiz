

# l6-ifcs-formative-python-quiz

This project is a modular Python quiz application with a graphical interface. It is designed for formative assessment in the Intensive Foundations of Computer Science and Programming course.

## User Documentation

**What is this?**

This is a simple quiz app. When you run it, a window will appear with questions and a text input field for answers. Type your answer and click the "Submit" button. At the end, your score will be shown.

**How do I use it?**
1. [Install dependencies](#installing-dependencies) if you do not already have them.
2. [Run the quiz app](#how-to-run-the-quiz-app)
3. Answer the questions as they appear.
4. At the end, see your score!

## Installing Dependencies

You need Python 3.x installed. Tkinter is usually included with Python. If you have Python, you likely have everything you need.

To install Python, visit: https://www.python.org/downloads/

## How to Run the Quiz App

1. Download or clone this repository to your computer.
2. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and navigate to the project folder. Note if the `l6-ifcs-formative-python-quiz` folder is nested inside other folders, you will need to specify this in the path below before the repository folder and separate them by a `/`:
   ```bash
   cd l6-ifcs-formative-python-quiz
   ```
3. Run the following command:
   ```bash
   python run_quiz.py
   ```
4. The quiz window will appear. Answer the questions and see your score at the end.

## Technical Documentation

- `quiz_logic.py`: Contains the `Quiz` class for managing questions and scoring.
- `quiz_questions.py`: Stores the quiz questions and answers in a list.
- `quiz_gui.py`: Implements the Tkinter graphical interface (`QuizApp` class).
- `run_quiz.py`: Launches the quiz application.

## Developer Manual

- To add or change questions, edit the `quiz_questions` list in `quiz_questions.py`.
- All quiz logic is separated from the interface for easy maintenance and extension.
- You can further extend the app by adding new features or changing the interface in `quiz_gui.py`.
