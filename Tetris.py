import pygame
from random import choice
import schedule
import time


# Initialize pygame
pygame.init()

# Global constants
background_colour = (0, 0, 0)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 850
GRID_SIZE = 50  # Size of each grid cell
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tetris')

# Global variables
running = True
colors = {
    "lightblue": (0, 255, 255),
    "darkblue": (0, 102, 255),
    "orange": (255, 153, 0),
    "yellow": (252, 255, 56),
    "green": (102, 255, 102),
    "purple": (204, 102, 255),
    "red": (255, 0, 0),
    "white": (255, 255, 255)
}

tetronimos = {
    "I_Shape": {"Shape": [(0, 0), (0, -1), (0, -2), (0, 1)], "color": colors.get("lightblue")},
    "O_Shape": {"Shape": [(0, 0), (0, -1), (1, 0), (1, -1)], "color": colors.get("yellow")},
    "L_Shape": {"Shape": [(0, 0), (0, -1), (1, 0), (1, 1)], "color": colors.get("orange")},
    "J_Shape": {"Shape": [(0, 0), (0, -1), (0, 1), (-1, 0)], "color": colors.get("darkblue")},
    "Z_Shape": {"Shape": [(0, 0), (1, 0), (0, -1), (-1, -1)], "color": colors.get("red")},
    "S_Shape": {"Shape": [(0, 0), (-1, 0), (0, -1), (1, -1)], "color": colors.get("green")},
    "T_Shape": {"Shape": [(0, 0), (-1, 0), (1, 0), (0, -1)], "color": colors.get("purple")},
}

vel = GRID_SIZE
time_interval = 600
current_time_block = pygame.time.get_ticks()
current_time = pygame.time.get_ticks()
moveing_time = 0
keys = pygame.key.get_pressed()
moveing_time_block = 0
time_interval_block = 120
class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


pos_y = 0.236
# pos_x =

keys = pygame.key.get_pressed()



class Tetronimo:
    def __init__(self, shape, color, group):
        self.block_positions = tetronimos[shape]["Shape"]
        self.color = tetronimos[shape]["color"]
        self.blocks = [
            Block(group, (pos[0] * GRID_SIZE + WINDOW_WIDTH // 2, pos[1] * GRID_SIZE + WINDOW_HEIGHT * pos_y),
                  self.color)
            for pos in self.block_positions
        ]
        self.last_move_time = pygame.time.get_ticks()

    def move_down(self):
        for block in self.blocks:
            block.rect.y += GRID_SIZE

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time >= time_interval:
            self.move_down()
            self.last_move_time = current_time

    def movement_keys(self):
        keys = pygame.key.get_pressed()  # Get the current key states
        for block in self.blocks:
            if keys[pygame.K_a]:
                block.rect.x -= GRID_SIZE
            if keys[pygame.K_d]:  # Check if the 'd' key is pressed
                block.rect.x += GRID_SIZE

    def update_keys(self):
        current_time_block = pygame.time.get_ticks()
        if current_time_block - self.last_move_time >= time_interval_block:
            self.movement_keys()
            self.last_move_time = current_time_block



#schedule.every(0.5).seconds.do(falling)

class Sprites:
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.Tetronimo = Tetronimo(
            choice(list(tetronimos.keys())), colors.get("white"), group=self.sprites
        )

def drawGrid():
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, colors["white"], (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, colors["white"], (0, y), (WINDOW_WIDTH, y))

def main_game_loop():
    global running
    running = True
    clock = pygame.time.Clock()



    all_sprites = pygame.sprite.Group()

    sprites_instance = Sprites()

    schedule.run_pending()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False






        keys = pygame.key.get_pressed()  # Get the current key states
        if keys[pygame.K_a] or keys[pygame.K_d]:
            sprites_instance.Tetronimo.update_keys()

      #  if (pygame.time.get_ticks() %  2) == 0:
       #     pos_y += 0.002

        sprites_instance.Tetronimo.update()
        screen.fill(background_colour)
        drawGrid()
        sprites_instance.sprites.draw(screen)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)


    pygame.quit()

if __name__ == "__main__":
    main_game_loop()
