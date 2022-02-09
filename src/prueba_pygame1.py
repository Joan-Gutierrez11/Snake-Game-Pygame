import pygame
from pygame.locals import *


''' 
    #Forma para iniciar una ventana en pygame
    pygame.init()
    #Creamos la ventana con el tamanio de la tupla 
    dis = pygame.display.set_mode((400, 300))

    #Ponemos de color de fondo blanco
    dis.fill((255, 255, 255))

    pygame.display.set_caption('Snake Game')
    pygame.display.update()

    # En el bucle while indicamos que la ventana se mantega abierta
    close_window = False    
    while not close_window:
        pygame.time.delay(20)

        for event in pygame.event.get():
            if event.type == QUIT:
                close_window = True

    pygame.quit()
    quit()
'''


def main():
    pygame.init()
    dis = pygame.display.set_mode((400, 300))
    dis.fill((255, 255, 255))
    pygame.display.update()
    pygame.display.set_caption('Snake Game')
    pygame.display.update()

    posx = 10
    posy = 10

    cube_w = 20
    cube_h = 20

    close_window = False
    while not close_window:
        pygame.time.delay(20)

        for event in pygame.event.get():
            if event.type == QUIT:
                close_window = True

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_DOWN] and posy < 300-cube_w:
            posy += 10
        elif teclas[pygame.K_UP] and posy > 0:
            posy -= 10
        elif teclas[pygame.K_RIGHT] and posx < 400-cube_h:
            posx += 10
        elif teclas[pygame.K_LEFT] and posx > 0:
            posx -= 10

        dis.fill((255, 255, 255))
        pygame.draw.rect(dis, pygame.Color(255, 0, 0), [posx, posy, cube_w, cube_h], 0)
        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()