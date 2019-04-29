from scheme import *

class gui:

   def __init__(self):
        self.clinic = clinic()

   def add_client(self,name,age,stratum):
       pt = pt = patient(name,age,stratum)
       self.clinic.addPatient(pt)

   def find_client(self,name):
       return self.clinic.findPatient(name)

   def report_Scheme(self,name):
       return self.clinic.findPatient(name).reportScheme()

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
                    menu()
                    answer = raw_input()

                if answer == '1':
                    print ("\n**************** Consulta de Paciente***************")
                    answer = raw_input ("Por favor digite el nombre del paciente\n")
                    x = self.find_client(answer)
                    print x.report()

                if answer == '2':
                    print ("\n**************** Agregar Paciente ***************")
                    name = raw_input ("Por favor digite el nombre del paciente\n")
                    age = raw_input ("Por favor digite el numero de meses que tiene paciente\n")
                    stratum = raw_input ("Por favor digite el estrato socio-economico del paciente\n")
                    self.add_client(name,age,stratum)
                    print ("Paciente Agregado")

                if answer == '3':
                    print ("\n**************** Vacunar Paciente ***************")
                    name = raw_input ("Por favor digite el nombre del paciente\n")
                    add_vaccine(self.find_client(name))

                if answer == '4':
                    print ("\n**************** Reporte Paciente ***************")
                    name = raw_input ("Por favor digite el nombre del paciente\n")
                    print self.report_Scheme(name)

            except Exception:
                print("Oops! Algo salio mal. Intente nuevamente\n")


def menu():
    print ("\n*********************** MENU ***********************")
    print ("-> 1. Consultar Paciente")
    print ("-> 2. Agregar Paciente")
    print ("-> 3. Vacunar Paciente")
    print ("-> 4. Reporte Paciente")
    print ("Digite el numero de la opcion\n")


x = gui();
x.view();
