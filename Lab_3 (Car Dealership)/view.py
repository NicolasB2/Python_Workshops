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

                    x = self.dealership.add_Automobile(model, brand, price, reference, color, quantity)
                    print ("Vehiculo Agregado")


            except Exception:
                print("Oops! Algo salio mal. Intente nuevamente\n")


    def menu(self):
        print ("\n*********************** MENU ***********************")
        print ("-> 1. Consultar Cliente")
        print ("-> 2. Agregar Cliente")
        print ("-> 3. Consultar Automovil")
        print ("-> 4. Agregar Automovil")
        print ("Digite el numero de la opcion\n")

x = gui();
x.view();
