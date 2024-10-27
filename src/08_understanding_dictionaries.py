"""

    Diccionarios
    
"""
# How to access to a dictionary element
covenant_elite = {'color': "blue", 'points': 10}
print(covenant_elite)

print(covenant_elite['color'])
print(covenant_elite['points'])


# How to add elements to a dictionary
covenant_elite['x-position'] = 0
covenant_elite['y-position'] = 25
covenant_elite['weapon'] = "sword"
print(covenant_elite)

# Empty Dictionary
covenant_grunt = {}
print(type(covenant_grunt))

covenant_grunt['color'] = 'orange'
covenant_grunt['points'] = 1
print("Covenan Grunt", covenant_grunt)

covenant_grunt['points'] = 5
print("Covenan Grunt", covenant_grunt)

del covenant_grunt['points']
print(covenant_grunt)


covenant_grunt['x-position'] = 5
covenant_grunt['y-position'] = 25
covenant_grunt['speed'] = 'medium'

print(covenant_grunt)

if covenant_grunt['speed'] == 'slow':
    x_increment = 1
elif covenant_grunt['speed'] == 'medium':
    x_increment = 10
else:
    x_increment = 20

covenant_grunt['x-position'] = covenant_grunt['x-position'] + x_increment

print(covenant_grunt)


programming_lenguages = {
    'enoc': 'c+',
    'eliel': 'c++',
    'fatima': 'escalera',
    'alexandra': 'python',
    'karim': 'java',
    'griselda': 'python',
}
print(programming_lenguages['enoc'].title())

for key, value in programming_lenguages.items():
    print(f"{key.title()} le gusta el lenguage:", value)

"""
    Keys
"""
friends = ['enoc', 'eliel']
for name in programming_lenguages.keys():
    if name in friends:
        print(f" {name} Hola es un gusto saber que te gusta: {programming_lenguages[name]}" )

if 'charly' not in programming_lenguages.keys():
    print("A charly no le gusta programar")
    
print(programming_lenguages.keys())

for key in programming_lenguages.keys():
    print(key)

print()

for key in sorted(programming_lenguages.keys()):
    print(key)

print()    

for lenguaje in programming_lenguages.values():
    print(lenguaje)    
print()


"""for lenguaje in set(programming_lenguages.values()):
    print(lenguaje)"""