import sqlite3 as sl

connection = sl.connect('ivaners_test.db')

cursor = connection.cursor()

with connection:
    connection.executescript("""
    drop table if exists user;
    CREATE TABLE USER (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    );
    """)

sql = 'INSERT INTO USER (id, name, age) values (?, ?, ?)'
data = [(1, 'Alice', 21)
    , (2, 'Bob', 22)
    , (3, 'Chris', 23)
]

with connection:
    connection.executemany(sql, data)

a = connection.execute("""
    select * from user
    where age > 21
    """)

print([e for e in a])