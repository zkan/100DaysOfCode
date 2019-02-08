import sqlite3


with sqlite3.connect('addressbook.db') as connection:
    c = connection.cursor()
    c.execute("""INSERT INTO details
    VALUES('Kan', '123 Fake St, Thailand', 22222222)
    """)
