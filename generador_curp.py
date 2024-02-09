# hacer un progreama que genere una curp hipotetica tomando los siguientes valores
#inicial del apellido paterno y materno, como la inincial del nombre(s)

nombre = input("ingrese su nombre: ")
nombre2=  input("ingrese su nombre secundario: ")
apellidop= input("ingresen su apellido paterno: ")
apellidoM= input("ingrese su apellido materno: ")
añoN = input("ingrse su año de nacimiento: ")
mesN = input ("ingrese mes de nacimiento: ")
diaN = input ("ingrese dia de nacimiento")

nombreCom =[]
apellidoPat = apellidop[0]
apellidoMat= apellidoM[0]
nombreA=nombre[0]
nombreB=nombre2[0]
añonacimiento =añoN [2]
añonacimiento2 =añoN[3]
mesnacimiento= mesN [0]
mesnacimiento2 =mesN [1]
dianacimiento =diaN [0]
dianacimiento2 = diaN [1] 

curp=apellidoPat + apellidoPat + apellidoMat +nombreA + nombreB + añonacimiento + añonacimiento2 + mesnacimiento + mesnacimiento2 + dianacimiento + dianacimiento2

print ("tu curp es: ",curp.upper())
#variables individuales para mejorar el orden 0