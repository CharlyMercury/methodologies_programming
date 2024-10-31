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
    'frida': 'c++',
    'rita': 'python',
    'pedro': 'javascrip',
    'gael': 'python',
    'berenice': 'c',
    'cesar': 'javascrip',
}
print(programming_lenguages['frida'].title())


"""

    Ejercicios.

        1. Persona: Usa un diccionario para almacenar información sobre una 
            persona que conoces. Guarda su nombre, apellido, edad y la ciudad
            en la que vive. Deberías tener claves como nombre, apellido, edad y 
            ciudad. Imprime cada pieza de información almacenada en tu 
            diccionario.

        2. Números Favoritos: Usa un diccionario para almacenar los números 
            favoritos de varias personas. Piensa en cinco nombres y úsalos como
            claves en tu diccionario. Piensa en un número favorito para cada 
            persona y guárdalo como valor en tu diccionario. Imprime el nombre de
            cada persona y su número favorito. Para hacerlo más divertido, 
            encuesta a algunos amigos y obtén datos reales para tu programa.

        3. Glosario: Un diccionario de Python puede usarse para modelar un 
        diccionario real. Sin embargo, para evitar confusiones, llamémoslo 
        glosario.

            - Piensa en cinco palabras de programación que hayas aprendido en los 
            capítulos anteriores. Usa estas palabras como claves en tu glosario y
            guarda sus significados como valores.

            - Imprime cada palabra y su significado en una salida bien formateada. 
            Podrías imprimir la palabra seguida de dos puntos y luego su 
            significado, o imprimir la palabra en una línea y su significado 
            indentado en una segunda línea. Usa el carácter de nueva línea (\n) 
            para insertar una línea en blanco entre cada par palabra-significado
            en tu salida.

"""

for key, value in programming_lenguages.items():
    print(f"{key.title()} le gusta el lenguage:", value)

"""
    Keys
"""
friends = ['frida', 'pedro']
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
print()    
print()    
print("\n\n Clase de Conjuntos \n\n")
print(programming_lenguages)
print(" TOdos los valores ")    
for lenguaje in programming_lenguages.values():
    print(lenguaje)    
print()

print(" Set ")    
for lenguaje in set(programming_lenguages.values()):
    print(lenguaje)
    

"""
    Ejercicios:
    
        1. Glosario 2: Ahora que sabes cómo recorrer un diccionario con un 
            bucle, modifica el código del ejercicio anterior reemplazando tu 
            serie de instrucciones print con un bucle que recorra las claves y
            valores del diccionario. Cuando estés seguro de que tu bucle 
            funciona, agrega cinco términos más de Python a tu glosario. Al 
            ejecutar el programa nuevamente, estas nuevas palabras y sus 
            significados deberían incluirse automáticamente en la salida.

        2. Ríos: Crea un diccionario que contenga tres ríos importantes y el 
        país por el que cada río fluye. Un par clave-valor podría ser 
        'nilo': 'egipto'.

            - Usa un bucle para imprimir una oración sobre cada río, como: El Nilo fluye por Egipto.
            - Usa un bucle para imprimir el nombre de cada río incluido en el diccionario.
            - Usa un bucle para imprimir el nombre de cada país incluido en el diccionario.

"""
"""
    Nesting - Dictionaries in Lists
"""
covenant_elite = {'color': 'blue', 'puntos': 10}
covenant_jackal = {'color': 'gray', 'puntos': 8}
covenant_grunt = {'color': 'orange', 'puntos': 5}

covenants = [covenant_elite, covenant_jackal, covenant_grunt]

print("Covenants")
print(covenants)

for covenant in covenants:
    print(covenant)
    
# Vamos a crear una flotilla de 30 covenants gruts
covenant_fleet = []
for _ in range(30):
    new_covenant ={'color': 'orange', 'puntos': 5}
    covenant_fleet.append(new_covenant)
    
print(covenant_fleet)
print(len(covenant_fleet))

"""
    Listas en Diccionarios
"""
# Menú
tacos = {
    "tortillas": ['harina', 'maiz'],
    "guisos": ['bistek', 'tripa', 'pastor'],
}

print("Tu has ordenado unos tacos " + 
      f"de {tacos['guisos'][0]} en tortilla de {tacos['tortillas'][0]}")

## Imprimir los lenguales de cada persona
favorite_games = {
    "charly": ['fornite', 'halo', 'gearsofwar'],
    "alan": ['apex', 'warzone', 'counterstrike'],
    "valente": ['minecraft', 'rocketleague', 'blasphemous'],
    'doria': ["valorant", 'blackops'],
}

for name, games in favorite_games.items():
    print(name)
    for game in games:
        print("\t"+game.title())
        
        
"""
    Dictionaries in dictionaries
"""
# Caso de uso Usernames en una aplicación web
users = {
    "charlymercury": {
        "firstname": "Carlos",
        "lastname": "Tovar",
        "age": 32,
        "height": 175,
    }, 
    "sujefa": {
        "firstname": "Leo",
        "lastname": "Castillo",
        "age": 18,
        "height": 165,
    }, 
    "boliche717171": {
        "firstname": "Eduardo",
        "lastname": "Zayas",
        "age": 18,
        "height": 182,
    }, 
}

for user, user_info in users.items():
    print(user)
    full_name = user_info['firstname'] + " " + user_info['lastname']
    print("\t ",full_name, "tiene: ", f"{user_info['age']} años.", " Y mide: " + str(user_info['height']))
    
"""
    Request an api
    Petición a una API
"""
import requests
import json

api_url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(api_url)
response_dict = response.json()
pokemons_en_lista = response_dict['results']
for pokemon in pokemons_en_lista:
    print(pokemon)