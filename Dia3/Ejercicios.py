# solicite al usuario que ingrese la base y la altura del triángulo y calcule el área de este triángulo 

base= int(input("Ingrese la base del triángulo: "))
altura= int(input("Ingrese la altura del triáangulo: "))

area= (base*altura)/2

print("El área del triangulo es: ", str(area))

# solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo
a= int(input("Ingrese el primer lado del triángulo: "))
b=int(input("Ingrese el segundo lado del triángulo: "))
c= int(input("Ingrese el tercer lado del triángulo: "))

perimetro=a+b+c

print("el perímetro del triángulo es: ", str(perimetro))

# Obtenga la longitud y el ancho de un rectángulo usando el indicador. 
# área


largo= int(input("Ingrese el largo del rectángulo: "))
ancho= int(input("Ingrese el ancho del rectáangulo: "))

area= (largo*ancho)

print("El área del rectángulo es: ", str(area))

#perímetro

largo= int(input("Ingrese el largo del rectángulo: "))
ancho= int(input("Ingrese el ancho del rectáangulo: "))

perimetro= 2*(largo+ancho)

print("El área del rectángulo es: ", str(perimetro))

# Obtenga el radio de un círculo usando el indicador. 
# #Calcula el área (área = pi xrxr) y la circunferencia (c = 2 x pi xr) donde pi = 3,14.

radio= int(input("Ingresa el radio del círculo: "))
pi=3.14
area= pi*radio*radio
c= 2*pi*radio
print("El área del círculo es: ", str(area))
print("La circunferencia es: ", str(c))


# La pendiente es (m = y2-y1/x2-x1). Encuentre la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6,10)

y2=10
y1=2
x2=6
x1=2

m=(y2-y1)/(x2-x1)

print("La pendiente entre el punto (2,2) y el punto (6,10) es: ", str(m))
from math import dist
a=(2,2)
b=(6,10)
print(" La distancia euclidiana entre (2,2) y (6,10) es:  ",dist(a,b))
