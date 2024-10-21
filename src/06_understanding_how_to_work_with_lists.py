magicians = ["severus", 'voldemort', "harry potter", "hermione"]
print(magicians)
for mago in magicians:
    print(mago)
    print(mago.upper()+" ese fue un gran hechizo.")
    print(f"No puedo esperar a ver tu próximo hechizo, {mago.title()}\n")
print("Gracias a todos lo magos, fue un gran espectáculo")

"""

    Ejercicios.

    1. Piensa en al menos tres tipos de pizzas que te gusten mucho. 
    Guarda los nombres de estas pizzas en una lista y luego utiliza 
    un ciclo for para imprimir el nombre de cada pizza.

        a) Modifica el ciclo for para que imprima una oración completa, 
        en lugar de solo el nombre de la pizza. Por ejemplo, en lugar de 
        solo imprimir "pepperoni", el programa debe mostrar: 
        "Me gusta la pizza de pepperoni".

        b) Al final del programa, fuera del ciclo for, agrega una línea 
        que diga cuánto te gusta la pizza en general. Por ejemplo, después 
        de las oraciones de las pizzas específicas, podrías agregar algo 
        como: "¡Realmente me encanta la pizza!".
    
    2. Piensa en al menos 3 animales diferentes que tengan características
    similares. Almacenalos en una lista e imprime el nombres de cada animal
    utilizando un for. 
    
        a) Imprime un mismo mensaje para cada animal, por ejemplo: " un perro
        sería una gran mascota. "
        
        b) Agrega un elemento al final de tu programa e imprímelo, por ejemplo: 
        " Todos éstos animales serían una gran mascota" 

"""

"""
    La listas también pueden almacenar números y son ideales para almacenarlos.
    Python ofrece cantidades de herramientas que ayudan a trabajar eficientemente con
    listas de números.

"""

# Método built-in Range()
# El método range nos ayuda a crear fácilmente series de números
# Ejemplo:
for value in range(1, 5):
    print(value)

# Crear una lista de números utilizando range
numbers = list(range(-1, 11))
# Invertir una lista    
numbers.reverse()
print(numbers)

# Números pares
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Invertir una lista 
numbers = list(range(10, -2, -1))
print(numbers)

"""
    Podemos crear cualquier lista de números 
    utilizando range(). 
    
    Vamor a crear una lista que contenga todos
    los cuadrados de los numéros comprendidos
    entre el 1 y el 10, es decir, la lista debe ser:
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
"""
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Imprimir valores en for, comentario del for anidado
cars = ['hot-wheels', 'vocho', 'go-kars']
ice_creams = ['napolitano', 'fresa', 'pistache']
print()
for value in range(0,3): 
    print(cars[value] + "\n" + ice_creams[value] + '\n')    

# Otros métoso built-in
numbers = list(range(0,11))
print(min(numbers))
print(max(numbers))
print(sum(numbers))


"""

    Una list comprehension combina el for loop, la creación
    de nuevos elementos en una sola línea y automáticamente 
    agrega cada nuevo elemento a la lista, es decir, sin
    utilizar el append.

"""
squares_2 = [number**2 for number in range(1,11)]
print(squares_2)

"""

    Ejercicios: 

        1. Utiliza el for loop para imprimir los números del 1 al 20.
        2. Construye una lista de números del 1 al 1000000 y utiliza
            un for para imprimir los números. (En caso de ser necesario 
            utiliza ctrl+c para parar el progra).
        3. Utiliza la lista anterior para saber cual es el mínimo y el 
            máximo de una lista. Suma los números utilizando sum.
        4. Utiliza el tercer argumento de range() para hacer una lista
            que contenga los números pares del 1 al 20. Utiliza un for 
            para imprimir los valores de la lista.
        5. Crea una lista que contenga múltiplos de 3 del 3 al 30. 
            Utiliza un for para imprimir los valores de la lista.
        6. Un número elevado a la tercera potencia es llamado un cubo.
            Por ejemplo, el cubo de 2 se escribe en Python 2**3. Crea
            una lista con los primeros 10 cubos (1^3, 2^3, 3^3, ... , 10^3).
            Utiliza un for para imprimir los valores de la lista.
        7. Utiliza una list comprehension para generar una lista de los primeros
        20 cubos. Utiliza un for para imprimir los valores de la lista.
"""


## SLICING O SLICE
players = ['charly', 'doria', 'jose maria', 'valente', 'puga']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

## Slicing en un for
players = ['charly', 'doria', 'jose maria', 'valente', 'puga']
print("Aquí se presentan los primeros 3 alumnos")
for player in players[0:3]:
    print(player)

## Copia de listas
my_food = ['chilaquiles', 'flatuas de desebrada', 'enfrijoladas']
dorias_favorite_food = my_food[:]
dorias_favorite_food_2 = list(my_food)
dorias_favorite_food_3 = my_food.copy()
my_food.append('sopes')
print(my_food)
print(dorias_favorite_food)

"""
    Ejercicios: 
    
        1. Rebanadas: Usa uno de los programas que escribiste en el ejercicio 
            anterior, agrega varias líneas al final del programa que hagan lo siguiente:
            
            - Imprime el mensaje: Los primeros tres elementos en la lista son: 
                Luego usa una rebanada (slice) para imprimir los primeros tres 
                elementos de la lista de ese programa.
            - Imprime el mensaje: Tres elementos del medio de la lista son: 
                Usa una rebanada para imprimir tres elementos del medio de la lista.
            - Imprime el mensaje: Los últimos tres elementos de la lista son: 
                Usa una rebanada para imprimir los últimos tres elementos de la lista.
        
        2. Mis Pizzas, Tus Pizzas: Comienza con tu programa del Ejercicio de las pizzas. 
        Haz una copia de la lista de pizzas y llámala friend_pizzas. Luego, haz lo siguiente:

            - Agrega una nueva pizza a la lista original.
            - Agrega una pizza diferente a la lista friend_pizzas.
            - Demuestra que tienes dos listas separadas. 
                - Imprime el mensaje: Mis pizzas favoritas son:, y luego usa un bucle 
                    for para imprimir la primera lista. 
                - Imprime el mensaje: Las pizzas favoritas de mi amigo son:, y luego usa 
                    un bucle for para imprimir la segunda lista. Asegúrate de que cada 
                    nueva pizza esté almacenada en la lista correspondiente.

"""


## TUPLAS
# Las tuplas son listas de elemntos que no cambian de tamaños. 
# Las tuplas son listas inmutables
# Se utilizan los () para definir una tupla.
dimensions = (200, 500)

print(dimensions)

print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)
    
dimensions = (250, 500)
print(dimensions)
