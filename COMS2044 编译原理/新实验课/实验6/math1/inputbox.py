import pygame
from util import *

class InputBox:
    def __init__(self,surface,color,font):
        self.surface=surface
        self.color=color
        self.font=font
        
        self.text=""
        self.fun=None
        self.is_draw=False

    def enter(self,event):
        if event.key==pygame.K_RETURN:
            self.fun=parse(self.text)
            self.text=""
            return

        if event.key==pygame.K_BACKSPACE:
            self.text=self.text[:-1]
        else:
            self.text+=event.unicode
    
    def draw(self):
        draw_text(self.surface,self.font,self.text,self.color,(50,640))

    def clear(self):
        self.is_draw=False
        self.text=""