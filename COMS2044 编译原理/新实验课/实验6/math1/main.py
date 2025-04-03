import pygame
from pygame.locals import QUIT,KEYDOWN
import sys
from util import *
from inputbox import InputBox
import math
from curve import *

pygame.display.set_caption("Math Painter")
screen = pygame.display.set_mode((600,800))

input_box=InputBox(screen,blue_color,a20_font)

while True:
    # Init 
    screen.fill(white_color)
    draw_background(screen)

    # Events
    for event in pygame.event.get(): 
        # Input
        if event.type==KEYDOWN:
            input_box.enter(event)
            
        # Quit
        if event.type==QUIT:
            sys.exit()
    

    # draw inputbox
    input_box.draw()
    
    # draw curve
    if input_box.fun!=None:
        draw_curve1(screen,blue_color,input_box.fun)
        
    
    # Update
    pygame.display.update()
    