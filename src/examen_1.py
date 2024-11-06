"""

    Problema 1. Tipo entrevista laboral (Python Developer Jr)

    Descifra el mensaje oculto.
    
    Se tiene la siguiente lista:
    mensaje = [ "u", "n", "e", "m", "i", " ", "t", "o", " ", "Q", "o", "a", "d", "A", "R"]
        
    Crea un programa que reemplace: 
        - La letra a/A por la e
        - La letra e/E por la i
        - La letra i/I por la o
        - La letra o/O por la u
        - La letra u/U por la a
        - La letra q/Q por la p
        - La letra r/R por la s
        
    Muestra al final el mensaje oculto en consola con la función print.
    ( Imprime el mensaje con un ciclo for para la salida, utiliza el 
    argumento end="" para que no imprima un salto de línea en cada print
        Ejemplo: 
            print(letter, end="") 
    )
        
"""
mensaje = [ "u", "n", "e", "m", "i", " ", "t", "o", " ", "Q", "o", "a", "d", "A", "R"]
mensaje_oculto = []

mensaje.pop(0)
mensaje.insert(0, 'a')


for letra in mensaje:
    if letra.lower() == 'a':
        mensaje_oculto.append('e')
    elif letra.lower() == 'e':
        mensaje_oculto.append('i')
    elif letra.lower() == 'i':
        mensaje_oculto.append('o')
    elif letra.lower() == 'o':
        mensaje_oculto.append('u')
    elif letra.lower() == 'u':
        mensaje_oculto.append('a')
    elif letra.lower() == 'q':
        mensaje_oculto.append('p')
    elif letra.lower() == 'r':
        mensaje_oculto.append('s')
    else:
        mensaje_oculto.append(letra)

for letra in mensaje_oculto:
    print(letra, end="")


# Lista de letras del mensaje
mensaje = ["u", "n", "e", "m", "i", " ", "t", "o", " ", "Q", "o", "a", "d", "A", "R"]

# Diccionario de sustitución de letras
sustituciones = {
    "a": "e", "A": "e",
    "e": "i", "E": "i",
    "i": "o", "I": "o",
    "o": "u", "O": "u",
    "u": "a", "U": "a",
    "q": "p", "Q": "p",
    "r": "s", "R": "s"
}

# Ciclo para imprimir el mensaje descifrado
for letra in mensaje:
    # Reemplaza la letra si está en el diccionario, de lo contrario usa la misma letra
    print(sustituciones.get(letra, letra), end="")
