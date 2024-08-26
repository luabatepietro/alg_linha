import pygame
import os
class Item(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, base_image_path):
        super().__init__()
        self.image = pygame.image.load(os.path.join(base_image_path, 'cake.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))  # Redimensiona se necessário
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
