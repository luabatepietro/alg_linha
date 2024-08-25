import pygame
import numpy as np

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.image = pygame.image.load('images/asteroid.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))  # Redimensiona se necessário
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = np.random.choice([1, -1], size=2)
        self.speed = 3
        self.is_visible = True  # Novo atributo para indicar se o inimigo está ativo

    def hide(self):
        self.is_visible = False  # Marca o inimigo como "invisível" ou "estourado"
        self.rect.center = (-100, -100)  # Posiciona o inimigo fora da tela
