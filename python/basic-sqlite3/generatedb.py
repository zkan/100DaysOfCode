from contextlib import contextmanager
import sqlite3


@contextmanager
def create_db(name):
    try:
        conn = sqlite3.connect(f'{name}.db')
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.close()


def prompt_for_name():
    name = input('What would you like to name your test db file?: ')
    return name


if __name__ == '__main__':
    name = prompt_for_name()
    with create_db(name) as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS details
            (name TEXT, address TEXT, phone_number INT)
            """)

        print(f'{name}.db has been created')
