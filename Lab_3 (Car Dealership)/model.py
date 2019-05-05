
class Dealership:
    def __init__(self,nit,name,address,phone):
        self.nit = nit
        self.name = name
        self.address = address
        self.phone = phone
        self.clients = {}
        self.automobiles = {}

class client:
    def __init__(self,id,name,bornDate,salary,phone,address,email):
        self.id = id
        self.name = name
        self.bornDate = bornDate
        self.salary = salary
        self.phone = phone
        self.address = address
        self.email = email

class automobile:
    def __init__(self,model, brand, price, reference, color, quantity):
        self.model = model
        self.brand = brand
        self.price = price
        self.reference = reference
        self.color = color
        self.quantity = quantity

