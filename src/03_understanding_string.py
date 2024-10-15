"""
    STRINGS
    
    Un string es de manera sencilla una serie de caracteres.
    En Python todo lo que se encuentre dentro de comillas simples
    '' o de dobles comillas "" es considerado un string. 
    
    Ejemplos:
        "Esto es un string"
        'Esto también es un string'
        'Le dije a un amigo, "Python" es mi lenguage favorito'
        "El lenguaje 'Python' lleva el nombre por Monty Python y no por la serpiente"
"""
name = "clase de proGRamación"
print(name)

print(name.title())

"""
    Un método es una acción que python
    puede realizar en un fragmento de datos
    o sobre una variable. 
    El punto . después de la variable
    seguida del método title() dice
    que se tiene que ejecutar el 
    método title de la variable name.

    Todos lo métodos van seguidos de
    paréntesis porque en ocasiones 
    necesitan información adicional
    para funcionar, lo cual iriía
    dentro del paréntesis. En esta ocasión
    el método .title() no requiere información
    extra para ejecutarse.

"""
print("----------------------------------") 
print("Clase 104 o 75011")
"""
    Concatenación de Caracteres
"""
first_name = "charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name)
print(first_name + " " + last_name)
print(full_name)
print("Hola, "+full_name.title()+"!")

"""
    Whitespaces - Se refiere a cualquier caracter que no se imprime,
    es decir, un espacio, un tabulador y finales de línea. Los whitespaces
    se utilizan comúnmente para organizar las salidas, de tal manera que
    sea más amigable de leer o ver para los usuarios.
"""
print("\t\t\tPython")
print("Lenguajes: \nPython\nC\nJavascript")
"""
    ELIMINACIÓN DE ESPACIOS EN BLANCO
"""
print("********************************************")
print("Clase IM75004 - 09/10/2024")
programming_language = " Pyth on "
print(programming_language)
print(programming_language.lstrip())
print(programming_language.rstrip())
print(programming_language.strip())

message = "Una fortaleza de Python es su Comunidad y sus alumnos de la upv"
message = 'Una fortaleza de "PYTHON" su facilidad de enteder'
print(message)

"""
    Ejercio:
    
    1. Guarda el nombre de una persona en una variable e imprime 
    un mensaje de bienvenida a esa persona, ejemplo de la salida :
    " Hola Charly, ¿te gustaría aprender algo más sobre python?"
"""
persona_name = "Charly Mercury"
message = " ¿te gustaría aprender algo más sobre python?"
print(" Hola " + persona_name + message)
""" 
    2. Guarda el nombre de una persona en una variable e imprime
    su nombre en minúsculas, mayúsculas y utilizando el método title.
""" 
print(persona_name.lower())
print(persona_name.upper())
print(persona_name.title())
""" 
    3. Encuentra una cita de alguna persona famosa. Imprime la cita
    y el nombre del autor. Por ejemplo:
    "Charly Mercury una vez dijo, 'Python is love'"
""" 
message_quote = "Charly Mercury una vez dijo, 'Python is love'"
print(message_quote)
"""     
    4. Repite el ejercicio anterior, pero ahora almacena el nombre
    de la persona famosa en una variable famous_person. Ahora
    crea la variable para la cita e imprime el mensaje.
""" 
famous_person = "Charly Mercury"
quote = "'Python is love'"
print(famous_person+" una vez dijo, "+quote)
print("**************************")
message = f"{famous_person} una vez dijo {quote}"
print(message)
""" 
    5. Guarda el nombre de una persona en una variable,
    agrega espacios, 
    tabuladores, saltos de línea. Imprime el nombre, 
    después 
    el nombre varias veces utilizando los métodos 
    rstrip, lstrip, strip.
"""