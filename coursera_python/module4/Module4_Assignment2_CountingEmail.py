import sqlite3

db_connection = sqlite3.connect('emaildb.sqlite')
cursor = db_connection.cursor()

cursor.execute('''DROP TABLE IF EXISTS Counts''')

cursor.execute('''CREATE TABLE Counts (org TEXT, count INTERGER)''')

file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'mbox.txt'
file_handle = open(file_name)

for line in file_handle:
    if not line.startswith('From: '):
        continue
    words = line.split()
    org = words[1].split('@')[1]
    cursor.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))

    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

    db_connection.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cursor.execute(sqlstr):
    print(row[0], row[1])

cursor.close()
