####EJERCICIO REALIZADO POR: Oscar Fernández Rodriguez####
"""
Crea un archivo de texto que contenga nombres de archivos (con ruta completa)
Has de leer ese archivo línea a línea y crear las estructuras necesarias (Objetos) para
almacenar en memoria los datos y después mostrarlo por pantalla.
Los archivos seran:
agenda.csv  Contendra los datos de una agenda
red.csv  Cada linea tendra nombre de ordenador, ip, mascara
de red, puerta de enlace.
Lista_compra.csv  Contendra la lista de la compra (cod. Producto,
descripcion, unidades, precio sin iva, iva aplicable, precio
con iva).
"""
import csv, operator
import os

def menu():
	print ("\nSelecciona una opción")
	print ("\t1  - Listar el documento agenda.csv")
	print ("\t2  - Listar el documento red.csv")
	print ("\t3  - Listar el documento Lista_compra.csv")
	print ("\t4  - Listar todos los documentos leyendolos el link ")
	print ("\t0  - Salir")

##### Con este método me aseguro que inserten un string de caracteres no numericos en algunos atributos de la clase
def compruebaCadena(cadena):
	finalBucle = True
	while finalBucle:
		try:
			valor = input(cadena)
			prueba = str(valor)
			if valor == "" or valor == "salir" or valor == "Salir":
				break		
			if valor.isalpha() == True:
				finalBucle = False;
				valor = int(valor)
			else:
				print("\nATENCIÓN: Debe ingresar una cadena de texto no números.\n")
						
		except ValueError:
			pass		
	return valor

##### Este metodo lo usaremos para determinar si los valores enteros que tiene que introducir el usuario son correctos, no pudiendo introducir cosas raras
def lee_entero(cadena):
	finalBucle = True
	while finalBucle:
		try:
			valor = input(cadena)
			if valor == "" or valor == "salir" or valor == "Salir":
				break
				
			if valor == int(valor):
				finalBucle = False;
				valor = int(valor)
			
			return valor
		except ValueError:
			print("ATENCIÓN: Debe ingresar un número entero para esta caracteristica.")
	

####Con esto leo de forma mas bonita el archivo red
def leerRed():
	palabra = 'PC'		#Lo uso como filtro, para determinar la primera columna
	fichero = open('C:\\Users\\ASIR\\Desktop\\PracticaCSV\\red.csv','r')
	leer = csv.reader(fichero,delimiter=';')

	ocurrencias = []
	for linea in leer:
		if palabra in linea:
			contador = linea[0]
			nombre=linea[1]
			ip=linea[2]
			mascara=linea[3]
			conexion=linea[4]
			print("     " + contador + "   " + nombre + "        " + ip+ "           " +mascara + "     " +conexion);
			print("----------------------------------------------------------------------------");
		else:
			contador = linea[0]
			nombre=linea[1]
			ip=linea[2]
			mascara=linea[3]
			conexion=linea[4]
			print("     " + contador + "     " + nombre + "     " + ip+ "     " +mascara + "      " +conexion);


####Con esto leo de forma mas bonita el archivo agenda
def leerAgenda():
	palabra = 'Identificador'		#Lo uso como filtro, para determinar la primera columna
	fichero = open('C:\\Users\\ASIR\\Desktop\\PracticaCSV\\agenda.csv','r')
	leer = csv.reader(fichero,delimiter=';')
	archivoCompleto =[]

	for linea in leer:
		identificador = linea[0]
		nombre=linea[1]
		direccion=linea[2]
		telefono=linea[3]
	
		print("\n######################  CONTACTO: " + identificador + "  ######################\n\tNombre: "+nombre+"\n\tDireccion: "+direccion+"\n\tTelefono: "+telefono +"\n###########################################################");
		archivoCompleto.append(identificador+";"+nombre+";"+direccion+";"+telefono)
	return archivoCompleto

####Con esto leo de forma mas bonita el archivo listaCompra
def leerListaCompra():
	fichero = open('C:\\Users\\ASIR\\Desktop\\PracticaCSV\\Lista_compra.csv','r')
	leer = csv.reader(fichero,delimiter=';')
	ocurrencias = []
	for linea in leer:
		cod = linea[0]
		nombre=linea[1]
		descripcion=linea[2]
		unidades=linea[3]
		precioSinIva=linea[4]
		IvaAplicable=linea[5]
		precioConIva=linea[6]

		print("\n######################  Cod.Producto: " + cod + "  ######################\n\tNombre: "+nombre+"\n\tDescripcion: "+descripcion+"\n\tUnidades: "+unidades +"\n\tPrecio Sin IVA: "+precioSinIva + " Euro." + "\n\tIVA aplicable:  "+IvaAplicable +"\n\tPrecio con IVA: "+precioConIva + " Euro." + "\n###################################################################");

		

########Este metodo me deja leer todos los archivos que haya en el archivo, me da igual el tamaño de cada archivo, no necesito saber sus columnas, pero su visualizacion es mas fea
def leerTresFicheros():
	archivoPrincipal = open('C:\\Users\\ASIR\\Desktop\\PracticaCSV\\leerArchivosTieneTresLinks.txt','r') ;

	while True:
		try:
			ruta = archivoPrincipal.readline()[:-1];
			
			contador = 0
			if ruta != '':
			
				fichero = open(ruta,'r')
				leer = csv.reader(fichero,delimiter=';')
				nombreArchivo = ruta.split("\\\\")		#Esto lo utilizo en la siguiente linea para saber que archivo vamos a visualizar
				print("\nDatos procedentes del archivo: " + nombreArchivo[len(nombreArchivo)-1]+"\n")
				for linea in leer:
					for contador in range(0 ,len(linea)):
						cod = linea[contador]
						contador+=1;
						print("\t"+cod)
					print("##############################################")
			else:
				break;
		except ValueError:
			print("Ha habido algun problema, localice al administrador")
			break
			
		
	archivoPrincipal.close();


####### AQUI ESTA EL PROGRAMA REALMENTE...
while True:
	# Mostramos el menu
	menu();
	opcionMenu = input("inserta un numero >> ")
 
	if opcionMenu=="1":
		print ("")
		os.system('cls') # NOTA para linux has de cambiar cls por clear
		leerAgenda();
	elif opcionMenu=="2":
		print ("")
		os.system('cls') # NOTA para linux has de cambiar cls por clear
		leerRed()
	elif opcionMenu=="3":
		print ("")
		os.system('cls') # NOTA para linux has de cambiar cls por clear
		leerListaCompra()
	elif opcionMenu=="4":
		print ("")
		os.system('cls') # NOTA para linux has de cambiar cls por clear
		leerTresFicheros()

	elif opcionMenu=="0":
		print ("")
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
