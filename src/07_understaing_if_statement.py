
cars = ['bocho', 'mustang', 'sentra', 'honda', 'gtr', 'mustang']

for car in cars:
    if car == 'mustang':
        pass
        # print(car.upper())
    else:
        pass
        # print(car.title())


"""
    Condicionales - Los condicionales
    son el corazón de un if
"""

# Condicional que tiene como resultado True
car = 'bmw'
print(car == 'bmw')

# Condicional que tiene como resultado False
car = 'Audi'
print(car=='audi')

# Condicional que tiene como resultado True
car = 'Audi'
print(car.lower()=='audi')

# Condicional != para determinar desigualdad
tacos = 'bistek'
print(tacos!='pastor')


## 
age = 18
print(age==18)

answer = 17
print(answer!=42)


age = 21
print(age<21)
print(age<=21)
print(age>21)
print(age>=21)

"""
    Multiple Conditions
"""
age_0 = 22
age_1 = 18
print(age_0>=21 or age_1>=21) # -> arroja True
print(age_0>=21 and age_1>=21) # -> arroja False

print("Don Charly")
####
## if -elif - else
"""
    Costo para una persona: 
        <= 4 años -> entrada gratis
        <= 18 -> paga $200
        mayor de 18 -> $500
"""
age = 3
if age <= 4:
    price = 0
elif age<=18:
    price = 200
elif age <65:
    price = 500
elif age >= 65: 
    price = 100

print(f" Tu entrada cuesta ${price} ")

### If statement 

guisos = ['deshebrada', 'salsa verde']
if 'deshebrada' in guisos:
    print("Hay deshebrada")
if 'salsa verde' in guisos:
    print("Hay salsa verde")
if 'picadillo' in guisos:
    print("Hay picadillo")
print("Éstos son los guisos")

## Differences between elif and if

guisos = ['salsa verde', 'deshebrada']
if 'picadillo' in guisos:
    print("Hay Salsa verde")
elif 'picadillo' in guisos:
    print("Hay deshebrada")
elif 'chicharron' in guisos:
    print("Hay chicharron")  
else:
    print("No hay ningún guiso")  
    

# Empty List
guisos = []
if guisos:
    print("Hay elementos")
else:
    print("No hay elementos")
    

# 
guisos_disponibles = ['salsa verde', 'deshebrada', 
                      'picadillo', 'huevo con chorizo']
guisos_a_ordenar = ['chicharron', 'deshebrada', 'huevo con chorizo']
print("¿Qué guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print(f"Si tengo ese guiso: {guiso}")
    else:
        print(f"No tengo ese guiso: {guiso}")
