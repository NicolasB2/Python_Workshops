class clinic:
    def __init__(self):
        self.patients = {}

    def addPatient(self,patient):
        self.patients[patient.name] = patient

    def findPatient(self,name):
        return self.patients.get(name)

class patient:
    def __init__(self,name,age,stratum):
        self.name = name
        self.age = age
        self.stratum = stratum
        self.scheme = scheme()

    def add_vaccine(self,vaccine):
        self.scheme.add_Vaccine(vaccine)

    def report(self):
        return "Name: %s \nAge: %s \nScheme: %s\n" %(self.name,self.age,self.scheme.vaccines.__len__())

    def reportScheme(self):
        return self.scheme.report()

class scheme:
    def __init__(self):
        self.vaccines = []

    def add_Vaccine(self,vaccine):
        self.vaccines.append(vaccine)

    def report(self):
        r = ""
        for x in self.vaccines:
            r += "\t"+x.report()+"\n"
        return r;

class vaccine:
    def __init__(self,cost,name):
        self.cost = cost
        self.name = name

    def report(self):
        return ("Name: %s Cost: %s")%(self.name,self.cost)
