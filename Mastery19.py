print("Vamos a escribir una serie de numeros")
x=int(input("Tu elijes desde que numero: "))
y=int(input("Hasta que numero: "))
z=""
while (x!=y+1):
	z=(z+" "+str(x)+",")
	x=x+1
print(z[:-1])
