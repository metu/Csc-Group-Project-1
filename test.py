import sqlite3
conn = sqlite3.connect('CINEMA.db')

c = conn.cursor()
c.execute('''CREATE TABLE movie(movieNo TEXT PRIMARY KEY, 
								movieName TEXT)''')

c.execute('''CREATE TABLE employer(empNo TEXT PRIMARY KEY, 
								   empName TEXT, 
								   empSname TEXT)''')

c.execute('''CREATE TABLE manager(manNo TEXT PRIMARY KEY, 
								  manName TEXT, 
								  manSname TEXT)''')

c.execute('''CREATE TABLE seat (seatNo TEXT NOT NULL , 
								movieTime TEXT NOT NULL , 
								custName TEXT, 
								price INTEGER, 
								PRIMARY KEY (seatNo,movieTime))''')