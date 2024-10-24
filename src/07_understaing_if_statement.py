
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
age = 40
if age <= 4:
    price = 0
elif age <= 18:
    price = 200
elif age <= 50:
    price = 500
elif age > 50: 
    price = 100
    
print(f"Tu pagas {price} pesos.")


### Multiple conditions
guisos = ['deshebrada', 'salsa verde']
if 'deshebrada' in guisos:
    print('Hay deshebrada')
elif 'salsa verde' in guisos:
    print('Hay salsa verde')
elif 'picadillo' in guisos:
    print('Hay picadillo')
    
print("Éstos guisos hay")
print()

print()


#### Listas Vacías


if guisos:
    print("Tengos guisos") 
else:
    print("No hay guisos")
    
    
####
guisos_availables = ['salsa verde', 'deshebrada', 'picadillo',
                   'huevo chorizo']

guisos_to_order = ['barbacoa', 'deshebrada', 'cabrito', 'picadillo']

print("¿Qué desea ordenar?")

for guiso in guisos_to_order:
    if guiso in guisos_availables:
        print(f"Si tenemos {guiso}")
    else: 
        print(f"No tenemos {guiso}")

print("Realizar Pedido")

