# hacer un progreama que genere una curp hipotetica tomando los siguientes valores
#inicial del apellido paterno y materno, como la inincial del nombre(s)

nombre = input("ingrese su nombre: ")
nombre2=  input("ingrese su nombre secundario: ")
apellidop= input("ingresen su apellido paterno: ")
apellidoM= input("ingrese su apellido materno: ")

nombreCom =[]
apellidoPat = apellidop[0]
apellidoMat= apellidoM[0]
nombreA=nombre[0]
nombreB=nombre2[0]
curp= apellidoPat + apellidoMat +nombreA + nombreB

print ("tu curp es: ",curp.upper())