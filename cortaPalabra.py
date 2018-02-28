
def partirCadena():
	palabra = input("Introduce la palabra a dividir en trozos --> ")
	numero = int(input("Introduce en cuantos cachos --> "))
	tamanioPalabra = len(palabra)
	bloqueAMostrar = " "
	numeroLetrasDividir = tamanioPalabra//numero
	while(tamanioPalabra > numeroLetrasDividir):
		bloqueAMostrar =  palabra.strip()[:numeroLetrasDividir] + " "
		palabra = palabra[numeroLetrasDividir:]
		tamanioPalabra = len(palabra)
		print(bloqueAMostrar)		
		
		
partirCadena()
