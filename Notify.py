from datetime import datetime, timedelta
from plyer.utils import platform
from plyer import notification
import mysql.connector
import pandas as pd
import csv
import numpy as np

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='BirthdayNotifier')


def notify():
    cursor = conn.cursor()

    ## defining the Query
    query = "SELECT * FROM bday"

    ## getting records from the table
    cursor.execute(query)

    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()

    """ ## Showing the data
      for record in records:
          print(record) """
    cols = ['Rollno', 'Name', 'Age', 'Bday', 'Place']

    # print(records)

    with open('shows.csv', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerow(cols)
        write.writerows(records)

    data = pd.read_csv('shows.csv')
    data1 = data[['Rollno', 'Name', 'Bday']].copy()
    # df2 = df[['Courses', 'Fee']].copy()

    data1.to_csv('Final.csv')

    days = datetime.today() + timedelta(days=3)
    data1['Y/N'] = np.where(data1['Bday'] == days.strftime('%Y-%m-%d'), 'Y', 'N')


    # print(data1)
    df2 = data1.loc[data1['Y/N'] == 'Y']
    df3 = df2[['Rollno', 'Name']].copy()
    df3.to_csv('Output.csv', index=None)
    my_list = df3.values.tolist()
    msg = 'Hey, Its ' +str(my_list) + ' Bday'

    notification.notify(
        title='Upcoming Birthday!!!!',
        message=msg,
        app_name='Birtday Notifier',
        toast=False,
        timeout=10
    )
