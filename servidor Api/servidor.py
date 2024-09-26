import fastapi
from fastapi import HTTPException
import json
from anime import *
from usuarioApi import *
from tokenApi import *

app = fastapi.FastAPI()
app.include_router(usuario_router, prefix="/usuarios", tags=["usuarios"])
app.include_router(anime_router, prefix="/animes", tags=["animes"])
app.include_router(token_router)