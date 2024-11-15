import pygame
from src.utilidades.utilidades import *
import requests

class login():
    """
    Clase que se encarga de manejar el login del usuario y la creación de la cuenta
    Args:
        logeo (str): Es el nombre de usuario
        password (str): Es la contraseña del usuario
        correo (str): Es el correo del usuario
        momento (str): Es el momento en el que se encuentra el usuario
    """
    def __init__(self):
        self.logeo = ""
        self.password = ""
        self.correo = ""
        self.momento = "Login"
        self.img = pygame.image.load("./assets/img/login.png") #cargar la imagen correspondiente

    def dibujar_texto(self,screen,texto,fuente,x,y):
        texto = fuente.render(texto,True,(0,0,0))
        screen.blit(texto,(x,y))

    def centrar_texto(self,texto: str,fuente: pygame.font):
        """
        Retorna la coordenada en x de donde se situara el texto en pantalla
        Args:
            texto (str): Cadena de texto que se va a mostrar en pantalla
            fuente (pygame.font): Es la funte del texto
        """
        ancho_p, _ = fuente.size(texto)
        x = (ancho - ancho_p)//2
        return x

    def manejo_evento(self,event : pygame.event.Event):
        """
        Manejo de evento, aca se encagara de escribir en pantalla.
        Args:
            event (pygame.event.Event): Evento que se va a manejar
        """
        if event.type == pygame.TEXTINPUT:
            if self.momento == "Login":
                self.logeo += event.text
            elif self.momento == "Password":
                self.password += event.text
            else:
                self.correo += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.momento == "Login":
                    self.logeo = self.logeo[:-1]
                elif self.momento == "Password":
                    self.password = self.password[:-1]
                else:
                    self.correo = self.correo[:-1]
            elif event.key == pygame.K_RETURN:
                if self.momento == "Login":
                    self.momento = "Password"
                elif self.momento == 'Password':
                    if global_variables.etapa == "login":
                        self.login()
                    else:
                        self.momento = "Correo"
                else:
                    self.creacion_cuenta()
            elif event.key == pygame.K_TAB:
                if self.momento == "Login":
                    self.momento = "Password"
                elif self.momento == "Password":
                    if global_variables.etapa == "login":
                        self.momento = "Login"
                    else:
                        self.momento = "Correo"
                else:
                    self.momento = "Login"
            elif event.key == pygame.K_ESCAPE:
                global_variables.etapa = "Inicio"
                self.resetear()

    def dibujar_inicio(self,screen : pygame.Surface,fuente : pygame.font):
        """
        Dibuja en pantalla el inicio del login
        Args:
            screen (pygame.Surface): Es la pantalla en la que se dibujara
            fuente (pygame.font): Es la fuente que se utilizara para escribir en pantalla
        """
        x = self.centrar_texto(texto = 'Ingrese el usuario',fuente = fuente)
        y = 0
        self.dibujar_texto(screen,'Ingrese el usuario',fuente,x,y)
        y+= tamaño_letra
        x = self.centrar_texto(self.logeo,fuente)
        self.dibujar_texto(screen,self.logeo,fuente,x,y)
        y+= tamaño_letra
        x = self.centrar_texto('Ingrese la password',fuente)
        self.dibujar_texto(screen,'Ingrese la password',fuente,x,y)
        y+= tamaño_letra
        x = self.centrar_texto(self.password,fuente)
        self.dibujar_texto(screen,self.password,fuente,x,y)

    def dibujar_creacion(self,screen : pygame.Surface,fuente : pygame.font):
        """
        Dibuja en pantalla la creacion de la cuenta
        Args:
            screen (pygame.Surface): Es la pantalla en la que se dibujara
            fuente (pygame.font): Es la fuente que se utilizara para escribir en pantalla
        """
        self.dibujar_inicio(screen,fuente)
        x = self.centrar_texto('Ingrese correo electronico',fuente)
        y = 4*tamaño_letra
        self.dibujar_texto(screen,'Ingrese correo electronico',fuente,x,y)
        y+= tamaño_letra
        x = self.centrar_texto(self.correo,fuente)
        self.dibujar_texto(screen,self.correo,fuente,x,y)

    def dibujar(self,screen : pygame.Surface,fuente : pygame.font):
        """
        Dibuja en pantalla el login
        Args:
            screen (pygame.Surface): Es la pantalla en la que se dibujara
            fuente (pygame.font): Es la fuente que se utilizara para escribir en pantalla
        """
        screen.blit(self.img, (0,0))
        if global_variables.etapa == "login":
            self.dibujar_inicio(screen,fuente)
        elif global_variables.etapa == "crear":
            self.dibujar_creacion(screen,fuente)

    def resetear(self):
        """
        Resetea los valores de login y password
        """
        self.logeo = ""
        self.password = ""
        if global_variables.etapa == "crear":
            self.correo = ""
        self.momento = "Login"

    def creacion_cuenta(self):
        """
        Realiza el proceso de creación de la cuenta.
        Donde si es exitoso se cambia la etapa a login y en caso contrario se resetean los valores.
        """
        data = {
            "usuario": self.logeo,
            "contraseña": self.password,
            "correo": self.correo
        }
        try:
            response = requests.post(f"{url}/usuarios/Crear cuenta", params=data)
            self.resetear()
            global_variables.etapa = "Inicio"
        except Exception as e:
            self.resetear()
            print("Account creation failed. Please try again.")

    def login(self):
        """
        Realiza el proceso de login.
        Donde si es exitoso se cambia la etapa a menu y en caso contrario se resetean los valores.
        """
        try:
            data = {
                "username": self.logeo,
                "password": self.password
            }
            response = requests.post(f"{url}/token", data=data)
            global_variables.token = response.json()
            self.resetear()
            global_variables.etapa = "Menu"
        except:
            self.resetear()
            print("Login failed. Please try again.")