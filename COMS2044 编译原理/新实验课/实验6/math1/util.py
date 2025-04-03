import pygame
import math

pygame.init()

# colors & fonts
white_color=(255,255,255)
grey_color=(190,190,190)
black_color=(0,0,0)
blue_color=(0,0,255)

a20_font=pygame.font.SysFont("arial",20)

def draw_text(surface,font,text,color,position):
    text_surface=font.render(text,True,color)
    
    surface.blit(text_surface,position)

def draw_background(screen):

    # Coordinate System
    for i in range(30,600,30):
        pygame.draw.line(screen,grey_color,(0,i),(600,i),1)
        pygame.draw.line(screen,grey_color,(i,0),(i,600),1)

    # bottom
    pygame.draw.line(screen,black_color,(0,600),(600,600),3)

    pygame.draw.line(screen,black_color,(0,300),(600,300),2)
    pygame.draw.line(screen,black_color,(300,0),(300,600),2)

    draw_text(screen,a20_font,"0",black_color,(305,302))
    draw_text(screen,a20_font,"X",black_color,(580,302))
    draw_text(screen,a20_font,"Y",black_color,(305,2))

    # Input Box
    draw_text(screen,a20_font,"Please input your formula:",black_color,(50,610))
    pygame.draw.line(screen,black_color,(50,665),(550,665),1)

# simple parser ...
def parse(text):
    right=text[2:]
    if right[:3]=="sin":
        return lambda x:math.sin(x)
    elif right[:3]=="cos":
        return lambda x:math.cos(x)
    else:
        return lambda x:x**2