from tkinter import *
from tkinter import messagebox


## Window Settings
  
window1 = Tk()
window1.title("Window 1 - Dark green")
window1.geometry("500x500")
window1.configure(bg='#336639')
window1.iconbitmap("images/athleticclub.ico")
Label(window1, text="Welcome to the Quizz App", font=('Arial', 20)).pack(pady=20)

## Sample Questions
questions = [
    {"question": "What is 2+2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "What is the capital of France", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
    {"question": "What planet is known as the red planet?", "options": ["Jupiter", "Venus", "Mars"], "answer": "4"},
]


## Global Variables 

score = 0 #initialize player's score
question_index =  0 #initializing the question index


#function the start the quiz
def start_quiz():
    global question_index, score
    question_index=0 #resetting the question index
    score=0 #ressetting the score
    open_quiz_windows()

Button(window1, text="Start Quiz!", command=start_quiz, font=('Arial', 14)).pack(pady=10)

# function to open the quiz window
def open_quiz_windows():
    quiz_window = Toplevel(window1)
    quiz_window.title("Quiz")

    #function to display the question and options
    def show_question():
        if question_index < len(questions): #if there are still more questions
            q = questions[question_index] #get the current question from the list
            question_label.config(text=q["question"]) #set the question label text
            for i, option in enumerate(q["question"]):
                buttons[i].config(text=option, command=lambda opt=option: check_answer(opt, quiz_window))#set the options button text and command
        else:
            messagebox.showinfo("Quiz finished!", f"Your score is {score} / {len(questions)}")
            quiz_window.destroy() #close the window when the quiz is finished
            update_scoreboard()

    def check_answer(selected_option, quiz_window):
        global question_index, score
        if selected_option == questions[question_index]["answer"]:
            score+=1 #increase the score if the answer is correct
        question_index += 1 #increase the question index as we move forward
        show_question() #ask for the next question

    question_label = Label(quiz_window, text="", font=("Arial", 14))
    question_label.pack(pady=10)
    
    buttons = [Button(quiz_window, text="", font=('Arial', 12)) for _ in range(3)]

    for btn in buttons:
        btn.pack(pady=5)

    show_question()

## close of open_quiz_window function

#function to update the scoreboard
def update_scoreboard():
    with open("scores.txt", "a") as f: # appending or writing only to the file
        f.write(f"Score: {score}/{len(questions)}\n")
        
def view_scoreboard():
    scoreboard_window = Toplevel(window1)
    scoreboard_window.title("Scoreboard")

    Label(scoreboard_window, text="Scoreboard", font=("Arial", 14)).pack(pady=10)
    try:
        with open("scores.txt", "r") as f: #reads the file only
            scores = f.readlines
            for score in scores:  #extract scores and display them in a label
                Label(scoreboard_window, text=score.strip().pack(pady=5))
    except FileNotFoundError:
        Label(scoreboard_window, text= "No scores available yet").pack(pady=10)

Button(window1, text="View Scoreboard", command=view_scoreboard).pack(pady=10)


##  Run Window

window1.mainloop()
