import tkinter as tk
from tkinter import messagebox

# Sample quiz questions
questions = [
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus"], "answer": "Mars"}
]

score = 0  # Track the player's score
question_index = 0  # Track current question

# Function to start the quiz
def start_quiz():
    global question_index, score
    question_index = 0
    score = 0
    open_quiz_window()

# Function to open quiz window
def open_quiz_window():
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz")

    def show_question():
        if question_index < len(questions):
            q = questions[question_index]
            question_label.config(text=q["question"])
            for i, option in enumerate(q["options"]):
                buttons[i].config(text=option, command=lambda opt=option: check_answer(opt, quiz_window))
        else:
            messagebox.showinfo("Quiz Finished", f"Your Score: {score}/{len(questions)}")
            quiz_window.destroy()
            update_scoreboard()

    def check_answer(selected_option, window):
        global question_index, score
        if selected_option == questions[question_index]["answer"]:
            score += 1
        question_index += 1
        show_question()

    question_label = tk.Label(quiz_window, text="", font=("Arial", 14))
    question_label.pack(pady=10)

    buttons = [tk.Button(quiz_window, text="", font=("Arial", 12)) for _ in range(3)]
    for btn in buttons:
        btn.pack(pady=5)

    show_question()

# Function to update scoreboard
def update_scoreboard():
    with open("scores.txt", "a") as f:
        f.write(f"Score: {score}/{len(questions)}\n")

def clear_scoreboard():
    with open("scores.txt", "a") as f:
        f.reconfigure('''
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            Score: -/3
            ''')



# Function to view scoreboard
def view_scoreboard():
    scoreboard_window = tk.Toplevel(root)
    scoreboard_window.title("Scoreboard")
    
    tk.Label(scoreboard_window, text="Score History", font=("Arial", 14)).pack()
    
    try:
        with open("scores.txt", "r") as f:
            scores = f.readlines()
            for score in scores:
                label = tk.Label(scoreboard_window, text=score.strip())
                label.pack()
    except FileNotFoundError:
        tk.Label(scoreboard_window, text="No scores recorded yet.").pack()

# Main menu
root = tk.Tk()
root.title("Quiz App")

tk.Label(root, text="Welcome to the Quiz!", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Start Quiz", command=start_quiz).pack(pady=5)
tk.Button(root, text="View Scoreboard", command=view_scoreboard).pack(pady=5)
tk.Button(root, text="Clear Scoreboard", command=clear_scoreboard).pack(pady=5)


root.mainloop()
