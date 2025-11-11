import pygame

import constantes

class Personaje():
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, constantes.ALTO_PERSONAJE, constantes.ANCHO_PERSONAJE) # Creacion de un rectangulo  0 , 0, Alto de personaje, Ancho Personaje
        self.forma.center = (x, y)              # inicializarlo en la coordenada dada

    def dibujar (self, interfaz): # dibujar el personaje
        pygame.draw.rect(interfaz, (constantes.COLOR_PERSONAJE), self.forma)
