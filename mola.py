import pygame
import os

class Mola(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, repulsion_constant: float, base_image_path: str, size: tuple = (64, 64)):
        super().__init__()  # Certifique-se de que o init da superclasse seja chamado
        self.frames = [
            pygame.transform.scale(
                pygame.image.load(os.path.join(base_image_path, f'mola{str(i)}.gif')).convert_alpha(),
                size
            )
            for i in range(1, 8)
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.repulsion_constant = repulsion_constant  # Constante de repulsão da mola
        self.animation_speed = 0.1  # Velocidade da animação
        self.time_since_last_frame = 0

    def update(self):
        self.time_since_last_frame += self.animation_speed
        if self.time_since_last_frame >= 1:
            self.time_since_last_frame = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
