class patient:
    def __init__(self,name,age,stratum,scheme):
        self.name = name
        self.age = age
        self.scheme = scheme
        self.stratum= stratum

    def report(self):
        print("Name: %s\nAge: %s\nScheme")%(self.name,self.age,self.scheme.report)

    def add_vaccine(self,vaccine):
        scheme.add_Vaccine(vaccine)

class scheme:
    def __init__(self):
        self.vaccines = []

    def add_Vaccine(self,vacinne):
        self.vaccines.append(vaccine)

    def report(self):
        r = ""
        for x in self.vaccines:
            r += x.report+"\n"
        return r;

class vaccine:
    def __init__(self,cost,name):
        self.cost = cost
        self.name = name

    def report(self):
        return ("Name: %s\nCost: %s")%(self.name,self.cost)
