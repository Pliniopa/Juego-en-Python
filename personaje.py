import pygame

import constantes

class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False #Funcion para voltear el personaje

        self.animaciones = animaciones
        #Imagen de la animacion que se esta mostrando actualmente
        self.frame_index = 0

        self.update_time = pygame.time.get_ticks() #alamcena los milisegundos desde que se abre el jueguito


        self.image = animaciones[self.frame_index] #Halar la imagen

        self.forma = self.image.get_rect()
        
        #pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE) # Creacion de un rectangulo  0 , 0, Alto de personaje, Ancho Personaje
        self.forma.center = (x, y)              # inicializarlo en la coordenada dada

   
   
   
    def dibujar (self, interfaz): # dibujar el personaje

        imagen_flip = pygame.transform.flip(self.image, self.flip,  False) #Guarda la transformacion
        #                                               eje x   eje y
        interfaz.blit(imagen_flip, self.forma) #mostrar el personaje en la ventana
        #pygame.draw.rect(interfaz, (constantes.COLOR_PERSONAJE), self.forma, 1) #Rectangulo de marco

    
    
    
    
    def movimiento (self, delta_x, delta_y):
        
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False


        
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y +delta_y





    def update(self):
        cooldown_animacion = 100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

