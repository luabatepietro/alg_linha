import pygame
import os
class Item(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        super().__init__()
        base_image_path = os.path.join(os.path.dirname(__file__), 'assets')
        self.image = pygame.image.load(os.path.join(base_image_path, 'cake.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))  # Redimensiona se necessário
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
