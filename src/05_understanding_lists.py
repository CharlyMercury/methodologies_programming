"""
    
    Las listas nos permiten almacenar información en un lugar, 
    la cantidad que tengas: ya sean pocos elementos o millones
    de elementos.
    
    Una lista es una colección de items (elementos) que tienen
    un orden particular. Se pueden crear listas que incluyan
    strings, números, los nombres de las personas de tu familia, 
    etc. podemos almacenar (los tipos de datos permitidos en 
    Python) lo que queramos en una lista.
    
    Se recomienda nombrar una variable en plural, si la variable 
    es una lista.
    
    En Python, los corchetes [] indican una lista, sus elementos 
    se separan por comas.
    
    Ejemplo de una lista.
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

"""

    Accessando a los elementos de una lista.
    
"""
# Para acceder al primer elemento de una lista
print(bicycles[0])

# Los índices comienzan en 0, no en 1.
print(bicycles[1]) # imprime cannondale
print(bicycles[3]) # imprime specialized

# Accesando al último elemento
print(bicycles[-1]) # specialized

#Accesando al penúltimo
print(bicycles[-2]) # imprime redline

# Utilizando valores individuales de una lista
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# Utilizando f-strings
message_f = f"My first biclycle was a {bicycles[0].title()}"
print(message_f)


"""

    Ejercicios:
    
    1. Almacena los nombres de algunos de tus amigos 
    en una lista llamada names. Imprime el nombre de 
    tus amigos de uno por uno, accediendo a los
    elementos de la lista. 
    
    2. Utilizando la lista anterior. Imprime el nombre
    de la persona agregándole un mensaje. El texto del 
    mensaje debe ser el mismo, pero cada mensaje debe 
    estar personalizado con el nombre de la persona.
    
    3. Crea una lista con tus métodos favoritos de 
    transporte. Utiliza la lista para imprimir una
    serie de mensajes sobre cada elemento de la lista,
    por ejemplo, "Me gustaría tener un auto Tesla".
    
"""

"""
    Agregar elementos a una lista
"""

# Agregando elementos elementos a una lista.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Método append - Agrega elementos al final
# de la lista
motorcycles.append('ducati')
motorcycles.append('bmw')
print(motorcycles)

# Método insert - Agrega elementos en un lugar
# específico
motorcycles.insert(0, 'Italika')
motorcycles.insert(3, 'kawasaki')


"""
    Eliminar elementos a una lista
"""
# Método del - si conocemos el índice del elemento que deseamos eliminar
del motorcycles[0]
print(motorcycles)

# Método pop() -> Elimina el último elemento 
# de la lista, pero nos permite utilizar el 
# elemento después de eliminarlo
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Método pop(índice) -> Se puede utilizar también 
# para eliminar un elemento específico
element_to_delete = motorcycles.pop(0)
print(motorcycles)
print(element_to_delete)

"""
    Si vas a utilizar el elemento que vas a eliminar
    después de eliminarlo, utiliza pop() sino utiliza
    del.
"""

# Método remove() -> Permite eliminar elementos 
# por su valor
motorcycles.remove('suzuki')
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n A {too_expensive.title()} is too expesive for me. ")
print(f"I can buy {motorcycles}")


"""

    Ordernar Listas
    
    El método sort ordena la lista permanentemente
    
"""
cars = ['bmw', 'audi', 'toyotta']
cars.sort()
print(cars)

# ordenar la lista de manera ordenada en reversa
cars.sort(reverse=True)
print(cars)

"""
    Función built-in sorted
    
    Ordena la lista de manera temporal 

"""
cars = ['bmw', 'audi', 'toyotta']
print("Lista Original")
print(cars)
print("Lista Ordenada")
print(sorted(cars))
print("Lista Original")
print(cars)

"""
    Método reverse
    
    El método reverse de las listas
    invierte la lista de manera permanente

"""
cars.reverse()
print(cars)

"""

    Función built-in len

    Longitud de las listas
    
    El método len nos dice la cantidad
    de elementos que hay en una lista
    
"""

print(len(cars))