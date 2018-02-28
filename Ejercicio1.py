####EJERCICIO REALIZADO POR: Oscar Fernández Rodriguez####

"""
• Crear la clase vehículos que modele los diferentes vehículos
(tipo, ruedas, color, puertas, combustible, abs) y sus métodos.
• Añadir a la clase anterior, los atributos “fecha de fabricación”, “país de
fabricación”, “pintura metalizada” y “catalizado”, así como los métodos
asociados
• Añadir el método que permita eliminar un vehículo de la lista
• Crear un programa principal que nos permita a través de un menú, crear
una serie de vehículos ( por cada vehículo nos pida sus características). Al
dar a la opción de salir, ha de hacer un listado de los vehículos que
tenemos creados.
"""
import os
from datetime import datetime			#Lo uso para la fecha de fabricacion, ya que creo que en el enunciado al utilizar la palbra fecha de fabricacion se nos obliga a utilizar formato fecha y no string

class Vehiculo:	
	def __init__(self,contador,tip,rueda,colo,puerta,combustibl,ab,fechaFabricacion,paisFabricacion,pinturaMetal,cataliza):
		self.contador = contador			
		self.tipo=tip;
		self.ruedas=rueda;
		self.color=colo;
		self.puertas=puerta;
		self.combustible=combustibl;
		self.abs=ab;
		self.fechaDeFabricacion=fechaFabricacion;
		self.paisDeFabricacion=paisFabricacion;
		self.pinturaMetalizada=pinturaMetal;
		self.catalizado=cataliza;
		
		
	def toString(self):
		imprimirAbs="No"							#Considero que el usuario no tiene porque saber que es eso de True o de False, asi que lo amoldo a su conocimiento
		imprimirPinturaMetalizada="No"
		imprimirCatalaizador="No"
		if self.abs:
			imprimirAbs="Sí"
		if self.pinturaMetalizada:
			imprimirPinturaMetalizada="Sí"
		if self.catalizado:
			imprimirCatalaizador="Sí"
		return "####### Vehículo " + str(self.contador) + " ##############" + "\n\tTipo: " + self.tipo + ", Ruedas: " + str(self.ruedas) + ",\n\tColor: " + self.color + ", Puertas: " + str(self.puertas) + ",\n\tCombustible: " + str(self.combustible)  + ", ABS: " + imprimirAbs + "\n\tFecha Fabricación: " + str(self.fechaDeFabricacion) + ",\n\tPais de Fabricación: " + self.paisDeFabricacion+ ",\n\tPintura Metalizada: " + imprimirPinturaMetalizada + ",\n\tCatalizador: " + imprimirCatalaizador + "\n############ FINAL VEHICULO ############\n" 
				

																															
################################## TERMINA LA CLASE ######################################

diccionarioVehiculos={}	#Creo un diccionario vacio, en el se guardaran los objeto vehiculos


##### Menu para elegir que quiero
def menu():
	print ("\nSelecciona una opción")
	print ("\t1 - Dar de alta nuevo Vehiculo")
	print ("\t2 - Cargar lista de Vehiculos Predefinida")
	print ("\t3 - Ver todos los Vehiculo")
	print ("\t4 - Borrar Vehiculo")
	print ("\t5 - Limpiar pantalla")
	print ("\t0 - Salir")

#####  Con esto consigo la clave y el contador de mis vehiculos
def contador ():
	contador = len(diccionarioVehiculos)	
	finalBucle = True
	while finalBucle:
		if contador in diccionarioVehiculos.keys():		#Pregunto si el contador esta en el array de claves del diccionario
			contador += 1
			
		else:
			finalBucle = False
			break
	return(contador)	
	
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

##### Este metodo lo usaremos para determinar si los valores booleanos que preguntaremos al usuario son correctos
def comprobarBooleanos(string):
	if(string == 'si' or string == 'Si' or string == 'sí' or string == 'SI' or string == 'SÍ' or string == 'true' or string == 'True' or string == 'TRUE' or string == 'YES' or string == 'yes' or string == 'Yes'):
		resultado = True;
	else:
		resultado = False
	return resultado

##### Este metodo nos ayuda a comprobar que la fecha introducida sea correcta con un formato válido
def fechaFabricacionVehiculo():
	formato = "%Y"
	newFechaFabricacion = 0
	finalBucle = True
	while finalBucle:
		try:
			newFechaFabricacion = input('Introducir el año de fabricación (aaaa): ')   
   # Si no se introduce ningún valor se fuerza el final del bucle 
			if newFechaFabricacion == "":
				break
	#Comprobamos que la fecha es del formato deseado
			if datetime.strptime(newFechaFabricacion, formato):
				finalBucle = False
		except:
			print('Error en la fecha ¡Inténtalo de nuevo!')
	return(newFechaFabricacion)
		

##### Este metodo nos sirve para dar de alta un Vehiculo, sera el metodo a ejecutar de nuestro menu
def darDeAltaVehiculo():
	print("Bienvenido, vamos a dar de alta un nuevo vehículo\n")
	
	try:
	#Voy pidiendo todos los datos al usuario y valido que sean correctos, si el usuario lo deja vacio le dejo que sean datos vacios, si el cliente no lo quiere es facil de modificar
		newTipo = compruebaCadena("*Tipo de vehículo,Bicicleta,Ciclomotor,Turismo ---> ")
		newRuedas=lee_entero("*Número de ruedas que tiene el vehículo ---> ")	#Llamo a mi metodo para que metan un valor correcto
		newColor = compruebaCadena("*Escribe el color del vehículo ---> ")
		newPuertas=lee_entero("*Numero Puertas ---> ")							#Llamo a mi metodo para que metan un valor correcto
		newCombustible = lee_entero("*Litros de combustible ---> ")				#Llamo a mi metodo para que metan un valor correcto
		newAbs = input("*¿Tiene Abs? ---> ")
		newAbs = comprobarBooleanos(newAbs)
		newFechaFabricacion = fechaFabricacionVehiculo()	#Este es el dato mas peligroso ya que nos dice que tiene que ser una fecha por eso tiene un metodo aparte
		newPaisDeFabricacion = compruebaCadena("*País de fabricación del vehículo ---> ")
		newPinturaMetal = input("*¿Tiene pintura metálica? ---> ")
		newPinturaMetal = comprobarBooleanos(newPinturaMetal)
		newCatalizador = input("*¿Tiene catalizador? ---> ")
		newCatalizador = comprobarBooleanos(newCatalizador)
	#Inserto todos estos datos y creo un nuevo elemento del diccionario diccionarioVehiculos, para poder visualizarlo lo que inserto realmente es el toString de la clase	
		nuevoVehiculo=Vehiculo(contador(),newTipo,newRuedas,newColor,newPuertas,newCombustible,newAbs,newFechaFabricacion,newPaisDeFabricacion,newPinturaMetal,newCatalizador);
		diccionarioVehiculos[str(nuevoVehiculo.contador)]=nuevoVehiculo.toString()
	#Imprimo el vehiculo que he introducido	
		print("")
		print(nuevoVehiculo.toString());	
	except ValueError:
		print("No se ha registrado el vehículo correctamente")

##### Este metodo nos imprime todos los vehiculos que esten dentro de nuestro diccionario, se ejecuta como opcion 3 del menu		
def verTodosLosVehiculos():
	clave = diccionarioVehiculos.keys()
	valores = diccionarioVehiculos.values()
	elementos = diccionarioVehiculos.items()
	for clave, valores in elementos:
		print("ID:",clave,"",valores)

##### Simplemente elimina un elemento del diccionario, necesita una clave, sino existe nos lo avisa	
def eliminarElemntoDiccionario(clave):
	
	try:
		print("\nID: "+str(clave)+"  "+diccionarioVehiculos[str(clave)])
		confirmacion = input("\n¿Estas seguro que quieres eliminar el vehiculo "+clave+" (si/no) :")	
		
		if confirmacion=="si" or confirmacion=="Si" or confirmacion=="Sí" or confirmacion=="SI" or confirmacion=="sI" :
			del diccionarioVehiculos[str(clave)]
			print("\n\tEl Vehículo " + str(clave) + " ha pasado a mejor vida, ya no existe")
		else:
			print("\n\tFinalmente no has eliminado el vehículo")
	except:
		print("Lo sentiemos, el vehículo " + str(clave) + " no puede ser borrado, revisa si está en la siguiente lista")		
		key= diccionarioVehiculos.keys()	
		for key in diccionarioVehiculos:
			print("\tID:",key," ")

		
####### AQUI ESTA EL PROGRAMA REALMENTE...
while True:
	# Mostramos el menu
	
	menu();
	opcionMenu = input("inserta un numero >> ")
 
	if opcionMenu=="1":
		print ("")
		darDeAltaVehiculo();
	elif opcionMenu=="2":
		print ("")
		#Cargo lista de datos predeterminada, he puesto estos por que si...
		miVehiculo1 = Vehiculo(contador(),"Turismo",4,"Rojo",5,1200,True,"1992","España",False,True);
		diccionarioVehiculos[str(miVehiculo1.contador)]=miVehiculo1.toString()
		
		miVehiculo2 = Vehiculo(contador(),"Quard",4,"Azul",0,800,True,"1999","España",False,True);
		diccionarioVehiculos[str(miVehiculo2.contador)]=miVehiculo2.toString()
		
		
		miVehiculo3 = Vehiculo(contador(),"Bicicleta",2,"Negra",0,0,False,"2016","España",False,False);
		diccionarioVehiculos[str(miVehiculo3.contador)]=miVehiculo3.toString()
		
		#diccionarioVehiculos = {miVehiculo1.contador:miVehiculo1.toString(),miVehiculo2.contador:miVehiculo2.toString(),miVehiculo3.contador:miVehiculo3.toString()}
		print("Tienes cargados " + str(len(diccionarioVehiculos)) + " vehiculos para trabajar")
	elif opcionMenu=="3":
		print ("")
		verTodosLosVehiculos()
	elif opcionMenu=="4":
		print ("")
		os.system('cls') # NOTA para linux has de cambiar cls por clear
		verTodosLosVehiculos()
		
		if len(diccionarioVehiculos) >=1:
			clave= diccionarioVehiculos.keys()	
			print("Selecione una de las siguientes claves ---> " )
			for clave in diccionarioVehiculos:
				print("\tID:",clave," ")
		
			clave = input("Selecione una de los ID para eliminar el objeto Vehiculo ")
			eliminarElemntoDiccionario(clave)
			

	elif opcionMenu=="5":
		print ("")
		#Eliminamos todo de la pantalla
		os.system('cls') # NOTA para linux has de cambiar cls por clear

	elif opcionMenu=="0":
		print ("")
		verTodosLosVehiculos()
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")