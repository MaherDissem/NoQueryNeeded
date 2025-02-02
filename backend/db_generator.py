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
# Create a table named 'sales'
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    date TEXT NOT NULL
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
conn.commit()

# Insert some dummy data into the 'sales' table
cursor.executemany('''
INSERT INTO sales (product, price, quantity, date) VALUES (?, ?, ?, ?)
''', [
    ('Apple', 1.0, 100, '2022-01-01'),
    ('Banana', 0.5, 200, '2022-01-02'),
    ('Cherry', 2.0, 50, '2022-01-03'),
    ('Date', 3.0, 30, '2022-01-04'),
    ('Elderberry', 4.0, 20, '2022-01-05'),
    ('Fig', 1.5, 80, '2022-01-06'),
    ('Grape', 2.5, 70, '2022-01-07'),
    ('Honeydew', 3.5, 40, '2022-01-08'),
    ('Kiwi', 1.0, 90, '2022-01-09'),
    ('Lemon', 0.5, 120, '2022-01-10'),
    ('Mango', 2.0, 60, '2022-01-11'),
    ('Nectarine', 3.0, 40, '2022-01-12'),
    ('Orange', 1.5, 80, '2022-01-13'),
    ('Peach', 2.5, 70, '2022-01-14'),
    ('Quince', 3.5, 50, '2022-01-15'),
    ('Raspberry', 1.0, 100, '2022-01-16'),
    ('Strawberry', 0.5, 200, '2022-01-17'),
    ('Tomato', 2.0, 70, '2022-01-18'),
    ('Ugli fruit', 3.0, 30, '2022-01-19'),
    ('Vanilla bean', 4.0, 20, '2022-01-20'),
    ('Watermelon', 1.5, 90, '2022-01-21'),
    ('Xigua', 0.5, 120, '2022-01-22'),
    ('Yuzu', 2.0, 60, '2022-01-23'),
    ('Zucchini', 3.0, 40, '2022-01-24'),
    ('Apricot', 1.0, 100, '2022-01-25'),
    ('Blueberry', 0.5, 200, '2022-01-26'),
    ('Cantaloupe', 2.0, 50, '2022-01-27'),
    ('Dragonfruit', 3.0, 30, '2022-01-28'),
    ('Eggplant', 4.0, 20, '2022-01-29'),
    ('Fennel', 1.5, 80, '2022-01-30'),
    ('Grapefruit', 2.5, 70, '2022-01-31'),
    ('Huckleberry', 3.5, 40, '2022-02-01'),
    ('Jujube', 1.0, 90, '2022-02-02'),
    ('Kumquat', 0.5, 120, '2022-02-03'),
    ('Lime', 2.0, 60, '2022-02-04'),
    ('Mandarin orange', 3.0, 40, '2022-02-05'),
    ('Nashi pear', 1.5, 80, '2022-02-06'),
    ('Olive', 2.5, 70, '2022-02-07'),
    ('Papaya', 3.5, 50, '2022-02-08'),
    ('Quince', 1.0, 100, '2022-02-09'),
    ('Rambutan', 0.5, 200, '2022-02-10'),
    ('Starfruit', 2.0, 70, '2022-02-11'),
    ('Tamarillo', 3.0, 30, '2022-02-12'),
    ('Ugli fruit', 4.0, 20, '2022-02-13'),
    ('Vanilla bean', 1.5, 90, '2022-02-14'),
    ('Watermelon', 0.5, 120, '2022-02-15'),
    ('Xigua', 2.0, 60, '2022-02-16'),
    ('Yuzu', 3.0, 40, '2022-02-17'),
    ('Zucchini', 1.0, 100, '2022-02-18'),
    ('Apricot', 0.5, 200, '2022-02-19'),
    ('Blueberry', 2.0, 50, '2022-02-20'),
    ('Cantaloupe', 3.0, 30, '2022-02-21'),
    ('Dragonfruit', 1.5, 80, '2022-02-22'),
])
conn.commit()


with open(os.path.join('backend', 'database_file', 'schema.txt'), 'w') as f:
    # Save people schema
    f.write("'people' table schema:\n")
    cursor.execute("PRAGMA table_info(people)")
    schema = cursor.fetchall()
    for row in schema:
        f.write(f"{row}\n")

    # Save sales schema
    f.write("\n'sales' table schema:\n")
    cursor.execute("PRAGMA table_info(sales)")
    schema = cursor.fetchall()
    for row in schema:
        f.write(f"{row}\n")

# Close the connection to the database
conn.close()