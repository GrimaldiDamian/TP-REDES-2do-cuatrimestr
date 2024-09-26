from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from jose import jwt
from manejo_archivo import abrir_archivo, ruta

contraseña = OAuth2PasswordBearer(tokenUrl="token") #token tiene que estar creada
users = abrir_archivo(f"{ruta}usuarios.json")

secret_key = "Digimon Adventure"

def encode_token(payload:dict) ->str:
    token = jwt.encode(payload, secret_key,algorithm="HS256")
    return token

def decode_token(token:Annotated[str,Depends(contraseña)]) -> dict:   
    data = jwt.decode(token,secret_key,algorithms=["HS256"])
    usuario = users.get(data["usuario"])
    return usuario