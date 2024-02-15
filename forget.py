import tkinter as tk
import re

root = tk.Tk()
root.geometry("1350x700+0+0")
root.config(bg='#ADD8E6')

frame = tk.Frame(root, bg='#D9D9D9', relief=tk.RIDGE)
frame.place(x=400, y=200, width=600, height=400)

title = tk.Label(frame, text="Find your account", font=("Arial", 16, "bold"), fg='blue', bg='#D9D9D9')
title.place(x=140, y=70, width=300, height=40)

instruction = tk.Label(frame, text="Please enter your email to search for your account", font=("Arial", 12),fg='black', bg='#D9D9D9',)
instruction.place(x=80, y=100, width=400, height=40)


email = tk.Entry(frame, text= 'Email', width=30, bg="#C6B9B9")
email.place(x=160, y=180, width=280, height=30)


email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


def validate():
    
    email_input = email.get()
    match = email_input.isdigit() or re.match(email_pattern, email_input)
    if match:
        print(email_input)
        root.destroy()
    else:
        error = tk.Label(frame, text="Invalid email. Please try again.", font=("Arial", 10), fg="red", bg="light grey")
        error.place(x=100, y=180, width=200, height=20)


def cancel():
    
    root.destroy()

cancel_button = tk.Button(frame, text="Cancel", width=10,fg='black', bg='#5280A9', command=cancel)
cancel_button.place(x=180, y=240, width=80, height=30)

submit_button = tk.Button(frame, text="Submit", width=10, fg='black', bg='#5280A9',command=validate)
submit_button.place(x=350, y=240, width=80, height=30)


root.mainloop()
