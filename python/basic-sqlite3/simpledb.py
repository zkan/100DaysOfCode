import sqlite3


# Create db if it doesn't exist
connection = sqlite3.connect('addressbook.db')

c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS details
(name TEXT, address TEXT, phone_number INT)
""")

connection.close()
