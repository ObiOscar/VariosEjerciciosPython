    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
    # En este bucle, empezamos por el dos hasta un numero anterior a el, por lo
    # que si en el bucle, alguna vez se divide el numero, quiere decir que no es
    # primo
numeroFactorial = int(input("Introduce un numero para descomponerlo factorialmente --> "))
numeroOperar = numeroFactorial
contador = 0;
contador2 = 0
listaFactoriales = []
restoFactoriales = []
divisiblePorSiMismo = True
resultadoProvisional = 0
while divisiblePorSiMismo == True:
	for x in [2,3,5,7,11]:
		if numeroOperar%x == 0:
			numeroOperar = numeroOperar / x
			listaFactoriales.append(x)	
			divisiblePorSiMismo = True
			print("empieza if" + str(x))			
			break
		elif numeroOperar%numeroOperar == 0 and divisiblePorSiMismo==True: 
			print("empieza elseif" + str(numeroOperar))
			divisiblePorSiMismo = False
			restoFactoriales.append(numeroOperar)
			continue
		else:
			print ("FIN")				
        
while contador < len(listaFactoriales):
	print ("Bucle grande")
	print(str(listaFactoriales[contador]))
	contador += 1

contador = 0
	
while   contador < len(restoFactoriales):
	print("Bucle pequeño")
	print(str(restoFactoriales[contador]))
	contador += 1