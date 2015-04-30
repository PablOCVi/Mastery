#Pablo Enrique Cárdenas Viera
#3 Superpower
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

x =(int(input("Give me a number:")))

FcTorial = factorial(x)

print ("The factorial number is:", FcTorial)