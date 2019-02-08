import sqlite3


with sqlite3.connect('addressbook.db') as connection:
    c = connection.cursor()
    results = c.execute('SELECT * FROM details')
    for each in results:
        print(each)
