class Dealership:
    def __init__(self,nit,name,address,phone):
        self.nit = nit
        self.name = name
        self.address = address
        self.phone = phone
        self.clients = {}
        self.automobiles = {}

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
