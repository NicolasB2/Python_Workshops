import math

from Parking import *


class Mio:
    def __init__(self):
        self.parking_lot = {}

    def add_Parking(self,parking):
        self.parking_lot[parking.name] = parking

    def find_Parking(self,name):
        return self.parking_lot.get(name)

    def delete_Parking(self,name):
        del self.parking_lot[name]

    def calculate_distance(self,name_1,name_2):
        x = self.parking_lot.get(name_1)
        y = self.parking_lot.get(name_2)
        lat = (x.latitude - y.latitude)**2
        lon = (x.longitude - y.longitude)**2
        print "Distance between %s and %s : %s" %(name_1,name_2,math.sqrt(lat+lon))

    def report_Bikes(self):
       r = self.parking_lot.values()
       for x in r:
           print "Station Name: %s - bikes %s" % (x.name,x.bikes)

    def report_Parking(self):
       r = self.parking_lot.values()
       for x in r:
           print x.report()
