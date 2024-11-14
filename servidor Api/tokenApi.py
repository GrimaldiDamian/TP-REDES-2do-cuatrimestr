from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from util import *
from usuarioApi import Obtener_usuario
from jose import jwt

token_router = APIRouter()
contraseña = OAuth2PasswordBearer(tokenUrl="token")

@token_router.post("/token")
def token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    usuario = Obtener_usuario(form_data.username)

    if not usuario or usuario["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Usuario o password incorrecto")

    token = encode_token({"usuario": usuario["usuario"], "email": usuario["correo"]})
    return {"access_token": token, "token_type": "bearer"}