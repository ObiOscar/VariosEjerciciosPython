factorial = int(input("Introduce numero que quieras factorizar --> "))
valorAMostrar = 0
valorFactorial = 0

if factorial != 0 and factorial > 1:
	for i in range (1,factorial):
		if(factorial>1):
			valor = valorFactorial
			valorFactorial = factorial * factorial - 1
			
			factorial = factorial -1
			valorAMostrar = valor * factorial
		
		
print(str(valorAMostrar))	