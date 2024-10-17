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


