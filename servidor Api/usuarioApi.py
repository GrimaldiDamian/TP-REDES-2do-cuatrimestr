from fastapi import Depends, APIRouter, HTTPException
from typing import Annotated
from manejo_archivo import *
from util import *

nombre_archivo = f"{ruta}usuarios.json"
usuarios = abrir_archivo(nombre_archivo)

usuario_router = APIRouter()

@usuario_router.get("/Obtener_usuario")
def Obtener_usuario(usuario):
    return usuarios[usuario]

@usuario_router.get("/Obtener_nick_usuario")
def Obtener_nick_usuario():
    usuario = []
    for claves in usuarios.keys():
        if claves not in usuario:
            usuario.append(claves)
    return usuario

@usuario_router.get("/tipo_usuario")
def tipo_usuario(usuario: str):
    # Verificamos si el usuario existe en el JSON
    if usuario in usuarios:
        tipo = usuarios[usuario]["tipo de usuario"]
        return {"usuario": usuario, "tipo": tipo}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@usuario_router.post("/Crear cuenta")
def Crear_cuenta (usuario :str,contraseña:str,correo:str ,tipo_usuario = "users"):
    try:
        if usuario in usuarios:
            raise HTTPException(status_code=400, detail="El usuario ya existe.")

        dic = {
            "usuario": usuario,
            "password": contraseña,
            "correo": correo,
            "tipo de usuario": tipo_usuario
        }
        usuarios[usuario] = dic
        guardar_archivo(nombre_archivo, usuarios)
        

        return {"detail": f"Cuenta creada exitosamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocurrió un error: {e}")

def actualizar(user : dict, usuario : str, campo : str, cambio : str):
    if usuario in usuarios:
        if user["tipo de usuario"] == "admin" or user["usuario"] == usuario:
            usuarios[usuario][campo] = cambio
            guardar_archivo(nombre_archivo, usuarios)
            return "La información se guardó correctamente."
        else:
            raise HTTPException(status_code=400, detail="No tiene permisos para realizar esta acción.")
    else:
        raise HTTPException(status_code=400, detail = "No existe usuario")

@usuario_router.put("/Actualizar_tipo")
def Actualizar_tipo(user: Annotated[dict,Depends(decode_token)],nick : str, tipo : str):
    if user["tipo de usuario"] != "admin":
        raise HTTPException(status_code=403, detail="Fue rechazado por el servidor")
    else:
        if nick in usuarios:
            usuarios[nick]["tipo de usuario"] = tipo
            guardar_archivo(nombre_archivo,usuarios)
            return "Se modifico correctamente"
        else:
            raise HTTPException(status_code=400, detail=f"No existe ningun usuario registrado como {nick}")

@usuario_router.put("/Actualizar password")
def actualizar_password(user: Annotated[dict,Depends(decode_token)],usuario : str, password : str):
    return actualizar(user,usuario,"password",password)

@usuario_router.put("/Actualizar correo")
def actualizar_correo(user: Annotated[dict,Depends(decode_token)],usuario : str, correo : str):
    return actualizar(user,usuario,"correo",correo)

@usuario_router.delete("/eliminar usuario")
def eliminar_usuario(user: Annotated[dict,Depends(decode_token)],usuario : str):
    if usuario in usuarios:
        if user["usuario"] == usuario or user["tipo de usuario"] == "admin":
            usuarios.pop(usuario)
            guardar_archivo(nombre_archivo,usuarios)
            return f"Se elimino correctamente"
        raise HTTPException(status_code=400, detail = "No se puede eliminar dicho usuario")
    else:
        raise HTTPException(status_code=400, detail = "No existe dicho usuario")