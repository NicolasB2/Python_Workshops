from scheme import *

class gui:

   def __init__(self):
        self.clinic = clinic()

   def view(self):
       stop = True
       while(stop):

            print ("")
            print ("-> Precione m para ir menu")
            print ("-> Precione s para salir")

            answer = raw_input()

            if answer == 's':
               stop =False

            if answer == 'm':
                menu()
                answer = raw_input()

            if answer == '1':
                print ("\n****************Consulta de pacientes***************")

            if answer == '2':
                print ("\n**************** Agregar Cliente ***************")

            if answer == '3':
                print ("\n**************** Vacunar Cliente ***************")
                
            if answer == '4':
                print ("\n**************** Reporte Cliente ***************")


def menu():
    print ("\n*********************** MENU ***********************")
    print ("-> 1. Consultar pacientes")
    print ("-> 2. Agregar Cliente")
    print ("-> 3. Vacunar Cliente")
    print ("-> 4. Reporte Cliente")
    print ("Digite el numero de la opcion\n")



x = gui();
x.view();
