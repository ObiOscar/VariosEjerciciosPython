
contadorIntentos = 0
maximoIntentos = 10


while maximoIntentos -1 > contadorIntentos  :
	contrasenia = input("Introduce la contraseña --> ")
	if contrasenia == ("contraseña"):
		print("estas viendo los archivos secretos")
		break
	else:
		print("Contraseña incorrecta")
		print("Te quedan " + str((maximoIntentos -1)-contadorIntentos) + " intentos, el máximo de intentos será " + str(maximoIntentos))
		contadorIntentos = contadorIntentos + 1
		