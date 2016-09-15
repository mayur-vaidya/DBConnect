import sqlite3
conn=sqlite3.connect('database.db')
print "Opened Successfully"
conn.execute('CREATE TABLE students(firstname TEXT, lastname TEXT, address TEXT, mobile TEXT)')
print "Table created Successfully!!!"