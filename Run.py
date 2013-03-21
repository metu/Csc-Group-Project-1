from driver import*

option=str("0")
while option.upper()!="EXIT":
        print "Welcome to Cinema Bookings\n----------------------------"
        print("1)\tAdd new employee\n"+
              "2)\tPrint Employee\n"+
              "3)\tPrint Seat")
        option=raw_input("\aChoose an Option or type exit to close: ")
        print
        if option=='1': newEmployers()
        if option=='2': printEMP()
        if option=='3': printSeat()
