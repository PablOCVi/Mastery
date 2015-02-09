print("Si el numero ingresado es par y mayor a 10, lo mltiplicare por 4")
x=int(input("Ingresa un numero par: "))
while (x%2!=0)or(x<10):
	if x%2!=0:
		print("El numero"+" "+str(x)+" "+"es par")
	if x<10:
		print("El numero"+" "+str(x)+" "+"es menor a 10")
	x=int(input("Ingresa un numero par mayor a 10: "))
print("El numero "+str(x)+" es par")
print("El numero"+" "+str(x)+" "+"es mayor a 10")
print("Al numero "+str(x)+" Lo multiplicare por 4 "+"= "+str(x*4))
