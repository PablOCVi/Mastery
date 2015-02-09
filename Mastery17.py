print("Debes ingresar un valor impar, y multiplo de 5")
print("Solo asi pasaras al siguiente nivel")
x=int(input("Ingresa un numero: "))
while (x%2==0)or(x<5):
	if x%2!=0:
		print("El numero"+" "+str(x)+" "+"es impar")
	elif x<5:
		print("El numero"+" "+str(x)+" "+"es menor a 5")
	x=int(input("Recuerda que debes ingresar un valor impar, y multiplo de 5: "))
print("El numero "+str(x)+" es impar")
print("El numero"+" "+str(x)+" "+"es menor a 10")
print("GENIAL!!")
print("Has pasado al segundo nivel")
