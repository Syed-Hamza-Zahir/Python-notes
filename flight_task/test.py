from Flight_class import *
from Passenger_class import *

name = input("What is the passengers' name?: ")
passport_ID = input("What is the passengers' passport number? ")

new_passenger = Passenger(name, passport_ID)
Passenger.append(new_passenger)

print(f"The passenger {new_passenger.name}({new_passenger.passport_num}) has been successfully created.")