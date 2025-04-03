import pygame
import math

def draw_curve0(surface,color,function):

    x_list=[]
    y_list=[]
    for x in range(-300,300,1):  
        try:
            y=function(x)
            x_list.append(x)
            y_list.append(y)
        except:
            pass

    maxY=max(y_list)
    minY=min(y_list)

    fold=600.0/(maxY-minY)

    pre_point=(0,0)
    for i in range(len(x_list)):
        x,y=x_list[i],y_list[i]
        y*=fold

        real_x=x+300
        real_y=300-y

        if x==-300:
            pre_point=(real_x,real_y)
        
        pygame.draw.aaline(surface,color,pre_point,(real_x,real_y),1)

        pre_point=(real_x,real_y)

def draw_curve1(surface,color,function):
    draw_curve0(surface,color,lambda x:function(math.pi*x/300))