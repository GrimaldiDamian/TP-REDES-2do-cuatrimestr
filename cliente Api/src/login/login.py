import pygame
from src.utilidades.utilidades import *
import requests

class login():
    def __init__(self):
        self.logeo = ""
        self.password = ""
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
            else:
                self.password += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.momento == "Login":
                    self.logeo = self.logeo[:-1]
                else:
                    self.password = self.password[:-1]
            elif event.key == pygame.K_RETURN:
                if self.momento == "Login":
                    self.momento = "Password"
                else:
                    self.login()

    def dibujar(self,screen : pygame.Surface,fuente : pygame.font):
        """
        Dibuja en pantalla el login
        Args:
            screen (pygame.Surface): Es la pantalla en la que se dibujara
            fuente (pygame.font): Es la fuente que se utilizara para escribir en pantalla
        """
        screen.blit(self.img, (0,0))
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

    def resetear(self):
        """
        Resetea los valores de login y password
        """
        self.logeo = ""
        self.password = ""
        self.momento = "Login"

    def login(self):
        """
        Realiza el proceso de login
        """
        url = "http://localhost:8000/token"
        try:
            data = {
                "username": self.logeo,
                "password": self.password
            }
            response = requests.post(url, data=data)
            global_variables.token = response.json()
            self.resetear()
            global_variables.etapa = "menu"
        except:
            self.resetear()
            print("Login failed. Please try again.")