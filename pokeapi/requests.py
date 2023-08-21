import requests
from tqdm import tqdm
import time

def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def get_pokemon_name(pokemon_id):
    data = get_pokemon_data(pokemon_id)
    if data:
        return data["name"]
    else:
        return None
    
def get_pokemon_type_1(pokemon_id):
    data = get_pokemon_data(pokemon_id)
    if data:
        return data["types"][0]["type"]["name"]
    else:
        return None
    
def get_pokemon_list():
    url = f"https://pokeapi.co/api/v2/pokemon/?limit=1281"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return None
    
def get_pokemon_types(pokemon_id):
    data = get_pokemon_data(pokemon_id)
    types = [entry['type']['name'] for entry in data['types']]
    return types
    
def get_pokemon_list_with_types():
    pokemon_list_with_types = []
    pokemon_list = get_pokemon_list()
    for pokemon in tqdm(pokemon_list, desc='Getting Pokemon Types', unit='pokemon'):
        pokemon_id = pokemon['url'].split('/')[-2]
        types = get_pokemon_types(pokemon_id)
        pokemon_list_with_types.append({'id': pokemon_id, 'name': pokemon['name'], 'types': types})
        time.sleep(0.1)
    return pokemon_list_with_types
