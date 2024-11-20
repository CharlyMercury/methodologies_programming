
def create_name(firstname, middlename, lastname):
    """
        Crea nombre completo
        
        recibe tres parámetros strings
        
        regresa el nombre completo
    """
    fullname = firstname + " " + middlename + " " + lastname
    return fullname.title()


def imprimir_nombre(nombre):
    print(nombre)