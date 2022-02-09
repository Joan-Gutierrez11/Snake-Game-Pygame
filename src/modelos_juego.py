import pygame
from pygame.locals import *
from random import randint

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

    '''def exist_collison(self, other):
        if self.posx >= other.posx and self.posx <= other.posx + BLOCK_SIZE:
            if self.posy >= other.posy and self.posy <= other.posy + BLOCK_SIZE:
                return True
        return False'''

    def exist_collison(self, other):
        return self == other

class Apple(Block):
    
    def __init__(self, parent_screen):
        super().__init__(BLOCK_SIZE*3, BLOCK_SIZE*3, (255, 0, 0))
        self.parent_screen = parent_screen

    def draw_apple(self):
        super().draw_block(self.parent_screen)
        pygame.display.update()

    def move_other_position(self, snake):
        while True:
            self.posx = randint(0, (self.parent_screen.get_size()[0]//BLOCK_SIZE)-1)*BLOCK_SIZE
            self.posy = randint(0, (self.parent_screen.get_size()[1]//BLOCK_SIZE)-1)*BLOCK_SIZE
            if self not in snake.parts:
                break
        

class Snake:

    def __init__(self, parent_screen, color_screen, position_initial:tuple, color_blocks, length):
        self.length = length
        self.parent_screen = parent_screen
        self.color_screen = color_screen
        self.color = color_blocks
        
        self.parts = []
        self._add_blocks(position_initial[0], position_initial[1])
        self.head:Block = self.parts[0]
        self.head.color = (0, 0, 255)

        self.direction = 'down'
        self.prev_direction = None

    def _add_blocks(self, pos_x, pos_y):
        for x in range(self.length):
            self.parts.append(Block(pos_x, pos_y, self.color))

    def increment_parts(self):
        self.length += 1
        self.parts.append(Block(-1, -1, self.color))

    def draw(self):
        self.parent_screen.fill(self.color_screen)
        for x in range(len(self.parts)):
            self.parts[x].draw_block(self.parent_screen)
        pygame.display.update()
    
    def _change_direction(self, new_dir):
        self.prev_direction = self.direction
        self.direction = new_dir

    def move_up(self):
        self._change_direction('up')
    
    def move_down(self):
        self._change_direction('down')

    def move_left(self):
        self._change_direction('left')

    def move_right(self):
        self._change_direction('right')

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

    def auto_collision(self):
        if self.direction == 'down' and not self.prev_direction == 'up'\
            or self.direction == 'up' and not self.prev_direction == 'down':
            return self.head in self.parts[1:]

        if self.direction == 'left' and not self.prev_direction == 'right'\
            or self.direction == 'right' and not self.prev_direction == 'left':
            return self.head in self.parts[1:]

        