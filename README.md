
# l6-ifcs-formative-python-quiz

This project is a modular Python quiz application with a graphical interface built using Tkinter. It is designed for formative assessment in the Intensive Foundations of Computer Science and Programming course.

## Project Structure

- `quiz_mod.py`: Contains the `Quiz` class for managing questions and scoring.
- `questions.py`: Stores the quiz questions and answers in a list.
- `quiz_interface.py`: Implements the Tkinter graphical interface (`QuizApp` class).
- `quiz_app_mod.py`: Launches the quiz application.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)


## How to Run the Quiz App

1. Clone this repository to your computer:

	```bash
	git clone https://github.com/<your-username>/l6-ifcs-formative-python-quiz.git
	```


2. Make sure you have Python 3 installed on your system.
3. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and navigate to the project directory:

	```bash
	cd l6-ifcs-formative-python-quiz
	```

4. In the same terminal window, run the following command:

	```bash
	python quiz_app_mod.py
	```

5. The graphical quiz window will appear. Answer each question and your score will be displayed at the end.

## Customizing Questions

To add or change questions, edit the `quiz_questions` list in `questions.py`.

## Notes

- All quiz logic is separated from the interface for easy maintenance and extension.
- You can further extend the app by adding new features or changing the interface in `quiz_interface.py`.
