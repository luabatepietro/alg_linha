import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        super().__init__()
        self.image = pygame.image.load('images/cake.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))  # Redimensiona se necessário
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
