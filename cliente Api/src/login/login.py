import pygame

class login():
    def __init__(self):
        self.img = pygame.image.load("./cliente Api/assets/img/login.png") #cargar la imagen correspondiente

    def dibujar_texto(self,screen,texto,fuente,x,y):
        texto = fuente.render(texto,True,(0,0,0))
        screen.blit(texto,(x,y))

    def dibujar(self,screen):
        screen.blit(self.img, (0,0))

    def login(self):
        pass