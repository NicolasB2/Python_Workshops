class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def report(self):
        return "id: %s\nname: %s\n"%(self.id,self.name)
