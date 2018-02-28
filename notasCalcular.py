print("Recogeremos las notas: ")
notaMaxima = 0
notaMinima = 10
contadorNotas = 1
while True:
	print("ingrese la nota")
	notaRecogida = input()
	if notaRecogida == "salir":
		break
	if notaRecogida >= 0 and notaRecogida <= 10:
		print("promedio actual: ",notaRecogida/contadorNotas), "\n")
		if notaRecogida > notaMaxima:
			notaMaxima = notaRecogida
	    if notaRecogida < notaMinima:
			notaMinima = notaRecogida
		print("nota Máxima: ",max(valores), "\n")
		print("nota Mínima: ",min(valores), "\n")
		notaRecogida = notaRecogida + notaRecogida
		contadorNotas += 1
	else:
		try:
			print("promedio actual: ",notaRecogida/contadorNotas), "\n")
		except:
			print("primero ingrese un valor positivo")
