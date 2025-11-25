import pygame, math
import constantes;

class Weapon():
    def __init__(self, image): #Constructor
        self.imagen_original = image
        self.angulo = 0 #angulo
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo) #rotar imagen
        self.forma = self.imagen.get_rect()

    
    def update(self, personaje):
        self.forma.center = personaje.forma.center #centrado de punto cartesiano

        if personaje.flip == False:
            self.forma.x = self.forma.x + (personaje.forma.width / constantes.DIVISOR_DISTANCIA_ARMA)
            self.rotar_arma(False)
        if personaje.flip == True:
            self.forma.x = self.forma.x - (personaje.forma.width / constantes.DIVISOR_DISTANCIA_ARMA)
            self.rotar_arma(True)
        
        #Mover la pistola con el mouse

        mouse_pos = pygame.mouse.get_pos()

        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = - (mouse_pos[1] - self.forma.centery)

        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))

       
       
       
        #self.forma.y = self.forma.y + (- 45) #constantes.DIVISOR_DISTANCIA_ARMA




    def dibujar(self, interfaz):

        self.imagen = pygame.transform.rotate(self.imagen, 
                                              self.angulo)

        interfaz.blit(self.imagen, self.forma) #dibujado ("poner imagen")
        #pygame.draw.rect(interfaz, (constantes.COLOR_ARMA), self.forma, 1) #Rectangulo de marco


#Rotacion de arma
    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.imagen_original,
                                               True, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original,
                                               False, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

        


