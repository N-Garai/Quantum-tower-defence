"""
Visual Effects System
Particle effects, animations, and visual feedback for quantum mechanics
"""

import pygame
import numpy as np
import math
from typing import List, Tuple
import time


class Particle:
    """Single particle for effects"""
    
    def __init__(self, x, y, vx, vy, color, lifetime, size=3):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.size = size
        self.gravity = 0.1
    
    def update(self, delta_time):
        """Update particle position"""
        self.x += self.vx * delta_time * 60
        self.y += self.vy * delta_time * 60
        self.vy += self.gravity
        self.lifetime -= delta_time
    
    def is_alive(self):
        """Check if particle is still alive"""
        return self.lifetime > 0
    
    def get_alpha(self):
        """Get transparency based on remaining lifetime"""
        return int(255 * (self.lifetime / self.max_lifetime))


class MeasurementEffect:
    """Visual effect for wave function collapse"""
    
    def __init__(self, position: Tuple[float, float], color: Tuple[int, int, int]):
        self.position = position
        self.color = color
        self.start_time = time.time()
        self.duration = 0.5  # seconds
        self.max_radius = 80

    def update(self, delta_time=0):
        """Update effect state"""
        elapsed = time.time() - self.start_time
        return elapsed < self.duration
    
    def render(self, screen):
        """Render measurement collapse effect"""
        elapsed = time.time() - self.start_time
        progress = min(1.0, elapsed / self.duration)
        
        # Expanding circle
        radius = int(self.max_radius * progress)
        alpha = int(255 * (1 - progress))
        
        # Create surface with alpha
        surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        
        # Draw multiple circles for glow effect
        for i in range(3):
            circle_radius = radius - i * 5
            if circle_radius > 0:
                circle_alpha = alpha // (i + 1)
                color_with_alpha = (*self.color, circle_alpha)
                pygame.draw.circle(surf, color_with_alpha, (radius, radius), circle_radius, 2)
        
        screen.blit(surf, (self.position[0] - radius, self.position[1] - radius))


class SuperpositionEffect:
    """Quantum superposition visual effect"""
    
    def __init__(self, positions: List[Tuple[float, float]], color: Tuple[int, int, int]):
        self.positions = positions
        self.color = color
        self.start_time = time.time()
        self.duration = 0.3
    
    def update(self):
        """Update effect state"""
        elapsed = time.time() - self.start_time
        return elapsed < self.duration
    
    def render(self, screen):
        """Render superposition shimmer"""
        elapsed = time.time() - self.start_time
        progress = min(1.0, elapsed / self.duration)
        
        alpha = int(128 * math.sin(progress * math.pi * 4))
        
        for pos in self.positions:
            surf = pygame.Surface((30, 30), pygame.SRCALPHA)
            color_with_alpha = (*self.color, abs(alpha))
            pygame.draw.circle(surf, color_with_alpha, (15, 15), 15)
            screen.blit(surf, (pos[0] - 15, pos[1] - 15))


class EntanglementEffect:
    """Visual effect for quantum entanglement"""
    
    def __init__(self, pos1: Tuple[float, float], pos2: Tuple[float, float], color: Tuple[int, int, int]):
        self.pos1 = pos1
        self.pos2 = pos2
        self.color = color
        self.start_time = time.time()
        self.duration = 0.4
        self.particles = []
        
        # Create particles along the line
        steps = 10
        for i in range(steps):
            t = i / steps
            x = pos1[0] + (pos2[0] - pos1[0]) * t
            y = pos1[1] + (pos2[1] - pos1[1]) * t
            angle = np.random.random() * math.pi * 2
            speed = 2
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            self.particles.append(Particle(x, y, vx, vy, color, 0.4, size=4))
    
    def update(self, delta_time):
        """Update effect state"""
        for particle in self.particles:
            particle.update(delta_time)
        
        elapsed = time.time() - self.start_time
        return elapsed < self.duration
    
    def render(self, screen):
        """Render entanglement particles"""
        for particle in self.particles:
            if particle.is_alive():
                alpha = particle.get_alpha()
                surf = pygame.Surface((particle.size * 2, particle.size * 2), pygame.SRCALPHA)
                color_with_alpha = (*particle.color, alpha)
                pygame.draw.circle(surf, color_with_alpha, (particle.size, particle.size), particle.size)
                screen.blit(surf, (int(particle.x) - particle.size, int(particle.y) - particle.size))


class DamageNumber:
    """Floating damage number"""
    
    def __init__(self, position: Tuple[float, float], damage: int, color: Tuple[int, int, int]):
        self.x = position[0]
        self.y = position[1]
        self.damage = damage
        self.color = color
        self.start_time = time.time()
        self.duration = 1.0
        self.vy = -2  # Float upward
    
    def update(self, delta_time):
        """Update position"""
        self.y += self.vy * delta_time * 60
        elapsed = time.time() - self.start_time
        return elapsed < self.duration
    
    def render(self, screen, font):
        """Render damage number"""
        elapsed = time.time() - self.start_time
        progress = elapsed / self.duration
        alpha = int(255 * (1 - progress))
        
        # Create text surface
        text = font.render(f"-{self.damage}", True, self.color)
        
        # Create surface with alpha
        surf = pygame.Surface(text.get_size(), pygame.SRCALPHA)
        surf.blit(text, (0, 0))
        surf.set_alpha(alpha)
        
        screen.blit(surf, (int(self.x) - 10, int(self.y)))


class PhaseShiftEffect:
    """Visual effect for phase manipulation"""
    
    def __init__(self, position: Tuple[float, float], target_path: int):
        self.position = position
        self.target_path = target_path
        self.start_time = time.time()
        self.duration = 0.3
        self.color = (255, 200, 100)

    def update(self, delta_time=0):
        """Update effect state"""
        elapsed = time.time() - self.start_time
        return elapsed < self.duration
    
    def render(self, screen):
        """Render phase shift ripple"""
        elapsed = time.time() - self.start_time
        progress = elapsed / self.duration
        
        # Rotating particles
        num_particles = 8
        radius = 30 + progress * 20
        
        for i in range(num_particles):
            angle = (i / num_particles) * math.pi * 2 + progress * math.pi * 4
            x = self.position[0] + math.cos(angle) * radius
            y = self.position[1] + math.sin(angle) * radius
            
            alpha = int(255 * (1 - progress))
            if alpha>0:
                surf = pygame.Surface((8, 8), pygame.SRCALPHA)
                color_with_alpha = (*self.color, alpha)
                pygame.draw.circle(surf, color_with_alpha, (4, 4), 4)
                screen.blit(surf, (int(x) - 4, int(y) - 4))


class TeleportationEffect:
    """Visual effect for quantum teleportation"""
    
    def __init__(self, start_pos: Tuple[float, float], end_pos: Tuple[float, float]):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.start_time = time.time()
        self.duration = 0.2
        self.color = (100, 255, 255)
    
    def update(self, delta_time=0):
        """Update effect state"""
        elapsed = time.time() - self.start_time
        return elapsed < self.duration
    
    def render(self, screen):
        """Render teleportation beam"""
        elapsed = time.time() - self.start_time
        progress = elapsed / self.duration
        
        # Lightning bolt effect
        steps = 8
        points = [self.start_pos]
        
        for i in range(1, steps):
            t = i / steps
            x = self.start_pos[0] + (self.end_pos[0] - self.start_pos[0]) * t
            y = self.start_pos[1] + (self.end_pos[1] - self.start_pos[1]) * t
            
            # Add randomness
            offset = 10 * math.sin(progress * math.pi)
            x += np.random.uniform(-offset, offset)
            y += np.random.uniform(-offset, offset)
            
            points.append((x, y))
        
        points.append(self.end_pos)
        
        # Draw the beam
        alpha = int(255 * (1 - progress))
        if len(points) >= 2:
            for i in range(len(points) - 1):
                surf = pygame.Surface((abs(points[i+1][0] - points[i][0]) + 10, 
                                     abs(points[i+1][1] - points[i][1]) + 10), pygame.SRCALPHA)
                color_with_alpha = (*self.color, alpha)
                pygame.draw.line(screen, color_with_alpha, points[i], points[i+1], 3)


class EffectsManager:
    """Manages all visual effects"""
    
    def __init__(self):
        self.effects = []
        self.damage_numbers = []
        self.font = pygame.font.Font(None, 20)
    
    def add_measurement_effect(self, position: Tuple[float, float], color=(100, 255, 100)):
        """Add wave function collapse effect"""
        self.effects.append(MeasurementEffect(position, color))
    
    def add_superposition_effect(self, positions: List[Tuple[float, float]], color=(100, 180, 255)):
        """Add superposition shimmer"""
        self.effects.append(SuperpositionEffect(positions, color))
    
    def add_entanglement_effect(self, pos1: Tuple[float, float], pos2: Tuple[float, float], 
                                color=(200, 100, 255)):
        """Add entanglement link effect"""
        self.effects.append(EntanglementEffect(pos1, pos2, color))
    
    def add_phase_shift_effect(self, position: Tuple[float, float], target_path: int):
        """Add phase manipulation effect"""
        self.effects.append(PhaseShiftEffect(position, target_path))
    
    def add_teleportation_effect(self, start_pos: Tuple[float, float], end_pos: Tuple[float, float]):
        """Add quantum teleportation beam"""
        self.effects.append(TeleportationEffect(start_pos, end_pos))
    
    def add_damage_number(self, position: Tuple[float, float], damage: int, color=(255, 100, 100)):
        """Add floating damage number"""
        self.damage_numbers.append(DamageNumber(position, damage, color))
    
    def update(self, delta_time: float):
        """Update all effects"""
        # Update and remove dead effects
        self.effects = [effect for effect in self.effects if effect.update(delta_time)]

        
        # Update damage numbers
        self.damage_numbers = [num for num in self.damage_numbers if num.update(delta_time)]
    
    def render(self, screen):
        """Render all effects"""
        for effect in self.effects:
            effect.render(screen)
        
        for num in self.damage_numbers:
            num.render(screen, self.font)
    
    def clear_all(self):
        """Clear all effects"""
        self.effects.clear()
        self.damage_numbers.clear()
