def gui():

   stop = True
   while(stop):

        print ("")
        print ("-> Precione m para regresar al menu")
        print ("-> Precione s para salir")

        answer = raw_input()

        if answer == 's':
           stop =False

        if answer == 'm':
            menu()
            answer = raw_input()

        if answer == '1':
            print ("\n****************Consulta de pacientes***************")
            print ("resultado de la consultta\nmuestra datos del paciente\nby nicolas\nthanks")

        if answer == '2':
            print ("\n*********Reporte de vacunas de un paciente**********")

        if answer == '3':
            print ("*************totales recibos por cliente**************")


def menu():
    print ("\n*********************** MENU ***********************")
    print ("-> 1. Consultar pacientes")
    print ("-> 2. Reporte de vacunas de un paciente")
    print ("-> 3. totales recibos por cliente")
    print ("")
    print ("Digite el numero de la opcion\n")



x = gui();
