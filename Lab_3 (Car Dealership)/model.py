class Dealership:
    def __init__(self,nit,name,address,phone):
        self.freeId = 0;
        self.nit = nit
        self.name = name
        self.address = address
        self.phone = phone
        self.clients = {}
        self.automobiles = {}
        self.plans = {}

    def add_Cliente(self,id,name,bornDate,salary,phone,address,email):
        c = Client(id,name,bornDate,salary,phone,address,email);
        self.clients[id]=c;

    def find_Client(self,id):
        return self.clients.get(id)

    def add_Automobile(self,model, brand, price, reference, color, quantity):
        a = Automobile(model, brand, price, reference, color, quantity);
        self.automobiles[model]=a;

    def find_Automobile(self,model):
        return self.automobiles.get(model)

    def increase_quantity(self,model):
        self.automobiles.get(model).quantity+=1;

    def decrease_quantity(self,model):
        self.automobiles.get(model).quantity-=1;

    def next_Free_Id(self):
        self.freeId+=1;
        return self.freeId;

    def generate_Plan(self,auto,startDate,endDate,numClients,type):
        x = self.next_Free_Id()
        f  = Financing_plan(x,auto,startDate,endDate,numClients,type)
        self.plans[x]=f;

    def find_Plan(self,id):
        return self.plans.get(id);


class Financing_plan:
    def __init__(self,id,auto,startDate,endDate,numClients,type):
        self.id=id;
        self.auto=auto;
        self.startDate = startDate;
        self.endDate= endDate;
        self.numClients=numClients;
        self.type_plan = generate(type);


class type_plan:
    def __init__(self,name,minSalary,maxSalary,fee):
        self.name = name;
        self.minSalary=  minSalary;
        self.maxSalary=  maxSalary;
        self.fee = fee;

class Client:
    def __init__(self,id,name,bornDate,salary,phone,address,email):
        self.id = id
        self.name = name
        self.bornDate = bornDate
        self.salary = salary
        self.phone = phone
        self.address = address
        self.email = email

class Automobile:
    def __init__(self,model, brand, price, reference, color, quantity):
        self.model = model
        self.brand = brand
        self.price = price
        self.reference = reference
        self.color = color
        self.quantity = quantity

def generate(self,type):

    if(type == 'basico'):
            return type_plan('basico',1,2,234000)
    if(type == 'plata'):
            return type_plan('plata',3,5,703000)
    if(type == 'oro'):
            return type_plan('oro',5,6,1171000)
    if(type == 'diamante'):
            return type_plan('diamante',7,8,1640000)
    if(type == 'premium'):
            return type_plan('premium',9,10,2109000)
