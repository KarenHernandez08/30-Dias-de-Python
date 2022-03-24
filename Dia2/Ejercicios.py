#Usando la función incorporada len() , encuentre la longitud de su nombre

nombre='Karen'
print(len(nombre))


#Compare la longitud de su nombre y su apellido
nombre='Karen'
apellido='Hernandez'
print("Mi nombre tiene: ", len(nombre), "y mi apellido tiene: ", len(apellido))

#Declarar 5 como num_one y 4 como num_two

num_one=5
num_two=4

#Sume num_one y num_two y asigne el valor a un total variable
total=num_one+num_two
print(total)

#Reste num_two de num_one y asigne el valor a una variable diff
total_resta=num_one-num_two
print(total_resta)

#Multiplique num_two y num_one y asigne el valor a un producto variable
total_multi=num_one*num_two
print(total_multi)

#Divide num_one por num_two y asigna el valor a una división variable
total_divi=num_one*num_two
print(total_divi)

#Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
total_modulo=num_one//num_two
print(total_modulo)

#Calcule num_one a la potencia de num_two y asigne el valor a una variable exp
exp=num_one**num_two
print(exp)

#Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division
floor_division=num_one%num_two
print(floor_division)


""" El radio de un círculo es de 30 metros.
Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_circle
Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de circum_of_circle


"""

print("Tenemos un círculo con radio de 30 metros, calcular")
radio=30
area_of_circle= 3.1416* (radio**2)
print("Esta es el área del circulo: ", area_of_circle, "metros")
circum_of_circle=(2*3.1416)*30
print("Esta es la circunferencia del; círculo: ", circum_of_circle, "metros")

#Tome el radio como entrada del usuario y calcule el área.

r= int(input("Colocar el valor del radio: "))
area_of_circle= 3.1416 *(r**2)
print("Esta es el área del circulo: ", str(area_of_circle), "metros")
circum_of_circle=(2*3.1416)*r
print("Esta es la circunferencia del; círculo: ", str(circum_of_circle), "metros")


