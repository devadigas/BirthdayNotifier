from tkinter import *
from tkcalendar import Calendar, DateEntry
import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='BirthdayNotifier')

def update():
    cursor = conn.cursor()

    rollno = text1.get("1.0",'end-1c')
    sql_query = "Update  bday set bday=%s where rollno=%s"
    data = (cal.get_date(),rollno)
    print(data)

    try:
        # executing the sql command
        cursor.execute(sql_query, data,)
        # commit changes in database
        conn.commit()
        conn.close()

    except mysql.connector.Error as error:
        print("Failed to update record into Bday table {}".format(error))

    finally:
        if conn.is_connected():
            conn.rollback()
            print(cursor.rowcount, "record updated!")
            print("MySQL connection is closed")
    messagebox.showinfo("Message", "Fields stored successfully!!")


def update_entry():
    top3 = Toplevel()
    top3.title('Update an Entry')
    width, height = top3.winfo_screenwidth(), top3.winfo_screenheight()
    top3.geometry('%dx%d+0+0' % (width, height))
    top3.configure(bg='aquamarine')

    global cal,text1

    label1 = Label(top3, text="Update an Entry", font=("Helvetica", 16, "bold"), bg="aquamarine")
    label1.place(x=500, y=30)

    label2 = Label(top3, text="RollNo", font=("Helvetica", 14, "bold"), bg="aquamarine")
    label2.place(x=400, y=150)

    text1 = Text(top3, height=2, width=20)
    text1.place(x=500, y=150)

    label5 = Label(top3, text="Bday", font=("Helvetica", 14, "bold"), bg="aquamarine")
    label5.place(x=400, y=250)

    cal = DateEntry(top3, width=16, background="grey", foreground="white", bd=2)
    cal.place(x=500, y=250)

    button1 = Button(top3, text='Update', command=update, bg='Grey', fg='White', font='bold')
    button1.place(x=400, y=350)
    button1.configure(width=12, height=2)

    button2 = Button(top3, text='Back', command=top3.destroy, bg='Grey', fg='White', font='bold')
    button2.place(x=600, y=350)
    button2.configure(width=12, height=2)



