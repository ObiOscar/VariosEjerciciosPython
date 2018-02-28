"""Escribe un programa que pida numeros (acabada con un intro) luego calcula la media aritmetica, da el valor maximo y el minimo"""

listaNumeros = []
mediaAritmetica = 0
valorMaximo = 0
valorMinimo = 0
sumatorioLista = 0
salirPrograma = True
print("introduce un numero para añadirlo a la lista, te dare la media aritmetica el valor máximo y el minimo, escribe intro para salir ")
while salirPrograma == True:
	numero = input("Añade un numero : ")
	if(numero!=""):
		listaNumeros.append(int(numero));
		#sumatorioLista += int(numero)
		#mediaAritmetica = sumatorioLista / len(listaNumeros)

	else:
		valorMaximo = max(listaNumeros)
		valorMinimo = min(listaNumeros)
		print(listaNumeros.sort());	
		print("El maximo es" + int(valorMaximo));
		print("El minimo es" + valorMinimo);
		print("La media de la lista es " + mediaAritmetica)
		salirPrograma=False;
	
	