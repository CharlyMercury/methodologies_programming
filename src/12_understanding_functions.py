

def sumita(*args):
    print(args)
    print(type(args))
    for element in args:
        print(element)
    c = sum(args)
    return c


variable_elementos = (1, 2, 3, 4, 5) 
sumeishon = sumita(*variable_elementos)
print(sumeishon)



def create_fullname(nombre, edad, *args, **kwargs):
    print(nombre)
    print(edad)
    print(args)
    print(kwargs)
    

metadata = {
    "name": "carlos", 
    "middlename": "antonio", 
    "lastname": "tovar"
}

fullname = create_fullname("carlos", 25, "antonio", **metadata)
print(fullname)