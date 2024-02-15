from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import re

class Register:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#ADD8E6')

        frame1 = Frame(self.root, bg='white')
        frame1.place(x=480, y=100, width=700, height=500)
        frame1.config(bg='#151E4C')

        self.bg = ImageTk.PhotoImage(file='kasa.png')
        bg = Label(self.root, image=self.bg)
        bg.place(x=950, y=120)

        title = Label(frame1, text="REGISTER HERE ", font=("times new roman", 20,), bg="#151E4C", fg="Green")
        title.place(x=50, y=30)

        txt = Label(frame1, text="It's Quick And Easy", font=("times new roman", 15,), bg="#151E4C", fg="Gray")
        txt.place(x=70, y=60)
    
        f_name_label = Label(frame1, text="First Name", font=("times new roman", 15), bg="#151E4C", fg="Gray")
        f_name_label.place(x=50, y=100)
        self.f_name_entry = Entry(frame1, font=("times new roman", 15), bg="#AE9898")
        self.f_name_entry.place(x=50, y=130, width=250)

        l_name_label = Label(frame1, text="Last Name", font=("times new roman", 15), bg="#151E4C", fg="Gray")
        l_name_label.place(x=370, y=100)
        self.l_name_entry = Entry(frame1, font=("times new roman", 15), bg="#AE9898")
        self.l_name_entry.place(x=370, y=130, width=250)

        contact_label = Label(frame1, text="Mobile Number Or Email", font=("times new roman", 15), bg="#151E4C", fg="Gray")
        contact_label.place(x=50, y=170)
        self.contact_entry = Entry(frame1, font=("times new roman", 15), bg="#AE9898")
        self.contact_entry.place(x=50, y=200, width=570)

        password_label = Label(frame1, text="Password", font=("times new roman", 15), bg="#151E4C", fg="Gray")
        password_label.place(x=50, y=240)
        self.password_entry = Entry(frame1, font=("times new roman", 15), bg="#AE9898")
        self.password_entry.place(x=50, y=270, width=570)

        DOB = Label(frame1, text="Date Of Birth", font=("times new roman",15), bg="#151E4C", fg="Gray")
        DOB.place(x=50, y=311)

        self.Day = Entry(frame1, width=25, fg='Gray', border=0, bg='#AE9898', font=("times new roman", 15))
        self.Day.place(x=50, y=340, width=120)
        self.Day.insert(0, 'Day')
        self.Day.bind('<FocusIn>', self.on_enter_Day)
        self.Day.bind('<FocusOut>', self.on_leave_Day)

        self.Months = Entry(frame1, width=25, fg='Gray', border=0, bg='#AE9898', font=("times new roman", 15))
        self.Months.place(x=250, y=340, width=130)
        self.Months.insert(0, 'Months')
        self.Months.bind('<FocusIn>', self.on_enter_months)
        self.Months.bind('<FocusOut>', self.on_leave_months)

        self.Year = Entry(frame1, width=25, fg='Gray', border=0, bg='#AE9898', font=("times new roman", 15))
        self.Year.place(x=450, y=340, width=120)
        self.Year.insert(0, 'Year')
        self.Year.bind('<FocusIn>', self.on_enter_Year)
        self.Year.bind('<FocusOut>', self.on_leave_Year)


        self.show_password_var = BooleanVar()
        self.show_password_var.set(False)

        show_password_checkbox = Checkbutton(frame1, text="Show Password", variable=self.show_password_var,
                                             onvalue=True, offvalue=False, font=("times new roman", 14),
                                             padx=5,pady=5 , bg="#151E4C", fg="Gray", command=self.show_password)
        show_password_checkbox.place(x=520, y=270)

        Gender = Label(frame1, text="Gender", font=("times new roman", 15), bg="#151E4C", fg="Gray")
        Gender.place(x=50, y=374)

        self.selected_gender = StringVar()

        male_checkbox = Checkbutton(frame1, text="Male", variable=self.selected_gender, onvalue="Male", offvalue="",
                                    font=("times new roman", 15), bg="#151E4C", fg="Gray", padx=5, pady=5,
                                    activebackground="#151E4C", activeforeground="Gray", command=self.show_selected_gender)
        male_checkbox.place(x=50, y=395)

        female_checkbox = Checkbutton(frame1, text="Female", variable=self.selected_gender, onvalue="Female",
                                      offvalue="", font=("times new roman", 15), bg="#151E4C", fg="Gray",
                                      padx=5, pady=5, activebackground="#151E4C", activeforeground="Gray", command=self.show_selected_gender)
        female_checkbox.place(x=135, y=395)

        custom_checkbox = Checkbutton(frame1, text="Custom", variable=self.selected_gender, onvalue="Custom",
                                      offvalue="", font=("times new roman", 15), bg="#151E4C", fg="Gray",
                                      padx=5, pady=5, activebackground="#151E4C", activeforeground="Gray", command=self.show_selected_gender)
        custom_checkbox.place(x=245, y=395)

        sign_in = Button(frame1, width=20, text='Sign In', border=0, bg='#407AD1', cursor='hand2', fg='black',
                         font=("times new roman", 15), command=self.show_selected_sign)
        sign_in.place(x=240, y=450)
        # self.root.destroy()


    def on_enter_Day(self, e):
        if self.Day.get() == 'Day':
            self.Day.delete(0, 'end')

    def on_leave_Day(self, e):
        if self.Day.get() == '':
            self.Day.insert(0, 'Day')

    def on_enter_months(self, e):
        if self.Months.get() == 'Months':
            self.Months.delete(0, 'end')

    def on_leave_months(self, e):
        if self.Months.get() == '':
            self.Months.insert(0, 'Months')

    def on_enter_Year(self, e):
        if self.Year.get() == 'Year':
            self.Year.delete(0, 'end')

    def on_leave_Year(self, e):
        if self.Year.get() == '':
            self.Year.insert(0, 'Year')

    def show_selected_gender(self):
        print("Selected gender:", self.selected_gender.get())

    def show_selected_sign(self):
        if self.validate_fields():  # Validate form fields
            messagebox.showinfo("Success", "Sign in successful!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def validate_fields(self):
        # Add validation logic for form fields
        if (self.f_name_entry.get() and self.l_name_entry.get() and self.contact_entry.get() and
                self.password_entry.get() and self.Day.get() != 'Day' and self.Months.get() != 'Months') :
            # Check password requirements
            password = self.password_entry.get()
            if self.check_password_requirements(password):
                print("Passwords entered:")
                print("First Name:", self.f_name_entry.get())
                print("Last Name:", self.l_name_entry.get())
                print("Mobile Number or Email:", self.contact_entry.get())
                print("Password:", password)
                print("Day:", self.Day.get())
                print("Month:", self.Months.get())
                print("Year:", self.Year.get())
                return True
            else:
                messagebox.showerror("Error", "Password must contain at least one number, one special character, and one alphabet.")
                return False
        else:
            return False
        
    
    def check_password_requirements(self, password):
        # Password must contain at least one number, one special character, and one alphabet
        if re.search(r"(?=.*\d)(?=.*\W)(?=.*[a-zA-Z])", password):
            return True
        else:
            return False
        

    def show_password(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
            # self.root.destroy()


# Create an instance of the Register class to run it
root = Tk()
Register(root)
root.mainloop()
