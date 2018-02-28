"""Partiendo de la clase vehículo que hicimos anteriormente,
modifícalo para que la clase inicial sea vehículo cuyo atributo
principal sea el tipo (aéreo, terrestre, marítimo o espacial).

Crea las clases vehículo_aereo, vehículo_terrestre, vehículo_marítimo y
vehículo_espacial con las características propias de cada uno utilizando la herencia
y sus métodos.

Crea además la clase viaje, que modelara los viajes de los vehículos. Tendrá un
origen, un destino, si hace escalas (en caso de hacerlas, cuales serán y en que
orden), la distancia total del viaje, la compañía que lo opera, la compañía que lo
contrata (crea clase compañía, con un CIF, nombre, dirección, teléfono, persona
de contacto y trabajadores), el conductor (será una persona a la que añadiremos
tipo de carnet de conducir, y las fecha de validez del carnet de conducir).

Tanto la persona de contacto como el conductor son personas que tendrán su
DNI, nombre, dirección y teléfono.

Desde el programa principal podremos realizar las siguientes
opciones:
• Listar las compañías
• Listar las personas que trabajan en una compañía
• Listar las compañías con todos sus datos (incluida la lista de personas)
• Despedir(borrar)/contratar(añadir) un trabajador en una compañía
• Listar los viajes, mostrará origen , destino y conductor
• Listar los viajes mostrando toda su información
• Listar los viajes de un conductor
• Crear/Borrar un viaje"""
from datetime import datetime
def menu():
	print ("\nSelecciona una opción")
	print ("\t1  - Listar las compañias")
	print ("\t2  - Listar las persnas que trabajan en una compañia(SOLO EL NOMBRE)")
	print ("\t3  - Listar las persnas que trabajan en una compañia, TODOS SUS DATOS")
	print ("\t4  - Listar las compañías con todos sus datos (incluida la lista de personas)")
	print ("\t5  - Despedir(borrar) un trabajador en una compañía")
	print ("\t6  - Contratar(añadir) un trabajador en una compañía")
	print ("\t7  - Listar los viajes, mostrará origen , destino y conductor")
	print ("\t8  - Listar los viajes mostrando toda su información")
	print ("\t9  - Listar los viajes de un conductor")
	print ("\t10 - Crear un viaje")
	print ("\t11 - Borrar un viaje")
	print ("\t0  - Salir")
class persona:
	def __init__(self,DNI,nombre,direccion,telefono):
		self.DNI=DNI
		self.nombre=nombre
		self.direccion=direccion
		self.telefono=telefono
		
	def __str__(self):
		return "\n\t################### TRABAJADOR " + str(self.nombre.upper())+ " ###################"+  "\n\t\tDNI: " + str(self.DNI) + "\n\t\tNombre: " + str(self.nombre) + "\n\t\tDireccion: " + str(self.direccion) + "\n\t\tTelefono; " + str(self.telefono)
		
	def getNombre(self):
		return str(self.nombre)

class personaContacto(persona):

	pass
		
class conductor(persona):
	def __init__(self,tipoDeCarnet,fechaValidaCarnet,DNI,nombre,direccion,telefono):
		super().__init__(DNI,nombre,direccion,telefono)
		self.tipoDeCarnet=tipoDeCarnet
		self.fechaValidaCarnet=fechaValidaCarnet
		
	
	def __str__(self):
		return super().__str__() + "\n\t\tTipo Carnet: " + self.tipoDeCarnet + "\n\t\tFecha Validacion Carnet: " + self.fechaValidaCarnet + "\n\t########################################################"

class listaTrabajadores(conductor):
	pass

	
class Viaje:	#Modela los viajes de los vehiculos, tendra un origen un destino, si hace escalas, distancia total, la compañia...
	def __init__(self,origen,destino,bolEscala,distanciaTotal,clasCompañiaOpera,clasCompañiaContrata,conductor):
		self.origen=origen
		self.destino=destino
		self.bolEscala=bolEscala
		self.distanciaTotal=distanciaTotal
		self.clasCompañiaOpera=clasCompañiaOpera
		self.clasCompañiaContrata=clasCompañiaContrata
		self.conductor=conductor
		
	def mostrarOrigenDestinoConductor(self):
		haceEscala="No"
		if self.bolEscala:
			haceEscala="Sí"
			
		return "\n\t################ VIAJE DESDE: " + str(self.origen.upper())+ " ################"+  "\n\t\tDestino: " + str(self.destino) +  "\n\t\tConductor: " + self.conductor.nombre+ "\n\t###################################################\n"

	def __str__(self):
		haceEscala="No"
		if self.bolEscala:
			haceEscala="Sí"
			
		return "\n\t################### VIAJE DESDE: " + str(self.origen.upper())+ " ###################"+  "\n\t\tDestino: " + str(self.destino) +  "\n\t\tHace Escala: " + str(haceEscala) + "\n\t\tDistancia: " + str(self.distanciaTotal) + "\n\t\tCompañia ORGANIZA: " + self.clasCompañiaOpera.nombre + "\n\t\tCompañia CONTRATA: " + self.clasCompañiaContrata.nombre + "\n\t\tConductor: " + self.conductor.nombre+ "\n\t########################################################\n"

		

class Compania:
	nombreTrabajadores=""

	def __init__(self,CIF,nombre,direccion,telefono,personaContacto,trabajadores=[]):
		self.CIF=CIF
		self.nombre=nombre
		self.direccion=direccion
		self.telefono=telefono
		self.personaContacto=personaContacto
		for i in range(0,len(trabajadores)):
			self.nombreTrabajadores +=trabajadores[i].nombre+" "
		self.trabajadoresCompleto=trabajadores
		
		
	def getNombreTrabajadores(self):
		nomTrabaja=""
		for i in range(0,len(trabajadoresCompleto)):
			nomTrabaja +=trabajadoresCompleto[i].nombre+" "
		return nomTrabaja
		
	def __str__(self):
		return "\n\tCIF: " + str(self.CIF) + "\n\tNombre: " + str(self.nombre) + "\n\tDireccion: " + str(self.direccion) + "\n\tTelefono; " + str(self.telefono) + "\n\tPersona de Contacto: " +self.personaContacto.getNombre() +"\n\tTrabajadores: " + self.nombreTrabajadores

class Vehiculo:	
	def __init__(self,contador,tip,rueda,colo,puerta,combustibl,ab,fechaFabricacion,paisFabricacion,pinturaMetal,cataliza):
		self.contador = contador			#Es un atributo privado
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
		self.arrancar=False
		self.acelerar=False
		self.reducirVelocidad=False
		
	def arrancar(self):
		self.arrancar=True
	def reducirVelocidad(self):
		self.acelerar=False
		self.reducirVelocidad=True
	def acelerar(self):
		self.reducirVelocidad=False
		self.acelerar=True
		
		
	def toString(self):
		return "#### Vehículo " + str(self.contador) + " ####" + "\nTipo: " + self.tipo + ", Ruedas: " + str(self.ruedas) + ",\nColor: " + self.color + ", Puertas: " + str(self.puertas) + ",\nCombustible: " + str(self.combustible)  + ", ABS: " + str(self.abs) + "\nFecha Fabricación: " + str(self.fechaDeFabricacion) + ",\nPais de Fabricación: " + self.paisDeFabricacion+ ",\nPintura Metalizada: " + str(self.pinturaMetalizada) + ", Catalizador: " + str(self.catalizado) + "." 
				
		
class Vehiculo_Aereo(Vehiculo):
	def __init__(self,alturaMaximaQueAlcanza,bolTripulado,bolTransportaPasajeros):
		super.__init__(contador,tip,rueda,colo,puerta,combustibl,ab,fechaFabricacion,paisFabricacion,pinturaMetal,cataliza)
		self.alturaMaximaQueAlcanza=alturaMaximaQueAlcanza
		self.bolTripulado=bolTripulado
		self.bolTransportaPasajeros=bolTransportaPasajeros

	def turbulencias(self):
		print("Buenos dias pasajeros, soy el capitán y les informa que vamos atravesar ligeras turbulencias, mantengan la calma. Les deseamos un buen viaje")
	def finTurbulencias(self):
		print("Ya hemos pasado las turbulencias, buen viaje")
	
	
	def toString(self):
		super.toString()
		return "Altura máxima que alcanza: " + str(self.alturaMaximaQueAlcanza) + ", Aeronave tripulada: " + self.bolTripulado + ", Transporta pasajeros: " + self.bolTransportaPasajeros

class Vehiculo_Terrestre(Vehiculo):
	def __init__(self,bolLucesAntiNiebla,tipoCombustibleQueUsa,bolElectrico):
		super.__init__(contador,tip,rueda,colo,puerta,combustibl,ab,fechaFabricacion,paisFabricacion,pinturaMetal,cataliza)
		self.bolLucesAntiNiebla=bolLucesAntiNiebla
		self.tipoCombustibleQueUsa=tipoCombustibleQueUsa
		self.bolElectrico=bolElectrico

	def repostarCombustible(self):
		print("Has repostado " + self.tipoCombustibleQueUsa)
	
	
	def toString(self):
		super.toString()
		return "Luces Antiniebla: " + str(self.bolLucesAntiNiebla) + ", Tipo combustible: " + self.tipoCombustibleQueUsa + ", Vehiculo Eléctrico: " + self.bolElectrico


class Vehiculo_Maritimo(Vehiculo):
	def __init__(self,funcionDeVehiculo,numeroVelas,metrosEslora):
		super.__init__(contador,tip,rueda,colo,puerta,combustibl,ab,fechaFabricacion,paisFabricacion,pinturaMetal,cataliza)
		self.funcionDeVehiculo=funcionDeVehiculo					
		self.numeroVelas=numeroVelas
		self.metrosEslora=metrosEslora
		self.abordar=False
		self.encatallar=False
		
	def abordar(self):
		self.abordar=True
	def encallar(self):
		self.encatallar=True
		
		
	def toString(self):
		super.toString()
		return "Se usa para: " + str(self.funcionDeVehiculo) + ", Número velas: " + self.numeroVelas + ", Metros Eslora: " + self.metrosEslora
	


class Vehiculo_Espacial(Vehiculo):
	def __init__(self,numeroTripulacion,companiaOrganizacion):
		super.__init__(contador,tip,rueda,colo,puerta,combustibl,ab,fechaFabricacion,paisFabricacion,pinturaMetal,cataliza)
		self.numeroTripulacion=numeroTripulacion					
		self.companiaOrganizacion=companiaOrganizacion

	def cuentaAtrasDespegue(self):
		num=11
		for i in range(1,num+1):
			if num-i != 0:
				print("     ",num-i)
			else:
				print("  DESPEGAMOS")
		
	def descubrimosMarcianos(self):
		print("Jefe, hemos descubierto marcianos")
		
	def toString(self):
		super.toString()
		return "Número de tripulacion: " + str(self.numeroTripulacion) + ", Compañia/Organización: " + self.companiaOrganizacion


def fechaValCarnet():
	formato = "%d/%m/%Y"
	newFechaFabricacion = 0
	finalBucle = True
	while finalBucle:
		try:
			newFechaFabricacion = input('\t¿Cuando se saco el carnet? (dd/mm/yyyy): ')   
		# Si no se introduce ningún valor se fuerza el final del bucle 
			if newFechaFabricacion == "":
				break
		#Comprobamos que la fecha es del formato deseado
			if datetime.strptime(newFechaFabricacion, formato):
				finalBucle = False
		except:
			print('\tError en la fecha ¡Inténtalo de nuevo!')
	return(newFechaFabricacion)	
	
def comprobarBooleanos(string):
	if(string == 'si' or string == 'Si' or string == 'sí' or string == 'SI' or string == 'SÍ' or string == 'true' or string == 'True' or string == 'TRUE' or string == 'YES' or string == 'yes' or string == 'Yes'):
		resultado = True;
	else:
		resultado = False
	return resultado
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

	
listaCompañiasQueTengo=[]

#Creo una lista de trabajadores para la empresa SOPRANO
listaTrabajadoresSoprano=[]
listaTrabajadoresSoprano.append(conductor("B","17/10/1998","87469524-C","Ramón","Plaza Republica independiente de mi casa","645872148"))
listaTrabajadoresSoprano.append(conductor("A1","09/02/11995","47968852-B","Luis","Calle/Puchdemont president","687952425"))
listaTrabajadoresSoprano.append(conductor("B+E","19/12/2003","96547782-A","Maria","Calle/Invernalia bajo 3","697421547"))
listaTrabajadoresSoprano.append(conductor("D+E","03/04/2006","71264459-D","Maite","Calle/Lannister Mandan","682145658"))
#Creo la persona de contacto con la empresa Soprano
personaContactoSoprano=personaContacto("72897805-C","Maria Soprano","Avenida.Independencia Bajo 4ºC","975687429")
####CREO LA EMPRESA SOPRANO
companiaSopranoCorps=Compania("B245879","Soprano Corps","C/Inventada Bajo","69874587",personaContactoSoprano,listaTrabajadoresSoprano)
#Añado a mi lista la compañia que he creado
listaCompañiasQueTengo.append(companiaSopranoCorps)	

#Creo una lista de trabajadores para la empresa ZARA
listaTrabajadoresZara=[]
listaTrabajadoresZara.append(conductor("D","08/11/1987","85423694-C","Lucas","Plaza Republica independiente de mi casa","645872148"))
listaTrabajadoresZara.append(conductor("A1","09/02/11995","47968852-B","Mateo","Calle/Puchdemont president","687952425"))
listaTrabajadoresZara.append(conductor("B+E","19/12/2003","96547782-A","Olga","Calle/Invernalia bajo 3","697421547"))
listaTrabajadoresZara.append(conductor("D+E","03/04/2006","71264459-D","Isabel","Calle/Lannister Mandan","682145658"))
#Creo la persona de contacto con la empresa ZARA
personaContactoZara=personaContacto("72897805-C","Ortega Lara","Avenida.Independencia Bajo 4ºC","975687429")
####CREO LA EMPRESA ZARA
companiaZara=Compania("A5862178","ZARA S.A","C/Genova 1º","975487524",personaContactoZara,listaTrabajadoresZara)
#Añado a mi lista la compañia que he creado
listaCompañiasQueTengo.append(companiaZara)	

#Creo una lista de trabajadores para la empresa ARDUINO
listaTrabajadoresArduino=[]
listaTrabajadoresArduino.append(conductor("B","17/10/1998","87469524-C","Jose","Plaza Republica independiente de mi casa","645872148"))
listaTrabajadoresArduino.append(conductor("A1","09/02/11995","47968852-B","Alejandro","Calle/Puchdemont president","687952425"))
listaTrabajadoresArduino.append(conductor("B+E","19/12/2003","96547782-A","Judit","Calle/Invernalia bajo 3","697421547"))
listaTrabajadoresArduino.append(conductor("D+E","03/04/2006","71264459-D","Eva","Calle/Lannister Mandan","682145658"))
listaTrabajadoresArduino.append(conductor("D+E","03/04/2006","71264459-D","Sergio","Calle/Lannister Mandan","682145658"))
#Creo la persona de contacto con la empresa ZARA
personaContactoArduino=personaContacto("784451218-C","Oscar Fernandez","C/.De mi casa porque quiero Bajo","975687429")
####CREO LA EMPRESA ZARA
companiaArduino=Compania("C2151315","Arduino S.L","Plaza.Viva SoftwareLibre","67412145",personaContactoArduino,listaTrabajadoresArduino)
#Añado a mi lista la compañia que he creado
listaCompañiasQueTengo.append(companiaArduino)	



################ CREO LOS VIAJES, NO TIENE MUCHO SENTIDO VOLVER A CREAR OBJETOS TRABJADORES, ASI QUE USO LOS QUE EXITEN, SI SE CARGAN A TRABAJADOR MANO#############################
listaViajes =[]
viaje1 = Viaje("León","Paris",False,2567,listaCompañiasQueTengo[0],listaCompañiasQueTengo[2],listaCompañiasQueTengo[0].trabajadoresCompleto[0])
viaje2 = Viaje("Madrid","Londres",False,3000,listaCompañiasQueTengo[0],listaCompañiasQueTengo[2],listaCompañiasQueTengo[0].trabajadoresCompleto[0])
viaje3 = Viaje("Barcelona","Tunez",False,7000,listaCompañiasQueTengo[1],listaCompañiasQueTengo[2],listaCompañiasQueTengo[1].trabajadoresCompleto[2])
viaje4 = Viaje("Valencia","Moscu",False,10000,listaCompañiasQueTengo[1],listaCompañiasQueTengo[2],listaCompañiasQueTengo[1].trabajadoresCompleto[2])
viaje5 = Viaje("Lugo","Pontevedra",False,200,listaCompañiasQueTengo[2],listaCompañiasQueTengo[2],listaCompañiasQueTengo[2].trabajadoresCompleto[1])

listaViajes.append(viaje1)	
listaViajes.append(viaje2)
listaViajes.append(viaje3)
listaViajes.append(viaje4)
listaViajes.append(viaje5)
####### AQUI ESTA EL PROGRAMA REALMENTE...
while True:

	# Mostramos el menu
	menu();
	opcionMenu = input("inserta un numero >> ")
 
	if opcionMenu=="1":		#Listar las compañías
		print ("")
		for i in range(0,len(listaCompañiasQueTengo)):
			print("\t"+listaCompañiasQueTengo[i].nombre+" ")

	elif opcionMenu=="2":	#Listar las persnas que trabajan en una compañia
		print ("")
		try:
			####Muestro el nombre de las empresas que hay#####
			for i in range(0,len(listaCompañiasQueTengo)):
				print("\tID: "+ str(i)+ " " +listaCompañiasQueTengo[i].nombre+" ")
		
			identificadorEmpresa = int(input("\t¿De que compañia quieres ver la lista de trabajadores?(ESCRIBRE EL ID) "))
			print("\n\t*"+listaCompañiasQueTengo[identificadorEmpresa].nombreTrabajadores)
			
		except:
			print("Lo sentiemos, la empresa con el identificador " + str(identificadorEmpresa) + " no ha sido encontrada")	
			
	elif opcionMenu=="3":	#Listar las persnas que trabajan en una compañia, TODOS SUS DATOS
		print ("")
		try:
			####Muestro el nombre de las empresas que hay#####
			for i in range(0,len(listaCompañiasQueTengo)):
				print("\tID: "+ str(i)+ " " +listaCompañiasQueTengo[i].nombre+" ")
		
			identificadorEmpresa = int(input("\t¿De que compañia quieres ver la lista de trabajadores?(ESCRIBE EL ID) "))
			###CON ESTO SACO EL LISTADO COMPLETO DE LOS TRABAJADORES QUE HAY EN LA EMPRESA QUE HAN MARCADO
			for i in range(0,len(listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto)):
				print(listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto[i].__str__())

		except:
			print("Lo sentiemos, la empresa con el identificador "  + " no ha sido encontrada")		

			
	elif opcionMenu=="4":		#Listar las compañías con todos sus datos (incluida la lista de personas)
		print ("")
		
		for i in range(0,len(listaCompañiasQueTengo)):
			print("\t"+listaCompañiasQueTengo[i].__str__()+" ")
			

	elif opcionMenu=="5":		#Despedir(borrar) un trabajador en una compañía
		try:
			####Muestro el nombre de las empresas que hay#####
			for i in range(0,len(listaCompañiasQueTengo)):
				print("\tID: "+ str(i)+ " " +listaCompañiasQueTengo[i].nombre+" ")
	
			identificadorEmpresa = int(input("\t¿De que compañia quiere despedir?(ESCRIBE EL ID) "))
			
			###CON ESTO SACO EL LISTADO COMPLETO DE LOS TRABAJADORES QUE HAY EN LA EMPRESA QUE HAN MARCADO
			for i in range(0,len(listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto)):
				print("\tIDENTIFICADOR:"+str(i)+listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto[i].__str__()+"\n")
			identificadorTrabajador = int(input("\t¿Que trabajador quiere despedir?(ESCRIBE EL ID) "))
			
			#En este cacho obtengo todos los nombres de nuevo, pero sin el que ha selecionado el usuario(ya esta despedido)
			guardoNombreTrabajadores=""
			for i in range(0,len(listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto)):
				if listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto[identificadorTrabajador].nombre != listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto[i].nombre:
					guardoNombreTrabajadores +=listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto[i].nombre +" "
			
			#Con esto he actualizado el atributo con el nuevo valor
			setattr(listaCompañiasQueTengo[identificadorEmpresa],'nombreTrabajadores',guardoNombreTrabajadores)
			
			listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto.pop(identificadorTrabajador)	#Le digo que busque de la lista que tengo, que me de el elemento trabajadores, y que me borre el que quiere el usuario
			#DESPEDIMOS AL TRABAJADOR, SIMPLEMENTE ACTUALIUZAMOS LOS ATRIBUTOS
			setattr(listaCompañiasQueTengo[identificadorEmpresa],'trabajadoresCompleto',listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto)
			print("\n\tHas despedido al trabajador con Identificador " + str(identificadorTrabajador) + ", su familia no comerá el próximo mes =(")	


		except:
			print("\n\tLo sentiemos, no se ha podido despedir a nadie =D ")		
			
	elif opcionMenu=="6":		#Contratar(añadir) un trabajador en una compañía
		try:
		####Muestro el nombre de las empresas que hay#####
			for i in range(0,len(listaCompañiasQueTengo)):
				print("\tID: "+ str(i)+ " " +listaCompañiasQueTengo[i].nombre+" ")
	
			identificadorEmpresa = int(input("\t¿Para que compañia quieres contratar?(ESCRIBE EL ID) "))

			newCarnet = input("\t¿Que tipo de carnet tiene? ")
			newFechaValided=fechaValCarnet()
			newDni = input("\tEscriba su DNI: ")
			newNombre = input("\t¿Cual es su nombre? ")
			newDireccion = input("\t¿Cual es su direccion? ")
			newDni = input("\tTelefono: ")
			
			#Con esto obtengo el nombre de todos los trabajadores que hay en esta empresa despues le añado el nombre del nuevo trabajador y actualizo la lista
			guardoNombreTrabajadores=""
			for i in range(0,len(listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto)):
				guardoNombreTrabajadores +=listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto[i].nombre +" "
			
			guardoNombreTrabajadores += newNombre
			
			#Con esto he actualizado el atributo con el nuevo valor
			setattr(listaCompañiasQueTengo[identificadorEmpresa],'nombreTrabajadores',guardoNombreTrabajadores)
			
			listaCompañiasQueTengo[identificadorEmpresa].trabajadoresCompleto.append(conductor(newCarnet,newFechaValided,newDni,newNombre,newDireccion,newDni))
			print("\n\tEstupendo, has contratado a una nueva persona para la empresa " + listaCompañiasQueTengo[identificadorEmpresa].nombre)

		except:
			print("\n\tLo sentiemos, no se ha podido despedir a nadie =D ")		
			
	elif opcionMenu=="7":		#Listar los viajes, mostrará origen , destino y conductor
		print ("")
		
		for i in range(0,len(listaViajes)):
			print("\tIDENTIFICADOR: " +str(i) +listaViajes[i].mostrarOrigenDestinoConductor())
			
	elif opcionMenu=="8":		#Listar los viajes mostrando toda su informacion
	
		print ("")
		for i in range(0,len(listaViajes)):
			print("\tIDENTIFICADOR: " +str(i) +listaViajes[i].__str__())
	elif opcionMenu=="9":		#Listar los viajes de un conductor
		print ("")
		print("Aun en construccion")
	elif opcionMenu=="10":		#Crear/Borrar un viaje
		print ("")
		try:
			viaje1 = Viaje("León","Paris",False,2567,listaCompañiasQueTengo[0],listaCompañiasQueTengo[2],listaCompañiasQueTengo[0].trabajadoresCompleto[0])

			newOrigen= input("\t¿Cual es el origen? ")
			newDestino= input("\t¿Cual es el destino? ")
			newEscala= input("\t¿Tiene escalas? ")
			newEscala=comprobarBooleanos(newEscala)
			newDistancia= lee_entero("\t¿Cuanto es la distancia? (km) ")
			####Muestro el nombre de las empresas que hay#####
			for i in range(0,len(listaCompañiasQueTengo)):
				print("\tID: "+ str(i)+ " " +listaCompañiasQueTengo[i].nombre+" ")
				
			newNombreEmpresaOrganiza= int(input("\t¿Que compañia Organiza? (ID) "))

			####Muestro el nombre de las empresas que hay#####
			for i in range(0,len(listaCompañiasQueTengo)):
				print("\tID: "+ str(i)+ " " +listaCompañiasQueTengo[i].nombre+" ")
			newCompañiaContrata= int(input("\t¿Que compañia Contrata? "))
		
			###CON ESTO SACO EL LISTADO COMPLETO DE LOS TRABAJADORES QUE HAY EN LA EMPRESA QUE HAN MARCADO
			for i in range(0,len(listaCompañiasQueTengo[newNombreEmpresaOrganiza].trabajadoresCompleto)):
				print("\tIDENTIFICADOR:"+str(i)+listaCompañiasQueTengo[newNombreEmpresaOrganiza].trabajadoresCompleto[i].__str__()+"\n")
			newConductor= int(input("\t¿Que empleado conduce? "))
		
			#Creo el viaje
			
			newViaje = Viaje(newOrigen,newDestino,newEscala,newDistancia,listaCompañiasQueTengo[newNombreEmpresaOrganiza],listaCompañiasQueTengo[newCompañiaContrata],listaCompañiasQueTengo[newNombreEmpresaOrganiza].trabajadoresCompleto[newConductor])
			listaViajes.append(newViaje)	
			print("\t" +newViaje.__str__())
		except:
			print("\n\tLo sentiemos, algo ha salido mal, no se ha podido crear el viaje")	
		
		
	elif opcionMenu=="11":		#Borrar un viaje
		print ("")
		print("Aun en construccion")
		
		try:
			####Muestro los viajes a ser borrar ando con cuidado#####
			for i in range(0,len(listaViajes)):
				print("\tIDENTIFICADOR: " +str(i) +listaViajes[i].__str__())

			
			identificadorTrabajador = int(input("\t¿Cual quieres borrar?(ESCRIBE EL ID) "))
			
			
			listaViajes.pop(identificadorTrabajador)	#elimino el viaje
			
			print("\n\tHas eliminado el viaje " + str(identificadorTrabajador) + ", tu dinero se abonara en tu cuenta en los proximos dias")	

		except:
			print("\n\tLo sentiemos, no has podido borrar nada  ")		

	elif opcionMenu=="0":
		print ("")
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")	


