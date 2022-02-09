import pygame
from pygame.locals import *

BLOCK_SIZE = 20

class Block:

    def __init__(self, posx, posy, color):
        self.posx = posx
        self.posy = posy
        self.color = color

    def __eq__(self, other):
        return self.posx == other.posx and self.posy == other.posy

    def draw_block(self, surface):
        pygame.draw.rect(surface, self.color, (self.posx, self.posy, BLOCK_SIZE, BLOCK_SIZE), 0)

class Apple(Block):
    
    def __init__(self, parent_screen):
        super().__init__(BLOCK_SIZE*3, BLOCK_SIZE*3, (255, 0, 0))
        self.parent_screen = parent_screen

    def draw_apple(self):
        super().draw_block(self.parent_screen)
        pygame.display.update()

class Snake:

    def __init__(self, parent_screen, color_screen, position_initial:tuple, color_blocks, length):
        self.length = length
        self.parent_screen = parent_screen
        self.color_screen = color_screen
        self.direction = 'down'
        
        self.parts = []
        self._add_blocks(position_initial[0], position_initial[1], color_blocks)

    def _add_blocks(self, pos_x, pos_y, color):
        for x in range(self.length):
            self.parts.append(Block(pos_x, pos_y, color))

    def draw(self):
        self.parent_screen.fill(self.color_screen)
        
        for x in range(len(self.parts)):
            self.parts[x].draw_block(self.parent_screen)

        pygame.display.update()

    def move_up(self):
        self.direction = 'up'
    
    def move_down(self):
        self.direction = 'down' 

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.parts[i].posx = self.parts[i-1].posx
            self.parts[i].posy = self.parts[i-1].posy

        if self.direction == 'down':
            self.parts[0].posy += BLOCK_SIZE
        elif self.direction == 'up':
            self.parts[0].posy -= BLOCK_SIZE
        elif self.direction == 'right':
            self.parts[0].posx += BLOCK_SIZE
        elif self.direction == 'left':
            self.parts[0].posx -= BLOCK_SIZE
        self.draw()