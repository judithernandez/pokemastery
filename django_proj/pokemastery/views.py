from django.http import HttpResponse
from django.shortcuts import render

import requests


def greetings(request):
    return HttpResponse("Hello, PokéWorld!")

def hello_pokemon(request, pokemon_id):
    # API endpoint URL
    api_url = "https://pokeapi.co/api/v2/pokemon/"
    api_url += str(pokemon_id)
    # Make the GET request
    response = requests.get(api_url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON data
        data = response.json()

        # Extract and use data
        pokemon_name = data["name"].capitalize()
        
    return HttpResponse(f"Hello, pokémon {pokemon_name}!")

def pokepedia(request):
    return render(request, "pokepedia.html")

def index(request, pokemon):
    # API endpoint URL
    api_url = "https://pokeapi.co/api/v2/pokemon/"
    api_url += str(pokemon)
    # Make the GET request
    response = requests.get(api_url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON data
        data = response.json()

        # Extract and use data
        pokemon_id = data["id"]
        pokemon_name = data["name"].capitalize()
        pokemon_height = data["height"]
        pokemon_weight = data["weight"]
        pokemon_abilities = [ability["ability"]["name"].capitalize() for ability in data["abilities"]]
        pokemon_moves = [move["move"]["name"] for move in data["moves"]]
        pokemon_sprite = data["sprites"]["other"]["dream_world"]["front_default"]
        pokemon_stats = [stat["base_stat"] for stat in data["stats"]]
        pokemon_stat_names = [stat["stat"]["name"] for stat in data["stats"]]
        pokemon_types = [type["type"]["name"].capitalize() for type in data["types"]]
        

    # Render the index.html template with the context
    context = {
        'pokemon_id': pokemon_id,
        'pokemon_name': pokemon_name,
        'pokemon_height': float(pokemon_height)/10,
        'pokemon_weight': float(pokemon_weight)/10,
        'pokemon_abilities': pokemon_abilities,
        'pokemon_moves': pokemon_moves,
        'pokemon_sprite': pokemon_sprite,
        'pokemon_stat_names': pokemon_stat_names, 
        'pokemon_stats': pokemon_stats,
        'pokemon_types': pokemon_types
        }

    return render(request, "index.html", context)