import pygame

##Deteccion de teclas para el movimiento del personaje

def movimiento(event):
 
     if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("Izquierda")
            if event.key == pygame.K_d:
                print("Derecha")
            if event.key == pygame.K_w:
                print("Arriba")
            if event.key == pygame.K_s:
                print("Abajo")