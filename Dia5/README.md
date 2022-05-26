## Día 5

# LISTAS 
Las listas son una colección de diferentes tipos de datos ordenados y modificables, una lista puede estar vacía o puede tener elementos de diferentes tipos de datos.

La manera de crear una lista es la siguiente

```python
nombrelista=[] #esta es una lista vacia
nombrelista=['cadena', 4, 5.456, True]# cadena con valores
```
`len()` lo usamos para saber la longitud de nuestra cadena

```python
nombrelista=['cadena', 4, 5.456, True]
print(len(nombrelista)) #salida 4
```

## Acceder a los elementos de la listas

Se acceden a los elementos de la lista a traves de su indice, recordando que las listas inician en 0 el primer elememto
### indexación positiva

```python
nombrelista=['cadena', 4, 5.456, True]
print(nombrelista[0]) #cadena
print(nombrelista[1]) #4
print(nombrelista[2]) #5.456
print(nombrelista[3]) #True

```

### indexación negativa

```python
nombrelista=['cadena', 4, 5.456, True]
print(nombrelista[-1]) #True
print(nombrelista[-2]) #5.546
print(nombrelista[-3]) #4
print(nombrelista[-4]) #cadena

```