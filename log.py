from tkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox 
def signin():
    username=user.get()
    Password=pw.get()
    if username =='admin' and  Password == '1234':
        screen=Toplevel(root)
        screen.title('Log in')
        screen.geometry("1350x700+0+0")
        screen.config(bg='ADD8E6')

        Label(screen,text='Welcome TO KASA Project!',bg='#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)
        screen.mainloop()
        
    elif username != 'admin' and Password == '1234':
        error_screen = Toplevel(root)
        error_screen.title("Invalid Username and Password")
        error_screen.geometry('400x400+400+300')
        Label(error_screen, text="Invalid username and password").pack()
        error_screen.mainloop()

    elif Password != "1234":
        error_screen = Toplevel(root)
        error_screen.title("Invalid Password")
        error_screen.geometry('400x400+400+300')
        Label(error_screen, text="Invalid password").pack()
        error_screen.mainloop()

    elif username != 'admin':
        error_screen = Toplevel(root)
        error_screen.title("Invalid Username")
        error_screen.geometry('400x400+400+300')
        Label(error_screen, text="Invalid username").pack()
        error_screen.mainloop()




def on_enter_username(e):
    user.delete(0, 'end')

def on_leave_username(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

def on_enter_password(e):
    pw.delete(0, 'end')

def on_leave_password(e):
    name = pw.get()
    if name == '':
        pw.insert(0, 'Password')

root = Tk()
root.geometry('1200x800')
root.configure(bg="#fff")
root.config(bg='#ADD8E6')



# root.resizable(0, 0)
# image = Image.open('TeamWork.jpg')
# resized_image = image.resize((200,100 ), Image.BILINEAR)
# img = ImageTk.PhotoImage(resized_image)
# Label(root, image=img,bg='#ADD8E6').place(x=75, y=100)

frame = Frame(root, width=600, height=450, bg="white")
frame.place(x=480, y=70)
frame.config(bg='gray')

root.resizable(0, 0)
image = Image.open('kasa.png')
resized_image = image.resize((100,80 ), Image.BILINEAR)
img = ImageTk.PhotoImage(resized_image)
Label(frame, image=img, bg='gray').place(x=350, y=2)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='gray', font=('Microsoft YaHei UI light', 23, 'bold'))
heading.place(x=100, y=5)

# create username entry box
user = Entry(frame, width=25, fg='black', border=0, bg='gray', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)
# user.bind('<Key>', on_enter_username )

Frame(frame, width=330, height=2, bg='black').place(x=25, y=107)


# for password
pw = Entry(frame, width=25, fg='black', border=0, bg='gray', font=('Microsoft YaHei UI Light', 11), show='*')
pw.place(x=30, y=150)
pw.insert(0, 'Password')
pw.bind('<FocusIn>', on_enter_password)
pw.bind('<FocusOut>', on_leave_password)
# pw.bind('<Key>', on_enter_password)
Frame(frame, width=330, height=2, bg='black').place(x=25, y=177)


btn = Button(frame, width=30, pady=7, text='Sign in', bg='#57a1f8', fg='white', font=('Arial',12,'bold'), border=0, command=signin)
btn.place(x=35, y=204)

lbl = Label(frame, text="Don't Have An Account?", fg='black', bg='gray', font=('Arial', 9))
lbl.place(x=40, y=260)


def forget_password_click(event):
    forget_password_label.config(text="Forget Password", font=("Arial", 10, "underline"),background='gray')
forget_password_label = Label(root, text="Forget Password?", font=("Arial", 10),background='gray')
forget_password_label.place(x=520, y=360)

forget_password_label.bind("<Button-1>", forget_password_click)


sign_up = Button(frame, width=6, text='Sign up', border=0, bg='gray', cursor='hand2', fg='blue',)
sign_up.place(x=180, y=260)
root.geometry("1380x700")
root.mainloop()
