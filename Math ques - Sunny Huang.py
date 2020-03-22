from tkinter import *
from random import*
from threading import Timer

root = Tk()
root.title("what")
root.geometry("700x500+500+300")

frame1 = Frame(root)
frame2 = Frame(root)
question_box = Label(frame2)
answer_box = Entry(frame2)
answer = ""
response_box = Entry(frame2)


def screen1():
    
    global frame1

    frame2.grid_remove()
    
    frame1 = LabelFrame(root, height = "450", width = "400", bg = "light blue")
    frame1.grid(row = 0, column = 0)
    
    title_label = Label(frame1, bg = "black", fg = "white", width = 20, padx = 30, pady = 10, text = "Welcome to Maths quiz", font = ("Times", "14", "bold italic"))
    title_label.grid(columnspan = 2)
    
    name_label = Label(frame1, bg = "light blue", text = "Name:", width = 10, font=("Times", "14", "bold italic"))
    name_label.grid(row = 1, column = 0)
    
    name_box = Entry(frame1, width = 20)
    name_box.grid(row = 1, column = 1)
    
    age_label = Label(frame1, bg = "light blue", text = "Age:", width = 10, font=("Times", "14", "bold italic"))
    age_label.grid(row = 2, column = 0)    
    
    age_box = Entry(frame1, width = 20)
    age_box.grid(row = 2, column = 1)    
    
    next_buttom = Button(frame1, text = "Next", anchor = W, command = screen2)
    next_buttom.grid(row = 3, column = 1)


def screen2():

    global frame2
    global question_box
    global answer_box
    global response_box
    
    frame1.grid_remove()
    
    frame2 = LabelFrame(root, height = "450", width = "400", bg = "light blue")
    frame2.grid(row = 1, column = 0)
    
    questions_title = Label(frame2, bg= "black", fg = "white", width = 20, padx = 30, pady = 10, text = "Answer Quiz Questions", font = ("Times", "14", "bold italic"))
    questions_title.grid(columnspan = 2)
    
    question_box = Label(frame2, text = "", width = 10, bg = "light blue", font = ("10"))
    question_box.grid(row = 1, column = 0)    
    
    answer_box = Entry(frame2, width = 20)
    answer_box.grid(row = 1, column = 1)    
    
    next_button = Button(frame2, text = "Next Question", anchor = W, command = question_generation)
    next_button.grid(row = 2, column = 0)
    
    home_button = Button(frame2, text = "Home", anchor = W, command = screen1)
    home_button.grid(row = 3, column = 0)
    
    check_button = Button(frame2, text = "Check Answer", anchor = W, command = answer_check)
    check_button.grid(row = 2, column = 1)
    
    response_box = Label(frame2, text = "Are you ready?", width = 30, bg = "light blue", font = ("10"))
    response_box.grid(columnspan = 3)  
       
    question_generation()


def question_generation():
    
    global answer

    x = randrange(10)
    y = randrange(10)
    
    answer = x + y
        
    question = str(x) + " + " + str(y) + "= ?"
    question_box.configure(text = question)
    
    question_box.configure(bg = "light blue")
    frame2.configure(bg = "light blue")
    response_box.configure(text = "Are you ready?", bg = "light blue")
    
    answer_box.focus()
    
    
def background_refresh():

    question_box.configure(bg = "light blue")
    frame2.configure(bg = "light blue")
    response_box.configure(bg = "light blue")
    
    
def answer_check():
    
    try:
        answer_box.get() == float(answer_box.get())
            
        if float(answer_box.get()) == float(answer):
            question_box.configure(bg = "light green")
            frame2.configure(bg = "light green")
            response_box.configure(text = "Well Done!", bg = "light green")
            
            question_generation_countdown()

        else: 
            question_box.configure(bg = "tomato")
            frame2.configure(bg = "tomato")
            response_box.configure(text = str(answer_box.get()) +" is not correct.", bg = "tomato")
            
            background_refresh_countdown()
            
    except:
        
        if len(answer_box.get()) == 0:
            question_box.configure(bg = "orange")
            frame2.configure(bg = "orange")             
            response_box.configure(text = "At least try something!", bg = "orange")    
            
            background_refresh_countdown()
            
        else:
            question_box.configure(bg = "orange")
            frame2.configure(bg = "orange")             
            response_box.configure(text = "Please enter a number!", bg = "orange")
            
            background_refresh_countdown()
        
    answer_box.delete(0, END)
    answer_box.focus()        
        
        
def question_generation_countdown():
    timer = Timer(1.0, question_generation)
    timer.start()
    
    
def background_refresh_countdown():
    timer = Timer(1.0, background_refresh)
    timer.start()    

screen1()   
root.mainloop()