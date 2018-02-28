####EJERCICIO REALIZADO POR: Oscar Fernández Rodriguez####
"""
El ejercicio que debeis hacer es:

En base a lo aprendido hasta ahora, debereis crear un objeto que maneje el acceso a la base de datos,
 ya sea postgres o mysql. Los metodos que tiene que tener esta clase y que son los unicos a los que podremos acceder son:
Conectar a una BBDD
Cerrar la conexión a una BBDD
Ejecutar una consulta (Si ya antes en este objeto se hubiera o hubiese ejecutado una consulta, se debera ejecutar la nueva y 
se rellenaran de nuevo los cursores necesarios)
Devolver una a una las filas de la consulta que se le ha dado al objeto
Devolver todas las filas de la consulta que se le ha dado al objeto
Insertar datos en una tabla
Ejecutar una sentencia de modelado de base de datos (Borrar tabla o crear tabla)
"""

import MySQLdb
import exceptions
import csv, operator
 
class ClaseBDD(object):
	conectado	#Esta variable sera un atributo de la case, simplemente es un estado booleando la cual cambia en funcion de si esta conectado o no
	error		#Con este atributo de la clase escribiremos el error que queremos en funcion del error que nos pueda dar
	db			#Será el conector de la clase, en este atributo guardamos los datos de la conexión creada (host, usuario, contraseña, nombre....)
	cursor		#Será el cursor de la base de datos, guardaremos en el las consultas deseadas
 
	def __init__(self):
		self.conectado=0	#Nada mas crear un objeto de la clase, el objeto se inicializa vacio y desconectado
		self.error=""
 
	def ConectarBaseDatos(self,host,usuario,contrasenia,nombreBDD,puerto):
		try:
			self.db = MySQLdb.connect(host,usuario,contrasenia,nombreBDD)	#Guardo como atributo la base de datos creada
			self.cursor = self.db.cursor()									#Guardo como atributo el cursor
			self.conectado=1
		except Exception as e:
			self.error="Error: %s" % (e)
		except:
			self.error="Error desconocido"
        
	def CerrarConexion(self):
		self.conectado=0
		try:
			self.cursor.close()
			self.db.close()
		except:pass

		
	def EjecutarConsulta(self,instruccion):
		#instruccion="SELECT * FROM TABLA"		#NO SE ESPECIFICA COMO SE VA A TRABAJAR ESTE METODO ASI QUE QUEDA ABIERTO A INTERPRETACIONES
		if self.conectado:						#Compruebo que la base este conectada antes, si lo es asi intento guardar la sentencia que pasan en el cursor
			self.error=""
			try:
				self.cursor = self.cursor.execute(instruccion)		
				self.db.commit()
			except Exception as e:
				self.error="Error: %s" % (e)
 
	def DevolverUnaAUnaFilasConsulta():
		try:
			row = self.cursor.fetchone()	
			while row is not None:
				return row
				row = self.cursor.fetchone()
			print("\n\tConsulta exitosa")
		except Exception as e:
			print("Algo ha salido mal")
			return False
			
	def DevolverTodasLasFilasConsulta():
		try:
			for row in self.cursor:
				return row;
			print("\nLa consulta se ha ejecutado satisfactoriamente.");
		except Exception as e:
			print("\nLa consulta no ha podido ser ejecutada: " + str(e));
			return False
	def InsertarDatosTabla(sentecia):
		valorRetorno=False
		try:
			self.cursor.execute(sentecia)
			self.db.commit()
			valorRetorno = True
		except Exception as e:
			self.error="Error: %s" % (e)
			return valorRetorno

	def BorrarTabla(nombreTablaEliminar):
		valorRetorno=False
		try:
			#nombreTablaEliminar=input("Escriba el nombre de la tabla que quiere eliminar")
			self.cursor.execute("DROP TABLE IF EXISTS " + nombreTablaEliminar)
			valorRetorno = True
		except Error as err:
			print("La tabla " + nombreTablaEliminar + " no ha sido encontrada, por lo tanto no se puede eliminar")
			return valorRetorno
			
	def CrearTabla(miSentencia):
		valorRetorno=False
		#miSentencia = "CREATE TABLE Productos(NombreProducto VARCHAR(20), Id INT(10), Precio INT(10), DescripcionProducto VARCHAR(20))";
		try:
			self.cursor.execute(miSentencia);
			self.db.commit()
			valorRetorno = True
			print("La tabla " + nombreTabla+ " se ha creado correctamente");
		except Exception:
			print("Upss, esto es vergonzoso, algo ha salido mal...");	
			return valorRetorno		
			
##################### FINAL DE LA CLASE #############################################################			

			
 
if __name__=="__main__":
	objeto=ClaseBDD()
	ruta = "C:\\Users\\ASIR\\Desktop\\PracticaFinalOscarFernandezRodriguez\\datosCSVPracticaFinal.csv"
	fichero = open(ruta,'r')
	leer = csv.reader(fichero,delimiter=';')			#Leo el archivo CSV y lo guardo, se que solo hay una línea, no se espeficicaba cuantas habria
	for linea in leer:
		localhost = linea[0]
		nombre=linea[1]
		contra=linea[2]
		nombreBDD=linea[3]
		
	result=objeto.ConectarBaseDatos(localhost,nombre,contra,nombreBDD)
	if result:														#CON ESTO DESCARTAMOS QUE EL OBJETO ESTE MAL CREADO
        # Ejecuto una sentencia de seleción y la visualizo una a una las filas
		objeto.EjecutarConsulta("SELECT id,Texto FROM tabla WHERE id=15")
		print(objeto.DevolverUnaAUnaFilasConsulta())
		# Ejecuto una insercion de seleción y la visualizo todas las filas
		objeto.InsertarDatosTabla("INSERT Productos (NombreProducto, Id, Precio, DescripcionProducto) VALUES ('Ordenador Msi', 19, 1300, 'No se que poner')")
		print(objeto.DevolverTodasLasFilasConsulta())
 
		# Creo una tabla, la borro, cierro la conexion y ya
		objeto.CrearTabla("CREATE TABLE Productos(NombreProducto VARCHAR(20), Id INT(10), Precio INT(10), DescripcionProducto VARCHAR(20))")
		objeto.BorrarTabla('Productos')
		objeto.CerrarConexion()
	else:
		print(objeto.error)