import sqlite3
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE Contacts (Id integer primary key, Name text, Address text, Telephone text)")
cursor.execute("INSERT INTO Contacts VALUES (1, 'John Doe', 'Some Street 123', '555-1234')")
cursor.execute("INSERT INTO Contacts VALUES (2, 'Jane Doe', 'Some Other Street 456', '555-2345')")
conn.commit()
query = "SELECT * FROM Contacts"
contacts = cursor.execute(query).fetchall()
print(contacts)
bckup = sqlite3.connect('file:backup.db')
with bckup:
    conn.backup(bckup)
bckup.close()
conn.close()
