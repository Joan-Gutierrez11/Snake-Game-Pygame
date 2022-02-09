from modelos_juego import *

class Game:
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    def __init__(self, dimensions:tuple):
        self.window = None
        self.close_window = False
        self.name = 'Snake Game'
        self.dimension = dimensions

        pygame.init()
        self._init_component()

        self.snake = Snake(self.window, self.WHITE, (20,20), self.GREEN, 3)
        self.snake.draw()

        self.apple = Apple(self.window)
        self.apple.draw_apple()

    def _init_component(self):
        self.window = pygame.display.set_mode(self.dimension)
        self.window.fill((255, 255, 255))
        pygame.display.set_caption(self.name)
        pygame.display.update()

    def play(self):
        self.snake.walk()
        self.apple.draw_apple()
    
    def run(self):
        while not self.close_window:
            pygame.time.delay(120)
            for event in pygame.event.get():                
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.snake.move_up()
                    elif event.key == K_DOWN:
                        self.snake.move_down()
                    elif event.key == K_LEFT:
                        self.snake.move_left()
                    elif event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    self.close_window = True
            
            self.play()

        pygame.quit()
        quit()



if __name__ == '__main__':
    g = Game((400, 300))
    g.run()
