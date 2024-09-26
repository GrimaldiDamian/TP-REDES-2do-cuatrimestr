from fastapi import APIRouter
from manejo_archivo import *

anime_router = APIRouter()

anime = abrir_archivo(f"{ruta}anime.json")

@anime_router.get("/Obtener_Animes",tags = ["animes"])
def Obtener_Animes():
    nombres = []
    for dic_anime in anime:
        nombre = dic_anime["name"]
        if nombre not in nombres:
            nombres.append(nombre)
    return nombres