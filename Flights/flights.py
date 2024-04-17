class Flight():
    # Method to create new flight with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    # Method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    # Method to add a passenger to the flight:
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

# Create a new flight with own capacity
flight = Flight(3)

# Create a list of passengers and add them to the flight
while flight.open_seats() > 0:
    name = input("Enter passenger name: ")
    if flight.add_passenger(name):
        print(f"Passenger {name} added to the flight.")

# If no more seats available, print message
if flight.open_seats() == 0:
    print("No more seats available.")
