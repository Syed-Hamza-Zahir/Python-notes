from Passenger_class import *

class Flight(Passenger):
    def __init__(self):
        super().__init__()
        self.origin = ["London", "Birmingham", "Glasgow"]
        self.destination = ["New York", "Birmingham", "Glasgow"]

    def add_origin(self, origin):
        self.origin = origin

    def add_destination(self, destination):
        self.destination = destination

