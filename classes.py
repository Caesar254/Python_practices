class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if not self.open_seats(): #if open _seats == 0
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
       
        return self.capacity - len(self.passengers)     

    
flight =  Flight(3)

   
people = ["Wednesday", "Tyler", "Enid", "Bianca","Xavier"]
for person in people:
    success =  flight.add_passenger(person)
    if success:
        print( f"Added {person} to  flight successfully")
    else:
        print( f"No available seats  for {person}")

