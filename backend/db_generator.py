import sqlite3

# Create a connection to a new SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('database_file/dummy.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table named 'people'
cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Insert some dummy data into the 'people' table
cursor.executemany('''
INSERT INTO people (name, age) VALUES (?, ?)
''', [
    ('Alice', 30),
    ('Bob', 25),
    ('Charlie', 35),
    ('David', 40),
])

# Commit the changes
conn.commit()

# Query the data to verify it's been inserted
cursor.execute('SELECT * FROM people')

# Fetch and display all rows
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection to the database
conn.close()