from model import *

class clinic:
    def add_vaccine(self,patient):
        if patient.age==0:
            patient.add_vaccine(vaccine(0,"BCG"))
            patient.add_vaccine(vaccine(0,"Hepatitis B-Primera dosis"))

        if patient.age==2:
            patient.add_vaccine(vaccine(0,"Polio-Primera dosis"))
            patient.add_vaccine(vaccine(0,"Pentavallente"))

            if patient.stratum==1 & patient.stratum==2:
                patient.add_vaccine(vaccine(94000,"NeumoCoco"))
                patient.add_vaccine(vaccine(20000,"RotaVirus"))
            if patient.stratum==3 & patient.stratum==4:
                patient.add_vaccine(vaccine(154000,"NeumoCoco"))
                patient.add_vaccine(vaccine(64000,"RotaVirus"))
            if patient.stratum==5 & patient.stratum==6:
                patient.add_vaccine(vaccine(194000,"NeumoCoco"))
                patient.add_vaccine(vaccine(110000,"RotaVirus"))

        if patient.age==4:
            patient.add_vaccine(vaccine(0,"Polio"))

            if patient.stratum==1 & patient.stratum==2:
                patient.add_vaccine(vaccine(0,"Pentavalente"))
                patient.add_vaccine(vaccine(94000,"NeumoCoco"))
                patient.add_vaccine(vaccine(15000,"RotaVirus"))
            if patient.stratum==3 & patient.stratum==4:
                patient.add_vaccine(vaccine(0,"Pentavalente"))
                patient.add_vaccine(vaccine(154000,"NeumoCoco"))
                patient.add_vaccine(vaccine(59000,"RotaVirus"))
            if patient.stratum==5 & patient.stratum==6:
                patient.add_vaccine(vaccine(35000,"Pentavalente"))
                patient.add_vaccine(vaccine(194000,"NeumoCoco"))
                patient.add_vaccine(vaccine(105000,"RotaVirus"))

        if patient.age==6:
            patient.add_vaccine(vaccine(0,"Polio"))

            if patient.stratum==1 & patient.stratum==2:
                patient.add_vaccine(vaccine(0,"Pentavalente"))
                patient.add_vaccine(vaccine(0,"Influenza"))
            if patient.stratum==3 & patient.stratum==4:
                patient.add_vaccine(vaccine(18000,"Pentavalente"))
                patient.add_vaccine(vaccine(50000,"Influenza"))
            if patient.stratum==5 & patient.stratum==6:
                patient.add_vaccine(vaccine(35000,"Pentavalente"))
                patient.add_vaccine(vaccine(50000,"Influenza"))
