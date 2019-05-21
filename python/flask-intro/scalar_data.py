from sqlalchemy import create_engine


eng = create_engine('sqlite:///:memory:')

with eng.connect() as con:
    rs = con.execute('SELECT 5')
    data = rs.fetchone()[0]
    print(f'Data: {data}')
