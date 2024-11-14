from fastapi import APIRouter,HTTPException
from manejo_archivo import *

anime_router = APIRouter()

nombre_archivo = f"{ruta}anime.json"
anime = abrir_archivo(nombre_archivo)

@anime_router.get("/Obtener_Animes")
def Obtener_Animes():
    nombres = []
    for dic_anime in anime:
        nombre = dic_anime["name"]
        if nombre not in nombres:
            nombres.append(nombre)
    return nombres

def gets(columna,name):
    for dic_anime in anime:
        if name == dic_anime["name"]:
            return dic_anime[columna]
    raise HTTPException(status_code=404, detail="Anime no encontrado")

@anime_router.get("/descripcion")
def descripcion(name):
    return gets("description",name)

@anime_router.get("/clasificacion")
def clasificacion(name):
    return gets("Rating",name)

@anime_router.get("/categoria")
def categoria(name):
    return gets("categorie",name)

@anime_router.get("/estudio")
def estudio(name):
    return gets("studio",name)

@anime_router.get("/episodios")
def episodios(name):
    return gets("episode",name)

def puts(columna,name,value):
    for index, dic_anime in enumerate(anime):
        if name == dic_anime["name"]:
            anime[index][columna] = value
            guardar_archivo(nombre_archivo,anime)
    raise HTTPException(status_code=404, detail="Anime no encontrado")

@anime_router.put("/actualizar episodios")
def actualizar_episodios(name: str,episode: int):
    return puts("episode",name,episode)

@anime_router.put("/actualizar descripsion")
def actualizar_episodios(name: str,Rating: float):
    return puts("Rating",name,str(Rating))

@anime_router.put("/actualizar nombre")
def actualizar_nombre(name: str, new_name : str):
    return puts("name",name,new_name)

@anime_router.delete("/eliminar anime")
def delete(name):
    for index, dic_anime in enumerate(anime):
        if name == dic_anime["name"]:
            anime.pop(index)
            guardar_archivo(nombre_archivo,anime)
            return f"Se elimino correctamente"
    raise HTTPException(status_code=404, detail="Anime no encontrado")