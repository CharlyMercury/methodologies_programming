"""

    User Inputs

    El método built-in input permite obtener información
    del usuario.
    
    input(prompt) -> string

"""
"""message = input("Escribe algo, y lo reimprimiré de nuevo para ti: ")
print(message)
"""

"""# Prompt para pedir un string
prompt = " Introduce tu nombre: "
message = input(prompt)
print(message)"""

"""# Prompt para pedir un número
prompt = "¿Cuál es tu edad?: "
age = input(prompt)
print(age)
print(type(age))
print(int(age)>=18)"""


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


import time


"""

    While Loop
    
"""

contador = 0

while contador < 5:
    print("Charly")
    contador += 1


message = ""
while message != 'salir':
    message = input("Si quiere salir, tipea salir: ")
    

while True: 
    print("Franco")
    print("Gerry")
    prompt = "¿Quieres imprimir otro nombre?, escríbelo." +\
        "si quieres salir , tipea quit: "
    message = input(prompt)
    if message == 'quit' or message == 'exit' or message == 'salir':
        break
    print(message)