import pygame

from personaje import Personaje

import constantes 


#Creacion de personaje

jugador = Personaje(50, 50) # creacion y pase de coordenadas a usar



pygame.init() #Inicializar libreria

#Creacion de ventana

ventana= pygame.display.set_mode((constantes.ANCHO, constantes.ALTO)) # Creacion de una ventana

pygame.display.set_caption("Jueguito 1") # Cambiar el nombre de la ventana


run = True

while run:

    

    jugador.dibujar(ventana) #Dibujar personaje

    for event in pygame.event.get(): # trae y entrega todos los eventos ejecutados en el juego

        if event.type == pygame.QUIT: # identificar el tipo de evento

            run = False                # Cambio de estado re uno de true a false para cerrar la ventana

        pygame.display.update() #Actualizar la ventana para ver parametros




pygame.quit()