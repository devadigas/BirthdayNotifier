from tkinter import *
import pyautogui            # gives us the resolution of screen
import AddEntry
import ViewEntry
import UpdateEntry
import Notify

top = Tk()

Notify.notify()

top.title("Birthday Notifier App")
x,y = pyautogui.size()
screen_dimensions = str(x)+'x'+str(y)
top.geometry(screen_dimensions)

label1 = Label(top, text="Welcome to Birthday Notifier App", font=("Helvetica", 18, "bold"),bg = "aquamarine")
label1.place(x=450,y=100)

def make_entry():
    AddEntry.add_entry()

def view_entry():
    ViewEntry.view_entry()

def update_entry():
    UpdateEntry.update_entry()

button1 = Button(top, text = 'Make Entry', command = make_entry,bg = 'Grey',fg = 'White',font = 'bold')
button1.place(x=300, y=350)
button1.configure(width = 12, height = 2)

button2 = Button(top, text = 'View Entry', command = view_entry,bg = 'Grey',fg = 'White',font = 'bold')
button2.place(x=500, y=350)
button2.configure(width = 12, height = 2)

button3 = Button(top, text = 'Update Entry', command = update_entry,bg = 'Grey',fg = 'White',font = 'bold')
button3.place(x=700, y=350)
button3.configure(width = 12, height = 2)

button4 = Button(top, text = 'Exit', command = top.destroy,bg = 'Grey',fg = 'White',font = 'bold')
button4.place(x=900, y=350)
button4.configure(width = 12, height = 2)

top.configure(bg='aquamarine')
top.mainloop()
