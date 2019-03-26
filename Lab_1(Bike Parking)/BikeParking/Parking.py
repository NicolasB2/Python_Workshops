from Employee import *


class Parking:
    def __init__(self, name, bikes, latitude, longitude):
        self.name = name
        self.bikes = bikes
        self.latitude = latitude
        self.longitude = longitude
        self.employee = None

    def num_bikes(self):
        return self.bikes

    def add_bike(self):
        self.Bikes + 1

    def remove_Bike(self):
        self.bikes - 1

    def report(self):
        return "%s\n%s" % (self.name, self.employee.report())
