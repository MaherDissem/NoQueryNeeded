import sqlite3
import os

# Create a connection to a new SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(os.path.join('backend', 'database_file', 'dummy.db'))

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table named 'people'
cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    height REAL DEFAULT 0.0,
    score Integer DEFAULT 0,
    hometown TEXT DEFAULT 'Unknown'
)
''')

# Insert some dummy data into the 'people' table
cursor.executemany('''
INSERT INTO people (name, age, height, score, hometown) VALUES (?, ?, ?, ?, ?)
''', [
    ('Alice', 30, 1.65, 85, 'New York'),
    ('Bob', 25, 1.80, 90, 'Los Angeles'),
    ('Charlie', 35, 1.75, 75, 'Chicago'),
    ('David', 40, 1.70, 88, 'Houston'),
    ('Emma', 28, 1.60, 95, 'San Francisco'),
    ('Frank', 33, 1.82, 70, 'Seattle'),
    ('Grace', 29, 1.68, 92, 'Boston'),
    ('Henry', 45, 1.77, 80, 'Miami'),
    ('Ivy', 32, 1.66, 87, 'Austin'),
    ('Jack', 27, 1.78, 93, 'Denver'),
    ('Kara', 38, 1.69, 78, 'Portland'),
    ('Liam', 31, 1.74, 82, 'Atlanta'),
    ('Mia', 26, 1.61, 96, 'San Diego'),
    ('Nathan', 36, 1.79, 76, 'Dallas'),
    ('Olivia', 34, 1.64, 85, 'Philadelphia'),
    ('Paul', 41, 1.72, 89, 'Phoenix'),
    ('Quinn', 29, 1.70, 90, 'Charlotte'),
    ('Rachel', 37, 1.67, 77, 'Las Vegas'),
    ('Samuel', 43, 1.75, 83, 'Indianapolis'),
    ('Tina', 24, 1.59, 94, 'Nashville'),
    ('Umar', 30, 1.73, 81, 'Columbus'),
    ('Violet', 39, 1.68, 88, 'Kansas City'),
    ('Walter', 46, 1.80, 79, 'Minneapolis'),
    ('Xavier', 28, 1.76, 91, 'Orlando'),
    ('Yasmine', 35, 1.65, 84, 'Baltimore'),
    ('Zach', 42, 1.78, 86, 'Detroit'),
    ('Abby', 31, 1.60, 97, 'Louisville'),
    ('Ben', 27, 1.79, 75, 'Memphis'),
    ('Catherine', 38, 1.63, 89, 'Raleigh'),
    ('Derek', 32, 1.81, 80, 'Oklahoma City'),
    ('Elaine', 40, 1.67, 92, 'Salt Lake City'),
    ('Felix', 33, 1.75, 83, 'Milwaukee'),
    ('Gina', 26, 1.62, 95, 'Richmond'),
    ('Hector', 45, 1.70, 78, 'Tampa'),
    ('Isabella', 29, 1.66, 86, 'St. Louis'),
    ('James', 37, 1.74, 88, 'New Orleans'),
    ('Kaitlyn', 34, 1.68, 91, 'Sacramento'),
    ('Leo', 30, 1.77, 85, 'Hartford'),
    ('Megan', 28, 1.64, 93, 'Cleveland'),
    ('Noah', 41, 1.72, 82, 'Buffalo')
])

# Commit the changes
conn.commit()

# Query the data to verify it's been inserted
cursor.execute('SELECT * FROM people')

# Fetch and display all rows
rows = cursor.fetchall()
for row in rows:
    print(row)

# Get schema
cursor.execute("PRAGMA table_info(people)")
schema = cursor.fetchall()

with open(os.path.join('backend', 'database_file', 'schema.txt'), 'w') as f:
    for row in schema:
        f.write(f"{row}\n")

# Close the connection to the database
conn.close()