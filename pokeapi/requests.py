import requests

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