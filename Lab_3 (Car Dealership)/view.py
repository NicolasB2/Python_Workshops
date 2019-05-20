from model import *;
class gui:
    def __init__(self):
        self.dealership = Dealership('A0','carNow','#4567','52237876');

    def view(self):

       stop = True
       while(stop):

            print ("********************************************************")
            print ("-> Precione m para ir menu")
            print ("-> Precione s para salir")

            try:

                answer = raw_input()

                if answer == 's':
                   stop =False

                if answer == 'm':
                    self.menu()
                    answer = raw_input()

                if answer == '1':
                    print ("\n**************** Consulta de Cliente ***************")
                    answer = raw_input ("Por favor digite el nombre del paciente\n")
                    x = self.dealership.find_Client(answer)
                    print x.report()

                if answer == '2':
                    print ("\n**************** Agregar Cliente ***************")
                    id   = raw_input ("Por favor digite la cedula del Cliente\n")
                    name = raw_input ("Por favor digite el nombre del Cliente\n")
                    bornDate = raw_input ("fecha de nacimiento del cliente en el formato DD/MM/AAAA\n")
                    salary = raw_input ("Por favor digite el salario (#SMLV) del Cliente\n")
                    phone = raw_input ("Por favor digite el numero de telefono del Cliente\n")
                    adrress = raw_input ("Por favor digite la direccion del Cliente\n")
                    email = raw_input ("Por favor digite el email del Cliente\n")
                    self.dealership.add_Cliente(id,name,bornDate,salary,phone,adrress,email)
                    print ("Cliente Agregado")

                if answer == '3':
                    print ("\n**************** Consulta de Automovil ***************")
                    answer = raw_input ("Por favor digite el modelo del automovil\n")
                    x = self.dealership.find_Automobile(answer)
                    print x.report()

                if answer == '4':
                    print ("\n**************** Agregar Automovil ***************")
                    model = raw_input ("Por favor digite el modelo del vehiculo\n")
                    brand = raw_input ("Por favor digite el modelo del vehiculo\n")
                    price = raw_input ("Por favor digite el modelo del vehiculo\n")
                    reference = raw_input ("Por favor digite el modelo del vehiculo\n")
                    color = raw_input ("Por favor digite el modelo del vehiculo\n")
                    quantity = raw_input ("Por favor digite el modelo del vehiculo\n")

                    self.dealership.add_Automobile(model, brand, price, reference, color, quantity)
                    print ("Vehiculo Agregado")

                if answer == '5':
                    print ("\n**************** Agregar Cantidad de un Automovil ***************")
                    model = raw_input ("Por favor digite el modelo del vehiculo\n")
                    quantity= input ("Por favor digite el numero de vehiculos a agregar\n")

                    self.dealership.increase_quantity(model,quantity)
                    print ("Vehiculos agregados")

                if answer == '6':
                    print ("\n**************** Consulta de Plan de Pago  ***************")
                    answer = raw_input ("Por favor digite el id del Plan\n")
                    x = self.dealership.find_Plan(answer)
                    print x.report()

                if answer == '7':
                    print ("\n**************** Agregar Cliente a un Plan de Pago  ***************")
                    idPlan = raw_input ("Por favor digite el id del Plan\n")
                    idClient = raw_input ("Por favor digite la cedula del Cliente\n")
                    x = self.dealership.add_Client_to_Plan(idClient,idPlan)
                    print ("Cliente agregado al plan")

                if answer == '8':
                    print ("\n**************** Generar Plan de Pago  ***************")
                    model = raw_input ("Por favor digite el modelo del carro para el Plan\n")
                    year = raw_input ("Por favor digite el año en el que se inicia a pagar el plan\n")
                    month = raw_input ("Por favor digite el mes en el que se inicia a pagar el plan\n")
                    clients = raw_input ("Por favor digite el numero de clientes que se van a afiliar al plan\n")
                    type = raw_input ("Por favor el typo de Plan\n")
                    x = self.dealership.generate_Plan(model,year,month,clients,type)
                    print ("Se genero un nuevo plan con codigo "+x)


            except Exception:
                print("Oops! Algo salio mal. Intente nuevamente\n")


    def menu(self):
        print ("\n*********************** MENU ***********************")
        print ("-> 1. Consultar Cliente")
        print ("-> 2. Agregar Cliente")
        print ("-> 3. Consultar Automovil")
        print ("-> 4. Agregar Nuevo Automovil")
        print ("-> 5. Aumentar cantidad de Automoviles")
        print ("-> 6. Consultar Plan de pago")
        print ("-> 7. Agregar Cliente a un Plan de pago")
        print ("-> 8. Crear Plan de pago")
        print ("Digite el numero de la opcion\n")

x = gui();
x.view();
