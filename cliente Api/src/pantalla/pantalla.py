import pygame
from src.utilidades.utilidades import *
from src.login.login import *

class Screen():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((ancho,alto))
        pygame.display.set_caption("Cliente API")
        self.reloj = pygame.time.Clock()
        self.runnig = True
        self.fuente = pygame.font.SysFont("Times New Roman",tamaño_letra)
        self.login = login()

    def manejo_eventos(self):
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                self.runnig = False

    def dibujar(self):

        # self.screen.fill("red")
        if etapa in ["login","crear"]:
            self.login.dibujar(self.screen)

        pygame.display.flip()

    def bucle_principal(self):
        while self.runnig:
            self.manejo_eventos()

            self.reloj.tick(60)

            self.dibujar()