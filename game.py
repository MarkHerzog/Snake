import random
import pygame as py, sys

py.font.init()

class Game:
    def __init__(self):
        self.screen = py.display.set_mode((500, 500))
        self.clock = py.time.Clock()
        self.x, self.y = 250, 250
        self.change = [0, 0]
        self.blocks = [[self.x, self.y]]
        self.spawn_apple()
        self.score = 0
    def update_block(self):
        new_blocks = [[self.x, self.y]]
        for block in self.blocks[:-1]:
            new_blocks.append(block)
        self.blocks = new_blocks
        for block in self.blocks[60:]:
            if py.Rect(self.x, self.y, 1, 1).colliderect(py.Rect(block[0], block[1], 25, 25)):
                self.respawn()
        if 0 >= self.x or self.x >= 500:
            self.respawn()
        if 0 >= self.y or self.y >= 500:
            self.respawn()
    def respawn(self):
        self.x, self.y = 250, 250
        self.change = [0, 0]
        self.spawn_apple()
        self.score = 0
        self.blocks = [[self.x, self.y]]
    def spawn_apple(self):
        self.apple = py.Rect(random.randint(25, 475), random.randint(25, 475), 25, 25)
    def add_block(self):
        for i in range(10):
            self.blocks.append([self.blocks[-1][0], self.blocks[-1][1]])
    def play_frame(self):
        my_font = py.font.SysFont('Comic Sans MS', 30)
        self.update_block()
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_RIGHT:
                    if self.change != [-2, 0]:
                        self.change = [2, 0]
                if event.key == py.K_LEFT:
                    if self.change != [2, 0]:
                        self.change = [-2, 0]
                if event.key == py.K_UP:
                    if self.change != [0, 2]:
                        self.change = [0, -2]
                if event.key == py.K_DOWN:
                    if self.change != [0, -2]:
                        self.change = [0, 2]
        self.x += self.change[0]
        self.y += self.change[1]

        self.screen.fill((0, 0, 0))
        score = my_font.render(str(self.score), False, (255, 255, 255))
        for snake in self.blocks:
            block_rect = py.Rect(snake[0], snake[1], 25, 25)
            py.draw.rect(self.screen, (50, 255, 50), block_rect)
            if block_rect.colliderect(self.apple):
                self.add_block()
                self.spawn_apple()
                self.score += 1
        py.draw.rect(self.screen, (255, 50, 50), self.apple)
        self.screen.blit(score, (0, 0))
        py.display.update()

        self.clock.tick(120)

game = Game()

while True:
    game.play_frame()