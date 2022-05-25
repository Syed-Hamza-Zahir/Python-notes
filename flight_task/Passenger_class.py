from Airplane_class import *

class Passenger(airplane):
    def __init__(self, name, passport_ID):
        super().__init__()
        self.name = name
        self.passport_ID = passport_ID
        self.passenger_list = [
            ("Jake Smith", 543657),
            ("Izzy Jones", 235876),
            ("Fred Williams", 346764),
            ("Joanna Rittler", 797382)
        ]

    def add_passenger(self, passenger, passport_ID):
        self.passenger_list.append(passenger)