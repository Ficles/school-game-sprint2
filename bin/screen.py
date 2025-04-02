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

    def draw_sprite(self, name, pos, angle):
        image = self.sprites[name]
        rotated_image = pygame.transform.rotate(image, angle)
        blit_pos = [0, 0]
        blit_pos[0] = pos[0] - (rotated_image.get_width() / 2)
        blit_pos[1] = pos[1] - (rotated_image.get_height()/ 2)
        self.screen.blit(rotated_image, blit_pos)

    def update(self):
        pygame.display.flip()
        self.screen.fill(self.background)