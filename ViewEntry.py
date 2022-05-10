from tkinter import *
import mysql.connector


def view_entry():

    global top2
    top2=Toplevel()
    top2.title('View an Entry')

    conn = mysql.connector.connect(user='root', password='root', host='localhost', database='BirthdayNotifier')
    my_conn = conn.cursor()

    ####### end of connection ####
    my_conn.execute("SELECT * FROM bday limit 0,10")
    i = 0
    for bd in my_conn:
        for j in range(len(bd)):
            e = Entry(top2, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, bd[j])
        i = i + 1

    """width, height = top2.winfo_screenwidth(), top2.winfo_screenheight()
    top2.geometry('%dx%d+0+0' % (width, height))
    top2.configure(bg='aquamarine')

    label1 = Label(top2, text="View an Entry", font=("Helvetica", 16, "bold"), bg="aquamarine")
    label1.place(x=500, y=30)

    button1 = Button(top2, text='Show', command=show_entry, bg='Grey', fg='White', font='bold')
    button1.place(x=400, y=450)
    button1.configure(width=12, height=2)

    button2 = Button(top2, text='Back', command=top2.destroy, bg='Grey', fg='White', font='bold')
    button2.place(x=600, y=450)
    button2.configure(width=12, height=2)

"""
