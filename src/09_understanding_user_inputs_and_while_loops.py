"""

    User Inputs

    El método built-in input permite obtener información
    del usuario.
    
    input(prompt) -> string

"""
"""
message = input("Escribe algo, y lo reimprimiré de nuevo para ti: ")
print(message)
print(type(message))
"""
# Prompt para pedir un string
"""prompt = " Introduce tu nombre: " 
message = input(prompt)
print(message)
"""
# Prompt para pedir un número
"""prompt = "¿Cuál es tu edad?: "
age = int(input(prompt))
print(age)
print(type(age))
print(age>=18)
"""

"""

    Operador Módulo
    
"""
"""print(4%3)
print(5%3)
print(6%3)
par_impar = "Introduce un número para decirte si es par o impar: "
number = int(input(par_impar))
if number%2==0:
    print(number, "es par.")
else:
    print(number, "es impar.")"""

"""

    While Loop
    
"""
import time

contador = 0

while contador < 5:
    print("Charly")
    time.sleep(0.1)
    contador += 1

message = ""
while message != 'salir':
    message = input("Si quiere salir, tipea salir: ")
    print(message)
   
    
while True: 
    print("Alan")
    print("Chema")
    prompt = "¿Quieres imprimir otro nombre?, escríbelo." +\
        "si quieres salir , tipea quit: "
    message = input(prompt)
    if message == 'quit' or message == 'exit' or message == 'salir':
        break
    print(message)