"""Hacer un programa que simule el juego del ahorcado (para dos jugadores) ha de contar el numero de fallos y como mucho son 11 fallos """

#Esto me sirve para poner tantos guiones como tamaño tenga la palabra pasada, en lugar de "-" puede ser cualquier caracter
def repite(tamanioCadena,caracter='-', repite=3):
	if (tamanioCadena > 0) :
		for i in range (1, 35):
			print()		
		print("\t Empieza el juego, el tamaño de la palabra que buscamos es " + str(repite) +"\n") 
		print("\t\t\t\t" + caracter * repite)
		print("\n\n\n\n")
	else:
		print("\t Lo sentimos, esa cadena no es válida")
	
def comprobarLetra(cadena="",letraEncontrada="a",cadenaDescifrada=""):
	miCadena=[]
	cadenaJuntadaALaAnterior=[]
	letrasProbadas=[]
	letrasProbadas.append(letraEncontrada)
	if len(letraEncontrada) == 1:
		for i in range (0,len(cadena)):
			if(cadena[i] == (letraEncontrada)):
				cadenaInvertida =cadenaInvertida.replace(cadena[i],letraEncontrada,1)
				#print("     " + cadenaInvertida+ "   -> "+cadenaInvertida[i] + " SOY EL IF  " + str(i))
				miCadena.append(cadenaInvertida[i])
			else:
				#restar lo que llevo
				cadenaInvertida = cadena.replace(cadena[i],"-")
				#print("     " + cadenaInvertida+ "   -> "+cadenaInvertida[i] + " SOY EL ELSE  " +str(i))
				miCadena.append(cadenaInvertida[i])	
	if len(letraEncontrada) > 1:
		if cadena == letraEncontrada:
			print("HAS GANADO")
		else:
			print("pues va a ser que no....")

	cadenaInvertida = "".join(miCadena)
	if cadenaDescifrada != "":
		#Ya tengo la cadena que buscaba, ahora tengo que juntarlo con la cadena anterior
		#Usando split separo la cadena anterior, no la que he sacado ahora, y busco las posiciones
		#donde tengo letras
		descompongoCadenaAnterior = cadenaDescifrada
		for i in range(len(cadena)):
			if(descompongoCadenaAnterior[i] == cadenaInvertida[i] ):			#Quiere decir que los dos tienen "-" o ya tenia descifrado esa letra
				cadenaJuntadaALaAnterior.append(descompongoCadenaAnterior[i])	#Meto la letra o el simbolo "-"
			elif (descompongoCadenaAnterior[i] != "-"):							#La primera cadena que tenia, si esa posicion no es "-" es una letra que no tenia en mi nueva cadena
				cadenaJuntadaALaAnterior.append(descompongoCadenaAnterior[i])
			elif (cadenaInvertida[i] != "-"):									#Quiere decir que de mi ultima cadena sacada no es "-" es un valor ya descifrado
				cadenaJuntadaALaAnterior.append(cadenaInvertida[i])

			#return(cadenaJuntadaALaAnterior,letrasProbadas)

		cadenaInvertida = "".join(cadenaJuntadaALaAnterior)
	return(cadenaInvertida,letrasProbadas)



def jugarAhorcado():
	jugador1 = input("Nombre Jugador 1 --> ")
	jugador2 = input("Nombre Jugador 2 --> ")
	palabra = input("Introduce la palabra para jugar --> ")
	palabra = palabra.strip()		#Quito los espacios en blanco
	palabra = palabra.lower()
	palabraBuscada = palabra
	
	tamanioPalabra = len(palabra)	#Guardo tamaño palabra
	numeroFallos1 = 10
	numeroFallos2 = 10
	contadorVueltas = 0
	letrasProbadas=[]
	palabraMostrar = ""
	#ESTO ES POR SI NO PONE NOMBRE A LOS JUGADORES, PARA QUE NO SALGAN VACIOS Y NO SEA UN LIO EL JUEGO
	if(len(jugador1) == 0):
		jugador1 = "Jugador 1"
	if(len(jugador2) == 0):
		jugador2 = "Jugador 2"
	
	personaQueLeTocaJugar = jugador1
	
	#Imprimo tantos guiones como caracteres tiene la palabra introducida
	repite(tamanioCadena = tamanioPalabra ,repite = len(palabra))
	
	if (tamanioPalabra > 0) :
		while numeroFallos1 >= 0 and numeroFallos2 >=0 :
			letraComprobar = input("\n\t\tIntroduce una letra para comprobar " + personaQueLeTocaJugar+"-> ")
			#palabra.find(letraComprobar)
			if palabraBuscada.find(letraComprobar) != -1 and palabraBuscada.find(letraComprobar) != 0  :	#Compruebo que la letra a comprobar pasada este en la palabra, y cuido que no metan intro
				if (contadorVueltas % 2 == 0 ): #Quiere decir que estoy en los pares, vamos el jugador 1
					print("\n\t\t Letra encontrada, muy bien jugador " + jugador1)
					if(palabra == palabraBuscada):											#Quiere decir que es la primera vuelta, que aun no se ha cambiado la palabra por "---"
						palabra = comprobarLetra(cadena=palabraBuscada,letraEncontrada=letraComprobar)[0]	#Guardo la cadena que obtendo del metodo
						print("\n\t\t\t\t" + palabra)
						letrasProbadas += comprobarLetra(cadena=palabraBuscada,letraEncontrada=letraComprobar)[1]
						print("Letras probadas: " + str(letrasProbadas))
					else:
						palabra = comprobarLetra(palabraBuscada,letraComprobar,palabra)[0]
						print("\n\t\t\t\t" + palabra)
						letrasProbadas += comprobarLetra(palabraBuscada,letraComprobar)[1]
						print("Letras probadas: " + str(letrasProbadas))
					print("####################################################################################")
					personaQueLeTocaJugar = jugador2
					#print(palabra[palabra.find(letraComprobar)])
				else:
					print("\n\t\t Letra encontrada, muy bien jugador " + jugador2)
					if(palabra == palabraBuscada):
						palabra = comprobarLetra(cadena=palabraBuscada,letraEncontrada=letraComprobar)[0]
						print("\n\t\t\t\t" + palabra)
						letrasProbadas += comprobarLetra(cadena=palabraBuscada,letraEncontrada=letraComprobar)[1]
						print("Letras probadas: " + str(letrasProbadas))
					else:
						palabra = comprobarLetra(palabraBuscada,letraComprobar,palabra)[0]
						print("\n\t\t\t\t" + palabra)
						letrasProbadas += comprobarLetra(palabraBuscada,letraComprobar)[1]
						print("Letras probadas: " + str(letrasProbadas))
					print("####################################################################################")
					personaQueLeTocaJugar = jugador1
					#print(palabra[palabra.find(letraComprobar)])
					
			elif (contadorVueltas % 2 == 0): #Quiere decir que estoy en los pares, vamos el jugador 1
				print("\n\t\t Letra no encontrada, tienes " + str(numeroFallos1) + " intentos, " +  jugador1)
				print("\n\t\t\t\t" + palabra)
				letrasProbadas.append(letraComprobar)	#añado la letra que no se ha encontrado para dar pistas
				print("Letras probadas: " + str(letrasProbadas))
				print("####################################################################################")
				
				numeroFallos1 = numeroFallos1 - 1
				personaQueLeTocaJugar = jugador2
			else:
				print("\n\t\t Letra no encontrada, tienes " + str(numeroFallos2) + " intentos, " + jugador2)
				print("\n\t\t\t\t" + palabra)
				letrasProbadas.append(letraComprobar)	#añado la letra que no se ha encontrado para dar pistas
				print("Letras probadas: " + str(letrasProbadas))
				print("####################################################################################")
				numeroFallos2 = numeroFallos2 - 1
				personaQueLeTocaJugar = jugador1
			contadorVueltas = contadorVueltas + 1
		
		if numeroFallos1 == 0:
			print("\n\t LO SENTIMOS, " + jugador1 + " has perdido, la palabra buscada era " + palabraBuscada)
		if numeroFallos2 == 0:
			print("\n\t LO SENTIMOS, " + jugador2 + " has perdido, la palabra buscada era " + palabraBuscada)
				
		
jugarAhorcado()
