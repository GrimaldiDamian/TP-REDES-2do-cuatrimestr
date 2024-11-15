import pygame
from src.utilidades.utilidades import *
from src.login.login import *
from src.menu.menu import *

class Screen():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((ancho,alto))
        pygame.display.set_caption("Cliente API")
        self.reloj = pygame.time.Clock()
        self.runnig = True
        self.fuente = pygame.font.SysFont("Times New Roman",tamaño_letra)
        self.login = login()
        self.menu = Menu()

    def manejo_eventos(self):
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT or (eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_ESCAPE) and global_variables.etapa == "Inicio":
                self.runnig = False
            if global_variables.etapa in ['login','crear']:
                self.login.manejo_evento(eventos)
            elif global_variables.etapa in ['Inicio','Menu']:
                self.menu.manejo_evento(eventos)

    def dibujar(self):

        # self.screen.fill("red")
        if global_variables.etapa in ["login","crear"]:
            self.login.dibujar(self.screen,self.fuente)
        elif global_variables.etapa in ["Inicio","Menu"]:
            self.menu.dibujar(self.screen,self.fuente)

        pygame.display.flip()

    def bucle_principal(self):
        pygame.key.start_text_input()
        while self.runnig:
            self.manejo_eventos()

            self.reloj.tick(60)

            self.dibujar()
        pygame.key.stop_text_input()