# -*- coding: utf-8 -*-

#modulos
import sys,pygame
import time
from ..control.main import *
 

#funcion que inicia pygame
pygame.init()

#-------------------------constantes--------------------------------------

#____windows_____
#route='c:/users/usuario/Desktop/ejercicioCatalogo/'
#_____linux______
route='/home/AndresAngarita/Documentos/ModelosDeProgramacion/ejercicioCatalogo/'

#dimensiones de ventana
display_width = 800
display_height = 400

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Catalogo de Personajes')
clock = pygame.time.Clock()

#se hace la carga de las imagenes
ogroImg=pygame.image.load(route+'media/imgs/orcoCho.png')
humanoImg=pygame.image.load(route+'media/imgs/humanoCho.png')
elfoImg=pygame.image.load(route+'media/imgs/elfoCho.png')

#funciones
def text_title():
    font = pygame.font.Font(None,30)
    text = font.render("Elija un Personaje", True, black)
    gameDisplay.blit(text,(320, 10))

def paint_person(x,y):
    gameDisplay.blit(ogroImg,(x,y))
    gameDisplay.blit(humanoImg,(x+240,y))
    gameDisplay.blit(elfoImg,(x+480,y))

def button(x,y,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    square = pygame.Rect((x,y),(x+w,y+h))
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if  click[0] == 1 and action != None:
            action()
    
            

def game_loop():
    
    while True:
        
        gameDisplay.fill(white)
        text_title()
        paint_person(50,70)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button(50,70,200,250,buildOrco)
                button(290,70,200,250,buildHumano)
                button(530,70,200,250,buildElfo)
                quitGame()
                
        pygame.display.update()
        clock.tick(60)

def quitGame():
    pygame.quit()
    quit()    

game_loop()
quitGame()