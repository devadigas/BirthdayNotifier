# mysql connector is the driver used

from tkinter import *
from tkcalendar import Calendar, DateEntry
import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='BirthdayNotifier')

def submit():

    if (text1.get("1.0",'end-1c') == '' or text2.get("1.0",'end-1c') == '' or text3.get("1.0",'end-1c') == '' or
            cal.get() == '' or text5.get("1.0",'end-1c') == '') :
        messagebox.showerror("Attention!!!!", "Field cannot be empty")
    else :
       # roll = text1.get("1.0",'end-1c')
        #nm = text2.get("1.0",'end-1c')
        #ag = text3.get("1.0",'end-1c')
        #bd = cal.get()
        #plc = text5.get("1.0",'end-1c')

        cursor = conn.cursor()

        insert_stmt = "insert into bday(rollno, name, age, bday, place) values(%s, %s, %s, %s, %s)"
        data = (text1.get("1.0",'end-1c'), text2.get("1.0",'end-1c'), text3.get("1.0",'end-1c'),cal.get_date(), text5.get("1.0",'end-1c'))
        print(data)

        try:
            # executing the sql command
            cursor.execute(insert_stmt,data)
            # commit changes in database
            conn.commit()
            conn.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into Bday table {}".format(error))

        finally:
            if conn.is_connected():
                conn.rollback()
                print(cursor.rowcount, "record inserted!")
                print("MySQL connection is closed")
        messagebox.showinfo("Message", "Fields stored successfully!!")

def add_entry():
    top1 = Toplevel()
    top1.title('Add an Entry')
    width, height = top1.winfo_screenwidth(), top1.winfo_screenheight()
    top1.geometry('%dx%d+0+0' % (width, height))
    top1.configure(bg='aquamarine')

    global text1, text2, text3, cal, text5

    label1 = Label(top1, text="Add an Entry", font=("Helvetica", 16, "bold"),bg = "aquamarine")
    label1.place(x=500,y=30)

    label2 = Label(top1, text="RollNo", font=("Helvetica", 14, "bold"),bg = "aquamarine")
    label2.place(x=400,y=150)

    text1 = Text(top1, height=2, width=20)
    text1.place(x=500, y=150)

    label3 = Label(top1, text="Name", font=("Helvetica", 14, "bold"), bg="aquamarine")
    label3.place(x=400, y=200)

    text2 = Text(top1, height=2, width=20)
    text2.place(x=500, y=200)

    label4 = Label(top1, text="Age", font=("Helvetica", 14, "bold"), bg="aquamarine")
    label4.place(x=400, y=250)

    text3 = Text(top1, height=2, width=20)
    text3.place(x=500, y=250)

    label5 = Label(top1, text="Bday", font=("Helvetica", 14, "bold"), bg="aquamarine")
    label5.place(x=400, y=300)

    cal = DateEntry(top1, width=16, background="grey", foreground="white", bd=2,date_pattern='dd/mm/yyyy')
    cal.place(x=500, y=300)

    label6 = Label(top1, text="Place", font=("Helvetica", 14, "bold"), bg="aquamarine")
    label6.place(x=400, y=350)

    text5 = Text(top1, height=2, width=20)
    text5.place(x=500, y=350)

    button1 = Button(top1, text='Submit', command=submit, bg='Grey', fg='White', font='bold')
    button1.place(x=400, y=450)
    button1.configure(width=12, height=2)

    button2 = Button(top1, text='Back', command=top1.destroy, bg='Grey', fg='White', font='bold')
    button2.place(x=600, y=450)
    button2.configure(width=12, height=2)
    top1.mainloop()


