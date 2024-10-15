# Let's try to use variables
message = "This is my first program :), I am very happy"
print(message)

message_a_number = 9
print(message_a_number)

print(message, message_a_number)
print(message_a_number, message)
message = "Hola atención"
print(message)

"""
Los nombres de variables deben nombrarse solo con: 
    - Letras, números y guión bajo
    - deben comenzar con una letra, un guión bajo pero
    no con número: message_1 (esto es correcto)
    1_message (esto es incorrecto)
    - no utilizar espacios 
    - no utilizar palabras reservadas para nombrar variables
    - utilizar inglés para nombrar variables
"""

message_1 = "Hola Amigo Python"
print(message_1)
print(mesage_1)


"""
NameError: Que olvidamos establecer el valor de una variable antes de utilizarla
o cometimos un error al ingresar el nombre de la variable.
"""


"""
    Ejercicio.
        1. Almacena un mensaje en una variable e imprímelo.
        2. Almacena un mensaje en una variable e imprímelo. 
        Luego cambia el valor de la variable a otro mensaje
        e imprime el nuevo mensaje.
"""

message_exercise_1 = "Hola mundo bonito"
print(message_exercise_1)

message_exercise_2 = "Hola mundo cruel"
print(message_exercise_2)
message_exercise_2 = "Hola de nuevo"
print(message_exercise_2)
