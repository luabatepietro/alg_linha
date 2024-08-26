import pygame
import numpy as np

class Player(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, size: tuple = (100, 50)) -> None:
        super().__init__()
        self.frames = [
            pygame.transform.scale(
                pygame.image.load(f'assets/frame_{str(i).zfill(2)}_delay-0.07s.gif').convert_alpha(),
                size
            )
            for i in range(11)
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = np.zeros(2, dtype=np.float64)
        self.thrown = False
        self.dragging = False
        self.initial_pos = np.array([x, y], dtype=np.float64)
        self.max_pull_distance = 100  # Distância máxima que pode puxar
        self.trajectory_points = []
        self.paused = False
        self.force = 0  # Força de lançamento
        self.animation_speed = 0.1  # Velocidade da animação
        self.time_since_last_frame = 0

    def update(self, planet_pos, gravitational_constant, planet_radius):
        if self.thrown and not self.paused:
            direction_vector = np.array(planet_pos) - np.array(self.rect.center)
            distance_to_planet = np.linalg.norm(direction_vector)
            
            if distance_to_planet <= planet_radius and distance_to_planet > 0:  # Só aplica gravidade dentro do raio
                normalized_direction = direction_vector / distance_to_planet
                gravitational_force = normalized_direction * (gravitational_constant / distance_to_planet**2)
                self.velocity += gravitational_force
            
            self.rect.center += self.velocity

        self.time_since_last_frame += self.animation_speed
        if self.time_since_last_frame >= 1:
            self.time_since_last_frame = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

    def drag(self, mouse_pos):
        drag_vector = np.array(mouse_pos) - np.array(self.initial_pos)
        drag_distance = np.linalg.norm(drag_vector)
        
        if drag_distance > self.max_pull_distance:
            drag_vector = drag_vector / drag_distance * self.max_pull_distance
            drag_distance = self.max_pull_distance

        self.rect.center = self.initial_pos + drag_vector
        self.force = int((drag_distance / self.max_pull_distance) * 100)  # Calcula a força proporcional
        self.update_trajectory(drag_vector, drag_distance)

    def release(self, mouse_pos):
        drag_vector = np.array(self.initial_pos) - np.array(mouse_pos)
        drag_distance = np.linalg.norm(drag_vector)
        
        max_speed = 10
        speed = min(max_speed, drag_distance / self.max_pull_distance * max_speed)
        
        if drag_distance > 0:
            unit_drag_vector = drag_vector / drag_distance
            self.velocity = unit_drag_vector * speed
        
        self.thrown = True
        self.paused = False  # Certifica-se de que o personagem não está pausado
        self.update_trajectory()  # Atualiza a trajetória após o lançamento

    def apply_repulsion(self, repulsion_pos, repulsion_constant):
        direction_vector = np.array(self.rect.center) - np.array(repulsion_pos)
        distance_to_mola = np.linalg.norm(direction_vector)
        if distance_to_mola > 0:
            normalized_direction = direction_vector / distance_to_mola
            repulsion_force = normalized_direction * (repulsion_constant / (distance_to_mola**2))
            self.velocity += repulsion_force
            self.update_trajectory()  # Atualiza a trajetória após aplicar a repulsão

    def update_trajectory(self, drag_vector=None, drag_distance=None, repulsion_pos=None, repulsion_constant=None):
        self.trajectory_points = []

        if drag_vector is None:
            future_position = np.array(self.rect.center, dtype=np.float64)
            future_velocity = self.velocity.copy()
        else:
            future_position = np.array(self.initial_pos, dtype=np.float64)
            future_velocity = -drag_vector / np.linalg.norm(drag_vector) * 10  # Simula a velocidade inicial

        for _ in range(10):
            if repulsion_pos is not None and repulsion_constant is not None:
                direction_vector = np.array(future_position) - np.array(repulsion_pos)
                distance_to_mola = np.linalg.norm(direction_vector)
                if distance_to_mola > 0:
                    normalized_direction = direction_vector / distance_to_mola
                    repulsion_force = normalized_direction * (repulsion_constant / (distance_to_mola**2))
                    future_velocity += repulsion_force
            
            future_position += future_velocity * 5
            self.trajectory_points.append(future_position.copy())
            future_velocity *= 0.95  # Diminui a velocidade para simular resistência do ar

    def draw_trajectory(self, screen):
        for i, point in enumerate(self.trajectory_points):
            point_int = point.astype(int)
            radius = max(1, 5 - i)  # Diminui o tamanho das bolinhas
            color = (0, 128, 255) if i == 0 else (255, 255, 255)  # A primeira bolinha é azul, as outras são brancas
            pygame.draw.circle(screen, color, point_int, radius)

    def draw_force_bar(self, screen):
        bar_width = 100
        bar_height = 10
        bar_x = self.rect.centerx - bar_width // 2
        bar_y = self.rect.centery - 40

        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, self.force, bar_height))

    def check_boundaries(self, screen_width, screen_height):
        return (self.rect.right < 0 or self.rect.left > screen_width or
                self.rect.bottom < 0 or self.rect.top > screen_height)

    def can_be_clicked(self, mouse_pos):
        distance = np.linalg.norm(np.array(mouse_pos) - np.array(self.rect.center))
        return distance <= 20 
    
    def reset(self):
        self.rect.center = self.initial_pos  # Reposiciona o jogador na posição inicial
        self.velocity = np.zeros(2, dtype=np.float64)  # Reseta a velocidade
        self.thrown = False  # Reseta o status de lançamento
        self.paused = False  # Reseta o status de pausa
        self.trajectory_points = []  # Reseta a trajetória
        
    def stop(self):
        self.velocity = np.zeros(2, dtype=np.float64)
        self.paused = True