import json

ruta = "./archivos/"

def abrir_archivo(nombre_archivo : str) -> dict:
    with open(nombre_archivo,'r') as file:
        archivo = json.load(file)
    return archivo

def guardar_archivo(nombre_archivo : str,contenido : dict):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(contenido, archivo, indent=4)