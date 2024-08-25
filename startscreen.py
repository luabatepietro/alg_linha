import pygame

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.SysFont(None, 74)
        self.font_instruction = pygame.font.SysFont(None, 36)
        self.title_text = self.font_title.render("Nyan Cat Maluco", True, (255, 255, 255))
        self.instruction_text = self.font_instruction.render("Pressione qualquer tecla para iniciar", True, (255, 255, 255))

    def show(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_text, (self.screen.get_width() // 2 - self.title_text.get_width() // 2, 150))
        self.screen.blit(self.instruction_text, (self.screen.get_width() // 2 - self.instruction_text.get_width() // 2, 300))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    waiting = False
