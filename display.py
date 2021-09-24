from demo import *
from tkinter import *
from tkinter import ttk

# Create an instance of Tkinter frame
root= Tk()

width = 750
height = 300

root.geometry(f"{width}x{height}")
root.resizable(0, 0)
root.title('Email Automation')


def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)


# Initialize a Label to display the User Input
label=Label(root, text="", font=("Courier 22 bold"), background="gray74").pack(pady=20, side= "TOP", anchor="w")
label.pack()


# Create an Entry widget to accept User Input
entry = Entry(root, width= 40)
entry.focus_set()
entry.pack()

# Create a Button to validate Entry Widget
ttk.Button(root, text= "Submit",width= 20, command= display_text).pack(pady=20)

root.mainloop()