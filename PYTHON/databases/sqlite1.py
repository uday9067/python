import sqlite3 

connection = sqlite3.connect('mydata.db')

cursor = connection.cursor()

cursor.execute(
"""CREATE TABLE IF NOT EXISTS person(
first TEXT,
last TEXT,
age INTEGER
)
"""
)

cursor.execute(
    """INSERT INTO person VALUES
    ("uday","suryavanshi",18),
    ('atish','thorat',18),
    ('chaitanya','khandekar',18),
    ('manish','dhaigude',17)
    """
)
cursor.execute(
    """
    SELECT * FROM person
    """
)

row =cursor.fetchall()
print(row)

connection.commit()