from modelos_juego import *

class Game:
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)

    def __init__(self, dimensions:tuple):
        self.window = None
        self.close_window = False
        self.name = 'Snake Game'
        self.dimension = dimensions

        pygame.init()
        self._init_window()

        self._init_components()
        self.snake.draw()
        self.apple.draw_apple()

    def _init_window(self):
        self.window = pygame.display.set_mode(self.dimension)
        self.window.fill((255, 255, 255))
        pygame.display.set_caption(self.name)
        pygame.display.update()

    def _init_components(self):
        self.snake = Snake(self.window, self.WHITE, (20,20), self.GREEN, 1)
        self.apple = Apple(self.window)

    def display_score(self):
        font = pygame.font.SysFont('arial', 25)
        score = font.render(f'Score: {self.snake.length}', True, self.BLACK)
        self.window.blit(score, (275, 0.5))

    def play(self):
        self.snake.walk()
        self.apple.draw_apple()
        self.display_score()
        pygame.display.update()
        
        if self.snake.head.exist_collison(self.apple):
            self.apple.move_other_position(self.snake)
            self.snake.increment_parts()
        
        if self.snake.auto_collision():
            raise 'Collision'
    
    def show_game_over(self):
        self.window.fill((255, 255, 255))
        font = pygame.font.SysFont('arial', 20)
        line1 = font.render(f'Game Over. Your score is: {self.snake.length}', True, self.BLACK)
        self.window.blit(line1, (15, 40))
        line2 = font.render('Press Enter to play Again or Esc to quit', True, self.BLACK)
        self.window.blit(line2, (15, 70))
        pygame.display.update()


    def run(self):
        pause = False
        game_over = False

        while not self.close_window:
            pygame.time.delay(120)
            for event in pygame.event.get():                
                if event.type == KEYDOWN:
                    #Pause the game
                    if event.key == K_BACKSPACE:
                        if not pause:
                            pause = True
                        else:
                            pause = False

                    if event.key == K_RETURN:
                        pause = False
                        if game_over:
                            self._init_components()

                    #Exit the game
                    if event.key == K_ESCAPE:
                        self.close_window = True
                    
                    if not pause:
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
            
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                game_over = True

        pygame.quit()
        quit()



if __name__ == '__main__':
    g = Game((400, 300))
    g.run()
