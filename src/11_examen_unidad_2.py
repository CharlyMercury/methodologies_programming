"""

    Problema 1. Tipo entrevista

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



"""

   Problema 2. Sistema de gestión de productos de una tienda

    Eres el encargado de crear un sistema básico para administrar 
    productos de una tienda. Este sistema debe permitir:

        - Registrar productos con su nombre y precio.
        - Consultar productos con precios específicos.
        - Actualizar los precios de productos existentes.
        - Obtener un resumen de todos los productos con ciertos filtros.

        Requerimientos
        
        Registro de productos:
            - Crea una lista vacía llamada productos.
            - Cada producto debe ser un diccionario con las claves: 
                "nombre" (cadena de texto) y "precio" (flotante).
            - Usa un bucle while para permitir al usuario agregar productos 
                hasta que decida detenerse.
        
        Consulta de productos por precio:
            - Pide al usuario que ingrese un precio límite.
            - Usa una list comprehension para generar una lista de productos 
                cuyo precio sea menor o igual al precio límite dado.
            - Muestra la lista resultante o indica que no hay productos en ese
                rango de precio.

        Actualización de precios:

            - Solicita al usuario el nombre del producto que quiere
                actualizar.
            - Si el producto existe, pide el nuevo precio y actualiza
                su valor.
            - Usa una estructura if para verificar si el producto 
                existe; si no, muestra un mensaje indicando que no se encontró.

        Resumen de productos:

            - Utiliza un bucle for para mostrar un resumen de todos los 
                productos registrados en un formato claro.
            - Si el usuario quiere filtrar los productos con precio mayor
                a un valor dado, filtra la lista y muestra solo los productos
                que cumplan con el criterio. 

"""