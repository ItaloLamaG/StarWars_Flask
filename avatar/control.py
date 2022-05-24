import json
import requests 
from .datos import planeta_obj, personaje_obj, pelicula_obj

__all__ = ["obtener_planetas",
           "obtener_peliculas",
           "obtener_personajes"]

def obtener_planetas():
    lista_planetas = []
    #Api de multiples paginas
    siguiente_pagina = "https://swapi.dev/api/planets/"
    while siguiente_pagina:
        json_data = json.loads((requests.get(siguiente_pagina)).content)
        siguiente_pagina = json_data["next"]
        for json_planeta in json_data["results"]:
            nuevo_planeta = planeta_obj(_limpiar_vacio(json_planeta["name"]),
                                    _limpiar_vacio(json_planeta["rotation_period"]),
                                    _limpiar_vacio(json_planeta["orbital_period"]),
                                    _limpiar_vacio(json_planeta["diameter"]),
                                    _limpiar_vacio(json_planeta["climate"]),
                                    _limpiar_vacio(json_planeta["terrain"]),
                                    _limpiar_vacio(json_planeta["population"]),
                                    _limpiar_vacio(json_planeta["residents"]),
                                    _limpiar_vacio(json_planeta["gravity"]))
            lista_planetas.append(nuevo_planeta)
    return lista_planetas


def obtener_peliculas():
    lista_peliculas = []
    #Api de multiples paginas
    siguiente_pagina = "https://swapi.dev/api/films/"
    while siguiente_pagina:
        json_data = json.loads((requests.get(siguiente_pagina)).content)
        siguiente_pagina = json_data["next"]
        for json_pelicula in json_data["results"]:
            nueva_pelicula = pelicula_obj(_limpiar_vacio(json_pelicula["title"]),
                                    _limpiar_vacio(json_pelicula["episode_id"]),
                                    _limpiar_vacio(json_pelicula["opening_crawl"]),
                                    _limpiar_vacio(json_pelicula["director"]),
                                    _limpiar_vacio(json_pelicula["producer"]),
                                    _limpiar_vacio(json_pelicula["release_date"]))
            lista_peliculas.append(nueva_pelicula)
    return lista_peliculas


def obtener_personajes():
    lista_personajes = []
    #Api de multiples paginas
    siguiente_pagina = "https://swapi.dev/api/people/"
    while siguiente_pagina:
        json_data = json.loads((requests.get(siguiente_pagina)).content)
        siguiente_pagina = json_data["next"]
        for personaje_json in json_data["results"]:
                nuevo_personaje = personaje_obj(
                              _limpiar_vacio(personaje_json["name"]),
                              _limpiar_vacio(personaje_json["height"]),
                              _limpiar_vacio(personaje_json["mass"]),
                              _limpiar_vacio(personaje_json["hair_color"]),
                              _limpiar_vacio(personaje_json["skin_color"]),
                              _limpiar_vacio(personaje_json["eye_color"]),
                              _limpiar_vacio(personaje_json["birth_year"]),
                              _limpiar_vacio(personaje_json["gender"]))
                lista_personajes.append(nuevo_personaje)
    return lista_personajes

#Manejo de datos vacios
def _limpiar_vacio(dato):
    if dato == "N/A" or dato == "unknown":
        return "Dato Desconocido"
    else:
        return dato