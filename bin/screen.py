import pygame

class Screen():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.sprites = {}
        self.background = (0, 0, 0)
    
    def load_sprite(self, name, image_path):
        image = pygame.image.load(image_path)
        self.sprites[name] = image

    def show_sprite(self, name, pos):
        image = self.sprites[name]
        blit_pos = (0, 0)
        blit_pos[0] = pos[0] + (image.get_width() / 2)
        blit_pos[1] = pos[1] + (image.get_height()/ 2)
        self.screen.blit(image, blit_pos)

    def update(self):
        pygame.display.flip(self.screen)
        self.screen.fill(self.background)