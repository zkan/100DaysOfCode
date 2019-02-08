import sqlite3


# Create db if it doesn't exist
connection = sqlite3.connect('addressbook.db')

c = connection.cursor()

c.execute("""INSERT INTO details
VALUES('Kan', '123 Fake St, Thailand', 22222222)
""")

connection.commit()

connection.close()
