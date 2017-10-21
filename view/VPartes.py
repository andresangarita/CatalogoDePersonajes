# -*- coding: utf-8 -*-

#modulos
import sys,pygame
import time
from ..control.main import *

#funcion que inicia pygame
pygame.init()

#dimensiones de ventana
display_width = 800
display_height = 400

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("personaje seleccionado")
clock = pygame.time.Clock()

def text_title(personaje):
    font = pygame.font.Font(None,30)
    text = font.render(personaje, True, black)
    gameDisplay.blit(text,(320, 10))

def game_loop_partes(personaje):
    
    while True:
        
        gameDisplay.fill(white)
        text_title(personaje)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGamePartes()
            
        pygame.display.update()
        clock.tick(60)

def quitGamePartes():
    pygame.quit()
    quit()    
