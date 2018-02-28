"""Escribir un programa que pida un numero superior a 300 y haga la criba de Erastóstenes"""

#inicializamos el tamano de la sequencia de numeros
n = 200
#se usa un conjunto porque es mas eficiente
#(no hay numeros repetidos)
noprimos = set()
 
#iteramos desde 2 hasta la raiz cuadrada de n
#y desde lo que lleva i, hasta n / i
#esto nos permite obtener todos los multiplos de i
#y agregarlos a el conjunto noprimos
for i in range(2, int(n ** .5) + 1):
    if i not in noprimos:
        for j in range(i, int(n / i) + 1): noprimos.add(i * j)
        
#por ultimo creamos una lista con todos los numeros
#primos desde 2 hasta n
primos = [p for p in range(2, n + 1) if p not in noprimos]
print(primos)