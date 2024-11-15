import pygame
from src.utilidades.utilidades import *

class Menu():

    def __init__(self) -> None:
        self.img = pygame.image.load("./assets/img/login.png") #Cambiar en el futuro con la imagen del menu correspondiente
        self.opciones_inicio = ["Crear","Login"]
        self.opciones = []
        self.op = 0

    def dibujar_texto(self,screen,texto,fuente,x,y):
        """
        Dibuja un texto en pantalla
        """
        texto = fuente.render(texto,True,(0,0,0))
        screen.blit(texto,(x,y))

    def dibujar_opciones(self,screen,fuente,opciones):
        """
        Dibuja las opciones del menu
        Args:
            screen (pygame.Surface): Superficie de la pantalla
            fuente (pygame.font): Fuente de los textos
            opciones (list): Lista de opciones
        """
        y = 0
        x = 0
        for opcion in opciones:
            self.dibujar_texto(screen,opcion,fuente,x,y)
            y += tamaño_letra
            if y >= alto:
                y = 0
                x += ancho//2

    def dibujar_seleccion(self,screen):
        """
        Dibujar que opcion se esta eligiendo
        Args:
            screen (pygame.Surface): Superficie de la pantalla
        """

        pygame.draw.rect(screen,(0,0,0),(0,self.op*tamaño_letra,ancho//2,tamaño_letra),2)

    def dibujar(self,screen,fuente):
        """
        Dibuja el menu en pantalla
        """
        screen.blit(self.img,(0,0))
        y = 0
        if global_variables.etapa == "Inicio":
            self.dibujar_opciones(screen,fuente,self.opciones_inicio)
        else:
            self.dibujar_opciones(screen,fuente,self.opciones)
        self.dibujar_seleccion(screen)

    def manejo_evento(self,event : pygame.event.Event):
        """
        Maneja los eventos del menu
        Args:
            event (pygame.event.Event): Evento que se va a manejar
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if global_variables.etapa == "Inicio":
                    self.op = max(0,min(len(self.opciones_inicio)-1,self.op+1))
                else:
                    self.op = max(0,min(len(self.opciones)-1,self.op+1))
            elif event.key == pygame.K_UP:
                if global_variables.etapa == "Inicio":
                    self.op = min(len(self.opciones_inicio)-1,max(0,self.op-1))
                else:
                    self.op = min(len(self.opciones)-1,max(0,self.op-1))
            elif event.key == pygame.K_RETURN:
                self.seleccion()
            elif event.key == pygame.K_ESCAPE:
                global_variables.etapa = "Inicio"
                self.op = 0

    def seleccion(self):
        """
        Selecciona una opcion del menu, dependiendo de la etapa en la que se encuentre el cliente api, se realizara una acción.
        Donde si se encuentra en la etapa de inicio, se podra seleccionar entre crear o logearse.
        Y en el caso que sea el menu final, este se encargara de realizar la acción correspondiente.
        """
        if global_variables.etapa == 'Inicio':
            if self.op == 0:
                global_variables.etapa = "crear"
            else:
                global_variables.etapa = "login"
        elif global_variables.etapa == "Menu":
            pass