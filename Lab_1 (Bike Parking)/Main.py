from email.mime.application import MIMEApplication

from Project import *


class Test:
    def test_1(self):

        mio = Mio()
        p1 = Parking("icesi", 25, 3456, 34567)
        p1.employee = Employee("1234", "Nicolas")

        p2= Parking("javeriana", 10, 4566, 33876)
        p2.employee = Employee("1234", "David")

        p3= Parking("autonoma",18, 3611, 37890)
        p3.employee = Employee("1234", "Daniela")

        mio.add_Parking(p1)
        mio.add_Parking(p2)
        mio.add_Parking(p3)

        mio.calculate_distance("icesi","javeriana")
        print ""
        mio.report_Bikes()
        print ""
        mio.report_Parking()


t = Test()
t.test_1()
