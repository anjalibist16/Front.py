# from tkinter import *
# from PIL import Image,ImageTk

# root=Tk()
# root.geometry("1400x1300")


# header = Canvas(root, width=1400, height=250, bg="#001F3F")
# header.create_text(680, 130, text="KASA-\nThe Event Manager", fill="white", font=('Cochin', 80))
# logo= (Image.open("KASA.png"))
# resized_image= logo.resize((150,150))
# new_image= ImageTk.PhotoImage(resized_image)

# header.create_image(30,60, anchor=NW, image=new_image)
# header.pack()

# mid=Canvas(height=1300, width=1250, bg="white")

# def show_features():
#     # Create a new window to display features
#     features_window = Toplevel(root)
#     features_window.title("Features")
#     features_window.geometry("200x200+800+213")

#     # Add buttons for features
#     upcoming_events_btn = Button(features_window, text="Upcoming Events")
#     upcoming_events_btn.pack(pady=5, fill=X, expand=True)

#     attendance_btn = Button(features_window, text="Attendance")
#     attendance_btn.pack(pady=5, fill=X, expand=True)

#     events_calendar_btn = Button(features_window, text="Events Calendar")
#     events_calendar_btn.pack(pady=5, fill=X, expand=True)

#     more_btn = Button(features_window, text="More")
#     more_btn.pack(pady=5, fill=X, expand=True)


# def toggle_menu():
#     if features_button.winfo_viewable():
#         features_button.pack_forget()
#     else:
#         features_button.place(x=10,y=2)

# def show_notifications():
#     features_window = Toplevel(root)
#     features_window.title("Notifications")
#     features_window.geometry("200x200+800+213")

# # Create a button to show features
# features_button = Button(root, text="☰", command=show_features)
# features_button.place(x=1300,y=270)

# notification_button = Button(root, text="🔔",command=show_notifications)
# notification_button.place(x=1250,y=270)


# mid.create_text(700,60,text="Administrator Profile",fill="black", font=("Cochin",60), anchor="center")
# mid.create_text(500,160,text="Name: ",fill="black", font=("Cochin",30), anchor="center")
# mid.create_text(600,260,text="No of events attended: ",fill="black", font=("Cochin",30), anchor="center")
# mid.create_text(620,360,text="No of events not attended:",fill="black", font=("Cochin",30), anchor="center")

# mid.pack()



# root.mainloop()




from tkinter import *
from PIL import Image, ImageTk

def on_resize(event):
    """Handle window resize event."""
    # Get the new window size
    width = event.width
    height = event.height

    # Configure canvas and other widgets accordingly
    header.config(width=width)
    mid.config(width=width, height=height-250)  # Adjust height to fill remaining space

root = Tk()
root.geometry("1400x1300")
root.bind("<Configure>", on_resize)  # Bind resize event handler

header = Canvas(root, bg="#001F3F")
header.create_text(680, 130, text="KASA-\nThe Event Manager", fill="white", font=('Cochin', 80))
logo = Image.open("KASA.png")
resized_image = logo.resize((150, 150))
new_image = ImageTk.PhotoImage(resized_image)
header.create_image(30, 60, anchor=NW, image=new_image)
header.pack(fill="x")  # Expand horizontally

mid = Canvas(root, bg="white")

def show_features():
    """Show features window."""
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
    """Toggle menu visibility."""
    if features_button.winfo_viewable():
        features_button.pack_forget()
    else:
        features_button.pack(side=LEFT, padx=10, pady=2)

def show_notifications():
    """Show notifications window."""
    features_window = Toplevel(root)
    features_window.title("Notifications")
    features_window.geometry("200x200+800+213")

# Create buttons to show features and notifications
features_button = Button(root, text="☰", command=show_features)
features_button.pack(side=LEFT, padx=10, pady=2)
notification_button = Button(root, text="🔔", command=show_notifications)
notification_button.pack(side=LEFT, padx=10, pady=2)

mid.create_text(500, 160, text="Name: ", fill="black", font=("Cochin", 30), anchor="e")
mid.create_text(500, 260, text="No of events attended: ", fill="black", font=("Cochin", 30), anchor="e")
mid.create_text(500, 360, text="No of events not attended:", fill="black", font=("Cochin", 30), anchor="e")

# Entry widgets for user input
name_entry = Entry(mid)
name_entry.place(x=600, y=150)  # Adjusted for responsiveness
events_attended_entry = Entry(mid)
events_attended_entry.place(x=600, y=250)  # Adjusted for responsiveness
events_not_attended_entry = Entry(mid)
events_not_attended_entry.place(x=600, y=350)  # Adjusted for responsiveness

mid.pack(fill="both", expand=True)  # Expand to fill remaining space

root.mainloop()
