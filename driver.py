import sqlite3
conn = sqlite3.connect('CINEMA.db')
#___ conn = sqlite3.connect(db) conn.execute('pragma foreign_keys = on') ___ 
#FKs must be enforced manually

c = conn.cursor()

def newEmployers():
	entries = int(raw_input("enter amount of entries"))
	emplist = []

	for i in range(0,entries):
		empNo = str(i)
		name = raw_input("enter name for employee ")
		sname = raw_input("enter surname for employee ")
		emplist.append((empNo,name,sname))

	c.executemany('''INSERT INTO employer(empNo, empName, empSname) VALUES(?,?,?)''',emplist)
	conn.commit()
	printEMP()

def printEMP():	
	d = c.execute('''SELECT * FROM employer''')
	for row in d:
		print row

def printSeat():	
	d = c.execute('''SELECT * FROM seat''')
	for row in d:
		print row

def printMovie():	
	d = c.execute('''SELECT * FROM movie''')
	for row in d:
		print row


def loginEmp():
	userId = (raw_input("enter user id "),)
	c.execute('''SELECT empNo FROM employer WHERE empNo =  ?''',userId)
	empNo = c.fetchone()

	if(empNo):
		c.execute('''SELECT empName FROM employer WHERE empNo = ?''', userId)
		empName = c.fetchone()
		print "welcome, ",empName[0]

		print "press 1 to place a booking"
		option = int(raw_input())
		if(option == 1):
			placeBooking()
	
	else:
		print "not in db"

def loginMan():
	userId = (raw_input("enter user id "),)
	c.execute('''SELECT manNo FROM manager WHERE manNo = ? ''',userId)
	manNo = c.fetchone()

	if(manNo):
		c.execute('''SELECT manName FROM manager WHERE manNo = ? ''',userId)
		manName = c.fetchone()
		print "welcome, ",manName[0]

		print "press 1 to place a booking"
		print "press 2 to remove a booking"
		print "press 3 to edit a booking"
		print "press 4 to enter new employees into the database"

		option = int(raw_input())

		if(option == 1):
			placeBooking()
		elif(option == 2):
			removeBooking()
		elif(option == 3):
			print "here"
		elif(option == 4):
			newEmployers()
		else:
			print "invalid selection"

def removeBooking():
	customer = (raw_input("enter customer name "),)
	c.execute('''DELETE FROM seat WHERE custName = ?''',customer)
	conn.commit()
	printSeat()

def placeBooking():
	bookings = int(raw_input("how man bookings "))
	list = []
	for i in range (0,bookings):
		seatNo = raw_input("enter seat number ")
		timeslot = raw_input("enter time slot ")
		name = raw_input("enter customer name ")

		if(timeslot == "14:00"):
			price = 30
		else:
			price = 60

		list.append((seatNo,timeslot,name,price))
	c.executemany('''INSERT INTO seat(seatNo,movieTime,custName,price) VALUES(?,?,?,?)''',list)
	conn.commit()
	printSeat()
	

#loginMan()
