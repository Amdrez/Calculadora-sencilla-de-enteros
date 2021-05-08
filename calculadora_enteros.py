def run():
	"""Calculadora sencilla de dos numeros enteros."""
	operaciones = []
	respuesta = 's'
	n = 0
	while respuesta == 's':
		n +=1
		menu = """\nElige la operacion que quieres realizar:
		
1. Suma
2. Resta
3. Multiplicacion
4. Division
		
Escribe el numero correspondiente a la operacion que deseas realizar: """

		opcion = int(input(menu))
		a = int(input("Esceibe un numero: "))
		b = int(input("Esceibe un otro: "))
	
		if opcion == 1:
			resultado= str(a + b)
			print("resultado: ", resultado)
			operador = "+"
		if opcion == 2:
			resultado= str(a - b)
			print("resultado: ", resultado)
			operador = "-"
		if opcion == 3:
			resultado= str(a * b)
			print("resultado: ", resultafo)
			operador = "*"
		if opcion == 4:
			resultado= str(a // b)
			print("resultado: ", resultado)
			operador = "/"
		
		datos_operacion = []
		datos_operacion.append("Operacion N° " + str(n))
		datos_operacion.append("1er Numero " + str(a))
		datos_operacion.append("2do Numero " + str(b))
		datos_operacion.append("Operador " + operador)
		datos_operacion.append("Resultado " + resultado)
		operaciones.append(datos_operacion)
		
		respuesta = input("\nDesea realizar otra operacion (s/n): ")
	
	veroperaciones = input("Se han realizado " + str(len(operaciones)) + " operaciones, desea ver los datos de cada una (s/n): ")
	if veroperaciones == "s":
		for i in operaciones:
			print(i)
			
	print("Hasta luego!")		
	
if __name__ == '__main__':
	print("BIENVENIDO A CALCULADORA DE NUMEROS ENTEROS")
	run()