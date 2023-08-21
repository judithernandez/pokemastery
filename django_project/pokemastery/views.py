from django.http import HttpResponse
from django.shortcuts import render
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, ".."))

from pokeapi.requests import get_pokemon_data


def greetings(request):
    return HttpResponse("Hello, PokéWorld!")

def pokepedia(request):
    return render(request, "pokepedia.html")

def pokemon(request, pokemon):
    
    data = get_pokemon_data(pokemon)

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
        

    # Render the pokemon.html template with the context
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

    return render(request, "pokemon.html", context)