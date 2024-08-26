import pygame
import numpy as np
from alg_linha.player import Player
from alg_linha.mola import Mola
from alg_linha.inimigo import Inimigo
from alg_linha.item import Item
from alg_linha.star import Star
from alg_linha.startscreen import StartScreen  
from alg_linha.telafinal import VictoryScreen
from alg_linha.gmover import GameOverScreen
import os

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Nyan cat maluco")
        self.clock = pygame.time.Clock()
        self.running = True
        self.slow_motion = False
        self.camera_shake = 0
        self.lives = 3  # Adiciona um contador de vidas

        self.base_image_path = os.path.join(os.path.dirname(__file__), 'assets')  # Armazene o caminho da pasta de imagens

        self.player = Player(100, 100, size=(100, 50), base_image_path=self.base_image_path)
        self.heart_full = pygame.image.load(os.path.join(self.base_image_path, 'coracao.gif')).convert_alpha()
        self.heart_full = pygame.transform.scale(self.heart_full, (32, 32)) 
        self.heart_empty = pygame.image.load(os.path.join(self.base_image_path, 'coracao1.gif')).convert_alpha()
        self.heart_empty = pygame.transform.scale(self.heart_empty, (32, 32)) 

        # Lista de inimigos
        self.enemies = [
            Inimigo(100, 500, self.base_image_path),
            Inimigo(300, 200, self.base_image_path),
            Inimigo(600, 400, self.base_image_path)
        ]

        self.yellow_square = Item(100, 300, self.base_image_path)
        self.planet_pos = (400, 300)
        self.planet_radius = 150  # Raio de influência do planeta
        self.gravitational_constant = 3000  # Constante gravitacional para o planeta
        self.repulsion_mola = Mola(100, 400, 3000, self.base_image_path)
        self.counter = 0
        self.can_relaunch = False
        self.yellow_square_collected = False

        self.star = Star(self.planet_pos[0], self.planet_pos[1], self.base_image_path)
        self.start_screen = StartScreen(self.screen, os.path.join(self.base_image_path, 'backgo.webp'))  # Adiciona o caminho da imagem de fundo
        self.victory_screen = VictoryScreen(self.screen, os.path.join(self.base_image_path, 'final.webp'))  # Instancia a tela de vitória
        self.game_over_screen = GameOverScreen(self.screen, os.path.join(self.base_image_path, 'gameover.webp'))  # Adiciona a tela de Game Over


    def reset(self):
        # Use o caminho armazenado em vez de redefinir o caminho
        self.player = Player(100, 100, size=(100, 50), base_image_path=self.base_image_path)
        
        # Reinicializa a lista de inimigos
        self.enemies = [
            Inimigo(100, 500, self.base_image_path),
            Inimigo(300, 200, self.base_image_path),
            Inimigo(600, 400, self.base_image_path)
        ]
        
        self.counter = 0
        self.can_relaunch = False
        self.yellow_square_collected = False
        self.lives = 3  # Reinicia as vidas

    def run(self):
        self.start_screen.show()  # Mostra a tela de início

        while self.running:
            self.clock.tick(30 if self.slow_motion else 60)
            self.events()
            self.update()

            if self.lives <= 0:  # Verifica se o jogador perdeu todas as vidas
                result = self.game_over_screen.show()  # Mostra a tela de Game Over
                if result == "restart":
                    self.reset()  # Reinicia o jogo
                else:
                    self.running = False 

            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.player.thrown:
                self.player.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP and self.player.dragging:
                self.player.dragging = False
                self.camera_shake = 10
                self.player.release(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEMOTION and (self.player.dragging or self.slow_motion):
                self.player.drag(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONDOWN and self.player.thrown and self.can_relaunch:
                if self.player.can_be_clicked(pygame.mouse.get_pos()):
                    self.slow_motion = True
                    self.player.initial_pos = np.array(self.player.rect.center)
                    self.player.stop()

            elif event.type == pygame.MOUSEBUTTONUP and self.slow_motion:
                self.slow_motion = False
                self.camera_shake = 10
                self.player.release(pygame.mouse.get_pos())

    def update(self):
        if self.player.thrown:
            self.player.update(self.planet_pos, self.gravitational_constant, self.planet_radius)

            if self.player.check_boundaries(self.screen.get_width(), self.screen.get_height()):
                self.lives -= 1  
                if self.lives > 0:
                    self.player.reset() 
                else:
                    self.reset()  

            for enemy in self.enemies:
                if self.player.rect.colliderect(enemy.rect):
                    print("Inimigo estourado!")
                    enemy.hide()
                if all(not enemy.is_visible for enemy in self.enemies):
                    self.victory_screen.show()

            if not self.yellow_square_collected and self.player.rect.colliderect(self.yellow_square.rect):
                self.counter += 1
                self.can_relaunch = True
                self.yellow_square_collected = True
                print(f"Contador: {self.counter}")

        for enemy in self.enemies:
            enemy.update(self.screen.get_width(), self.screen.get_height())
        
        self.star.update()

    def draw(self):
        self.background = pygame.image.load(os.path.join(self.base_image_path, 'fundo.png')).convert_alpha()
        self.screen.blit(self.background, (0, 0))

        if self.camera_shake > 0:
            shake_offset = np.random.randint(-5, 5, size=2)
            self.camera_shake -= 1
        else:
            shake_offset = np.array([0, 0])

        if self.player.rect.colliderect(self.repulsion_mola.rect):
            self.player.apply_repulsion(self.repulsion_mola.rect.center, self.repulsion_mola.repulsion_constant)
            self.mola = Mola.update(self.repulsion_mola)

        # Desenhe o perímetro branco ao redor do planeta
        pygame.draw.circle(self.screen, (255, 255, 255), self.planet_pos + shake_offset, self.planet_radius, 1)

        self.screen.blit(self.star.image, self.star.rect.move(shake_offset))
        self.screen.blit(self.player.image, self.player.rect.move(shake_offset))

        if not self.player.thrown or self.slow_motion or (self.can_relaunch and self.player.can_be_clicked(pygame.mouse.get_pos())):
            self.player.draw_trajectory(self.screen)
            if self.player.dragging:
                self.player.draw_force_bar(self.screen)

        if not self.yellow_square_collected:
            self.screen.blit(self.yellow_square.image, self.yellow_square.rect.move(shake_offset))

        for enemy in self.enemies:
            self.screen.blit(enemy.image, enemy.rect.move(shake_offset))

        self.screen.blit(self.repulsion_mola.image, self.repulsion_mola.rect.move(shake_offset))

        font = pygame.font.SysFont(None, 36)
        text = font.render(f"Counter: {self.counter}", True, (255, 255, 255))
        self.screen.blit(text, (600, 20))
        
        heart_x_start = 10 
        heart_y = 10  
        heart_spacing = 30 

        for i in range(3):  
            if i < self.lives:
                self.screen.blit(self.heart_full, (heart_x_start + i * heart_spacing, heart_y))  
            else:
                self.screen.blit(self.heart_empty, (heart_x_start + i * heart_spacing, heart_y))  

        pygame.display.flip()
    
    def quit(self):
        pygame.quit()
