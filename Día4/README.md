# DÍA 4

## Cadenas

Es una colección de uno o dos más caracteres bajo comillas simples o dobles
```python

cadena="hello world"
print(cadena)

```

La cadena multilínea se crea usando comillas triples simples (''') o triples dobles (""")

```python

cadena_multilinea= ''' Me llamo Karen
tengo 23 años, estudie la carrera de ingenieria 
en informática'''

print(cadena_multilinea)

```
Concatenación

```python

primer_Nombre=Karen
apellido=Hernandez
nombre_completo= primer + apellido

print(nombre_completo)
```

### Secuencias de escape
- \n: nueva línea
- \t: Tabulador significa (8 espacios)
- \\: barra invertida
- \': Una frase (')
- \": comillas dobles (")

ejemplo
```python
print('Karen Jocelyn \n hernandez romero') # line break
print('lenguaje\tHoras\tDías') # adding tab space or 4 spaces 
print('python\t3\t5')
print('java\t3\t5')
print('javascript\t3\t5')
print('Simbolo de la barra invertida (\\)') 
print('\"Hola Mundo!\"') 

#salida
Karen Jocelyn 
 hernandez romero
lenguaje        Horas   Días
python  3       5
java    3       5
javascript      3       5
Simbolo de la barra invertida (\)
"Hola Mundo!"

```

## Operaciones de cadenas 

### Longitud de cadena 

```python 
cadena="Karen"
len("cadena")
```
### Acceder a una posicion de una cadena

para poder acceder a la posicion colocaremos el indice dentro del corchete [i], para poder acceder a un indice de la cadena dinal se coloca "-", [-i]
```python
cadena="karen"
cadena[2] #la salida sera r
cadena[-1]#la salida sera n

```
### Invertir una cadena 

```python
cadena="karen"
print(cadena[::-1]) #salida nerak

```

### Métodos de cadena

- capitalize(): convierte el primer carácter de la cadena en letras mayúsculas
```python
cadena="karen"
print(cadena.capitalize()) #salida Karen

```
- count(): cuenta cuantas veces aparece ese carácter
```python
cadena="karen"
print(cadena.count('a')) #salida 1

```
- expandtabs(): reemplaza el carácter de tabulación con espacios
- find(): Devuelve el índice de la primera aparición del caracter a buscar, si no se encuentra devuelve un -1
- rfind(): Devuelve el índice de la última aparición de una subcadena, si no se encuentra devuelve -1
- format(): Formatea la cadena en una salida más agradable








