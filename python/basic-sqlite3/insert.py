import sqlite3


with sqlite3.connect('addressbook.db') as connection:
    c = connection.cursor()

    # We don't need to do connection.commit() when we use the context
    c.execute("""INSERT INTO details
    VALUES('Kan', '123 Fake St, Thailand', 22222222)
    """)
