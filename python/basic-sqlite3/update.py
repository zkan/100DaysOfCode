import sqlite3


with sqlite3.connect('addressbook.db') as connection:
    c = connection.cursor()

    # We don't need to do connection.commit() when we use the context
    c.execute("""UPDATE details
    SET name = 'yeah'
    WHERE name = 'Test'
    """)
