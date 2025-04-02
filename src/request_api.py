"""
    Request an api ->  pip install requests
    Petición a una API
"""
import requests

api_url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=151"

response = requests.get(api_url)
response_dict = response.json()
print(response_dict)
"""pokemons = response_dict['results']
for pokemon in pokemons:
    print(f"\t {pokemon['name']} \n ")
    print(f"\t\t Disponible en: {pokemon['url']} \n ")"""