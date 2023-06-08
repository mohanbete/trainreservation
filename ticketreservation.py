                                                            #Train Ticket Reservation
import datetime
import random
print(20*"===","Welcome To Train Ticket Reservation","==="*20)
list_of_trains={"Amaravathi":12345,"Vandhe_bharath":678910,"coramandal":111213,"venkatadri_express":141516,"rajadhani":171819} 
name=input("Enter Passenger Name:")
age=int(input("Enter Your Age:"))
gender=input("Enter Your Gender:")
train=input("Enter Your Requried Train:")
for k,v in list_of_trains.items():                                         
            print ("Train Name:",k,"Train Num:",v)
ticketprice={"Amaravathi":150,"Vandhe_bharath":250,"coramandal":350,"venkatadri_express":450,"rajadhani":550}
for t,r in ticketprice.items():
    print("Select_train:",t,"ticketprice:",r)
pas=int(input("Enter Number Of Passengers:"))
if train in ticketprice:
    print("Ticket Price:",int(ticketprice[train]))
    price=(int(ticketprice[train])*pas)
    print(price)
    user_date=int(input("enter your reservation date:"))
    date=datetime.datetime(2023,6,user_date)
    print("Your Reservation Date:",date)
    print("Your Ticket Was Reserved On:",datetime.datetime.now())
    seat=input("Select_Seattype:")
    class Train():
        def __init__(self, train_num, select_seat, source, destination, seats,):
            self.train_num=train_num
            self.select_seat=select_seat
            self.source=source
            self.destination=destination
            self.seats=seats
        def display_info(self):
            print("Train number:",self.train_num)
            print("select seat:",self.select_seat)
            print("source:",self.source)
            print("destination:",self.destination)
            print("available seats:",self.seats)
            print()
    tr=Train("12345","Ac","Bangalore","Hyderabad",2)
    print(25*"--","WELCOME TO IRCTC",25*"--")
    print("Name:",name)
    print("Age:",age)
    print("Gender:",gender)
    print("Train name:",train)
    print(50*"  ","PNRNO:",random.randint(222121,232321))
    print(40*"  ","Reservation date:",date)
    tr.display_info()
    print(40*"  ","Number Of Passenger:",pas,"TOTALPRICE:",price)
    print(45*"  ","TOTALPRICE:",price)
    print(25*"--","HAPPY JOURNEY",25*"--")

