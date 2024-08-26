import pygame
import os

class GameOverScreen:
    def __init__(self, screen, background_image_path):
        self.screen = screen
        self.background_image = pygame.image.load(background_image_path)

    def show(self):
        background = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))

        self.screen.blit(background, (0, 0))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_r:
                        waiting = False  
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        exit()
        return "restart"