#Importing Necessary modules
from tkinter import *
from PIL import Image,ImageTk

#Defining functions

def show_features():
    # Create a new window to display features
    features_window = Toplevel(root)
    features_window.title("Features")
    features_window.geometry("200x200+800+213")

    # Add buttons for features
    upcoming_events_btn = Button(features_window, text="Upcoming Events")
    upcoming_events_btn.pack(pady=5, fill=X, expand=True)

    attendance_btn = Button(features_window, text="Attendance")
    attendance_btn.pack(pady=5, fill=X, expand=True)

    events_calendar_btn = Button(features_window, text="Events Calendar")
    events_calendar_btn.pack(pady=5, fill=X, expand=True)

    more_btn = Button(features_window, text="More")
    more_btn.pack(pady=5, fill=X, expand=True)


def toggle_menu():
    if features_button.winfo_viewable():
        features_button.pack_forget()
    else:
        features_button.place(x=10,y=2)

def show_notifications():
    features_window = Toplevel(root)
    features_window.title("Notifications")
    features_window.geometry("200x200+800+213")

#Creating a new window
root=Tk()
root.geometry("1500x1500")

header = Canvas(root, bg="#001F3F")
header.create_text(680, 130, text="KASA-\nThe Event Manager", fill="white", font=('Cochin', 80))
logo = Image.open("KASA.png")
resized_image = logo.resize((150, 150))
new_image = ImageTk.PhotoImage(resized_image)
header.create_image(30, 60, anchor=NW, image=new_image)
header.pack(fill="x")

header.create_image(30,60, anchor=NW, image=new_image)

header.pack()

mid=Canvas(height=1450, width=1500, bg="white")




# Create a button to show features
features_button = Button(root, text="☰", command=show_features)
features_button.place(x=1300,y=280)

notification_button = Button(root, text="🔔", command=show_notifications)
notification_button.place(x=1260,y=280)


mid.create_text(700,60,text="Event Attendance",fill="black", font=("Cochin",60), anchor="center")

mid.pack()

root.mainloop()