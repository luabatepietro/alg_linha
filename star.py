import pygame

class Star(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.image = pygame.image.load('images/planet_6.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))  # Redimensiona se necessário
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
