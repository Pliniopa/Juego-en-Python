import pygame

from personaje import Personaje

import constantes 

from Funciones import movimiento

from Weapond import Weapon

pygame.init() #Inicializar libreria

#Creacion de ventana

ventana= pygame.display.set_mode((constantes.ANCHO, constantes.ALTO)) # Creacion de una ventana

pygame.display.set_caption("Jueguito 1") # Cambiar el nombre de la ventana


# Funcion donde se realiza el escalado de las imagenes
def escalar_img(image, scale):
    w = image.get_width() #Altura original
    h = image.get_height() #Anchura original
    nueva_imagn = pygame.transform.scale(image, (w*scale, #Escala en ancho
                                                  h*scale)) #Escala en alto
    return nueva_imagn


# importar imagenes
animaciones = []

#Personahe
for i in range (7):
    img = pygame.image.load(f"assets//Images//Characters//Player//Foto{i}.png")#.convert_alpha
    #                                                                           forzado transparencia de imagenes
    img = escalar_img(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)


#Arma

imagen_pistola = escalar_img( pygame.image.load("assets//Images//Weaponts//gun.png"), constantes.ESCALA_ARMA)
                            
                            #.convert_alpha)




#player_image = pygame.image.load("assets//Images//Characters//Player//Foto1.png") #Dimportar imagen de la ruta relativa del proyecto

#Escala de personaje
#player_image = escalar_img(player_image, constantes.ESCALA_PERSONAJE)

#Creacion de jugador de la clase personaje

jugador = Personaje(50, 50, animaciones) # creacion y pase de coordenadas a usar


#crear un arma de la clase weapond

pistola = Weapon(imagen_pistola)




#Definir variables de movimiento del jugador

mover_arriba = False #falso hasta presionar la tecla W
mover_abajo = False #falso hasta presionar la tecla s
mover_izquerda = False #falso hasta presionar la tecla a
mover_derecha= False #falso hasta presionar la tecla d




reloj = pygame.time.Clock() # controlador de frames por segundo

run = True



while run:

    #FPS

    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_FONDO) #Pintar el fondo

    
    #Calcular movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD

    if mover_izquerda == True:
        delta_x = -(constantes.VELOCIDAD)

    if mover_arriba == True:
        delta_y = -(constantes.VELOCIDAD)

    if mover_abajo== True:
        delta_y = constantes.VELOCIDAD


    #llamado de metodo para mover al jugador

    jugador.movimiento(delta_x, delta_y)

    # Actualiza estado jugador

    jugador.update()

    #Actualiza el estado del arma

    pistola.update(jugador)







    
#Dibujar jugador
    jugador.dibujar(ventana) #Dibujar personaje


    #Dibujar arma

    pistola.dibujar(ventana)

    for event in pygame.event.get(): # trae y entrega todos los eventos ejecutados en el juego

        if event.type == pygame.QUIT: # identificar el tipo de evento

            run = False                # Cambio de estado re uno de true a false para cerrar la ventana


### Movimiento de personaje

       # movimiento(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquerda = True
               # print("Izquierda")
            if event.key == pygame.K_d:
                mover_derecha = True
              #  print("Derecha")
            if event.key == pygame.K_w:

                mover_arriba = True
                #print("Arriba")
            if event.key == pygame.K_s:
                mover_abajo = True
                #print("Abajo")

        # Para cuando se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquerda = False
               # print("Izquierda")
            if event.key == pygame.K_d:
                mover_derecha = False
              #  print("Derecha")
            if event.key == pygame.K_w:

                mover_arriba = False
                #print("Arriba")
            if event.key == pygame.K_s:
                mover_abajo = False
                #print("Abajo")

       



    pygame.display.update() #Actualizar la ventana para ver parametros




pygame.quit()