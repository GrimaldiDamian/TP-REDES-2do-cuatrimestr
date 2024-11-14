# Proyecto de Redes de Datos - Trabajo Práctico

Este proyecto es un trabajo práctico de la universidad cuyo objetivo es desarrollar un servidor API y una interfaz para el cliente (en mi caso, implementada con Pygame). Dependiendo del tipo de cuenta del usuario (admin o user), se le presenta un menú personalizado. Este proyecto se enfoca en desarrollar y demostrar conocimientos en el manejo de APIs.

## Librerías necesarias

Para este proyecto, necesitarás instalar las siguientes librerías:

- `pygame`
- `uvicorn`
- `fastapi`
- `requests`
- `python-jose`

## Crear y activar un entorno virtual

### En Linux
1. Crear el entorno virtual:
    ```bash
    python3 -m venv .venv
    ```

2. Activar el entorno virtual:
    ```bash
    source .venv/bin/activate
    ```

### En Windows

1. Crear el entorno virtual:
    ```bash
    python -m venv ./.venv
    ```

2. Activar el entorno virtual:
    ```bash
    .venv\Scripts\activate
    ```

## Instalación de librerías

Una vez que el entorno virtual esté activado, puedes instalar las librerías necesarias con el siguiente comando:

```bash
pip install pygame uvicorn fastapi requests python-jose
```
## Ejecución del Servidor API

Para ejecutar el servidor API, sigue estos pasos:

1. Abre Visual Studio Code en la carpeta del servidor API.
2. Asegúrate de que el entorno virtual esté activado.
3. Ejecuta el siguiente comando para iniciar el servidor con Uvicorn:
    ```bash
    uvicorn servidor:app --reload
    ```

El servidor API estará disponible en `http://localhost:8000`.

## Ejecución del Cliente

Para ejecutar la interfaz del cliente, sigue estos pasos:

1. Abre Visual Studio Code en la carpeta del cliente.
2. Asegúrate de que el entorno virtual esté activado.
3. Ejecuta el archivo `main.py` con el siguiente comando:
    ```bash
    python main.py
    ```

## Notas Importantes

- El servidor API y el cliente deben ejecutarse en computadoras diferentes dentro de la misma red para este trabajo práctico. Sin embargo, también es posible ejecutarlos en la misma computadora para pruebas.
- Asegúrate de que ambas computadoras estén conectadas a la misma red y que no haya restricciones de firewall que impidan la comunicación entre ellas.

¡Y eso es todo! Ahora estás listo para comenzar a trabajar en tu proyecto.