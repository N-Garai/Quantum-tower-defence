"""
Game Renderer - Main rendering system
"""

import pygame
import numpy as np
import logging
from config.game_config import *

logger = logging.getLogger(__name__)


class GameRenderer:
    """Handles all game rendering"""
    
    def __init__(self, screen):
        """
        Initialize renderer
        
        Args:
            screen: Pygame screen surface
        """
        self.screen = screen
        
        # Load fonts
        try:
            self.font_small = pygame.font.Font(None, 20)
            self.font_medium = pygame.font.Font(None, 28)
            self.font_large = pygame.font.Font(None, 48)
            self.font_title = pygame.font.Font(None, 72)
        except:
            logger.warning("Failed to load custom fonts, using default")
            self.font_small = pygame.font.SysFont('arial', 20)
            self.font_medium = pygame.font.SysFont('arial', 28)
            self.font_large = pygame.font.SysFont('arial', 48)
            self.font_title = pygame.font.SysFont('arial', 72)
        
        logger.info("Game Renderer initialized")
    
    def render_paths(self):
        """Render all enemy paths"""
        for i, path in enumerate(PATHS):
            # Draw path line
            pygame.draw.lines(
                self.screen,
                COLORS['path'],
                False,
                path,
                4
            )
            
            # Draw path number at start
            text = self.font_small.render(f"Path {i}", True, COLORS['ui_text'])
            self.screen.blit(text, (path[0][0] + 10, path[0][1] - 20))
    
    def render_enemies(self, enemies, quantum_manager):
        """
        Render all enemies
        
        Args:
            enemies: List of enemy objects
            quantum_manager: Quantum state manager
        """
        for enemy in enemies:
            self.render_single_enemy(enemy, quantum_manager)
    
    def render_single_enemy(self, enemy, quantum_manager):
        """
        Render a single enemy
        
        Args:
            enemy: Enemy object
            quantum_manager: Quantum state manager
        """
        if enemy.is_measured:
            # Render solid enemy on measured path
            pos = get_position_on_path(enemy.measured_path, enemy.position_progress)
            
            # Choose color based on entanglement
            if enemy.is_entangled:
                color = COLORS['enemy_entangled']
            else:
                color = COLORS['enemy_measured']
            
            # Draw enemy circle
            pygame.draw.circle(
                self.screen,
                color,
                (int(pos[0]), int(pos[1])),
                15
            )
            
            # Draw border
            pygame.draw.circle(
                self.screen,
                (255, 255, 255),
                (int(pos[0]), int(pos[1])),
                15,
                2
            )
            
            # Draw health bar
            self.draw_health_bar(pos, enemy.health, 100)
        else:
            # Render semi-transparent on all paths with probabilities
            paths = enemy.get_active_paths(quantum_manager)
            
            for path_idx, prob in paths:
                if prob < 0.01:  # Skip very low probabilities
                    continue
                
                pos = get_position_on_path(path_idx, enemy.position_progress)
                
                # Create alpha surface for transparency
                alpha = int(prob * 255)
                s = pygame.Surface((32, 32), pygame.SRCALPHA)
                
                # Draw semi-transparent circle
                color = (*COLORS['enemy_superposition'][:3], alpha)
                pygame.draw.circle(s, color, (16, 16), 15)
                
                # Draw border
                border_color = (*COLORS['ui_text'], min(255, alpha + 50))
                pygame.draw.circle(s, border_color, (16, 16), 15, 2)
                
                # Blit to screen
                self.screen.blit(s, (int(pos[0]) - 16, int(pos[1]) - 16))
                
                # Show probability
                prob_text = self.font_small.render(
                    f"{int(prob*100)}%",
                    True,
                    COLORS['ui_text']
                )
                self.screen.blit(
                    prob_text,
                    (int(pos[0]) - 15, int(pos[1]) - 30)
                )
    
    def draw_health_bar(self, pos, current_health, max_health):
        """
        Draw enemy health bar
        
        Args:
            pos: (x, y) position
            current_health: Current health
            max_health: Maximum health
        """
        bar_width = 30
        bar_height = 4
        health_ratio = max(0, current_health / max_health)
        fill_width = int(bar_width * health_ratio)
        
        # Background
        pygame.draw.rect(
            self.screen,
            (50, 50, 50),
            (pos[0] - bar_width//2, pos[1] - 22, bar_width, bar_height)
        )
        
        # Health fill
        if fill_width > 0:
            pygame.draw.rect(
                self.screen,
                COLORS['health_bar'],
                (pos[0] - bar_width//2, pos[1] - 22, fill_width, bar_height)
            )
    
    def render_towers(self, towers):
        """
        Render all towers
        
        Args:
            towers: List of tower objects
        """
        for tower in towers:
            self.render_single_tower(tower)
    
    def render_single_tower(self, tower):
        """
        Render a single tower
        
        Args:
            tower: Tower object
        """
        # Get tower color
        color_map = {
            'measurement': COLORS['tower_measurement'],
            'phase': COLORS['tower_phase'],
            'entanglement': COLORS['tower_entanglement'],
            'teleportation': COLORS['tower_teleportation']
        }
        color = color_map.get(tower.tower_type, (255, 255, 255))
        
        # Draw tower base
        tower_rect = pygame.Rect(
            tower.position[0] - 20,
            tower.position[1] - 20,
            40,
            40
        )
        pygame.draw.rect(self.screen, color, tower_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), tower_rect, 2)
        
        # Draw range circle (semi-transparent)
        range_surface = pygame.Surface((int(tower.range * 2), int(tower.range * 2)), pygame.SRCALPHA)
        pygame.draw.circle(
            range_surface,
            (*color, 30),
            (int(tower.range), int(tower.range)),
            int(tower.range)
        )
        self.screen.blit(
            range_surface,
            (tower.position[0] - tower.range, tower.position[1] - tower.range)
        )
        
        # Draw tower type icon/letter
        icon_text = self.font_medium.render(
            tower.tower_type[0].upper(),
            True,
            (0, 0, 0)
        )
        icon_rect = icon_text.get_rect(center=tower.position)
        self.screen.blit(icon_text, icon_rect)
    
    def render_tower_preview(self, mouse_pos, tower_type, is_valid):
        """
        Render tower placement preview
        
        Args:
            mouse_pos: Mouse position
            tower_type: Type of tower being placed
            is_valid: Whether placement is valid
        """
        color_map = {
            'measurement': COLORS['tower_measurement'],
            'phase': COLORS['tower_phase'],
            'entanglement': COLORS['tower_entanglement'],
            'teleportation': COLORS['tower_teleportation']
        }
        color = color_map.get(tower_type, (255, 255, 255))
        
        # Adjust color based on validity
        if not is_valid:
            color = (255, 50, 50)  # Red for invalid
        
        # Draw preview
        preview_rect = pygame.Rect(
            mouse_pos[0] - 20,
            mouse_pos[1] - 20,
            40,
            40
        )
        
        s = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.rect(s, (*color, 128), (0, 0, 40, 40))
        pygame.draw.rect(s, (*color, 255), (0, 0, 40, 40), 2)
        
        self.screen.blit(s, preview_rect)
        
        # Draw range circle
        tower_range = TOWER_CONFIG[tower_type]['range']
        range_surface = pygame.Surface((int(tower_range * 2), int(tower_range * 2)), pygame.SRCALPHA)
        pygame.draw.circle(
            range_surface,
            (*color, 50),
            (int(tower_range), int(tower_range)),
            int(tower_range),
            2
        )
        self.screen.blit(
            range_surface,
            (mouse_pos[0] - tower_range, mouse_pos[1] - tower_range)
        )
    
    def render_entanglement_lines(self, entangled_pairs):
        """
        Render lines connecting entangled enemies
        
        Args:
            entangled_pairs: List of entangled enemy pairs
        """
        for pair in entangled_pairs:
            if pair.enemy1.is_measured and pair.enemy2.is_measured:
                pos1 = get_position_on_path(
                    pair.enemy1.measured_path,
                    pair.enemy1.position_progress
                )
                pos2 = get_position_on_path(
                    pair.enemy2.measured_path,
                    pair.enemy2.position_progress
                )
                
                # Draw wavy entanglement line
                pygame.draw.line(
                    self.screen,
                    COLORS['enemy_entangled'],
                    pos1,
                    pos2,
                    3
                )
    
    def render_menu(self):
        """Render main menu"""
        # Title
        title_text = self.font_title.render(
            "Quantum Tower Defense",
            True,
            COLORS['ui_text']
        )
        title_rect = title_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        )
        self.screen.blit(title_text, title_rect)
        
        # Subtitle
        subtitle_text = self.font_medium.render(
            "IBM Qiskit Educational Game",
            True,
            COLORS['quantum_coherence']
        )
        subtitle_rect = subtitle_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 60)
        )
        self.screen.blit(subtitle_text, subtitle_rect)
        
        # Instructions
        instructions = [
            "Press SPACE to Start",
            "",
            "Keys 1-4: Select Tower Type",
            "Mouse Click: Place Tower",
            "SPACE: Start Wave",
            "ESC: Pause/Quit"
        ]
        
        y_offset = SCREEN_HEIGHT // 2 + 50
        for instruction in instructions:
            text = self.font_medium.render(instruction, True, COLORS['ui_text'])
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 40
    
    def render_pause_overlay(self):
        """Render pause overlay"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = self.font_large.render("PAUSED", True, COLORS['ui_text'])
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(pause_text, pause_rect)
        
        # Resume instruction
        resume_text = self.font_medium.render(
            "Press ESC or SPACE to Resume",
            True,
            COLORS['quantum_coherence']
        )
        resume_rect = resume_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
        )
        self.screen.blit(resume_text, resume_rect)
    
    def render_game_over(self, resource_manager):
        """Render game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))
        
        # Game Over text
        game_over_text = self.font_large.render("GAME OVER", True, (255, 100, 100))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(game_over_text, game_over_rect)
        
        # Statistics
        stats = [
            f"Wave Reached: {resource_manager.wave}",
            f"Enemies Killed: {resource_manager.enemies_killed}",
            f"Final Score: {resource_manager.score}",
            "",
            "Press R to Restart",
            "Press ESC to Quit"
        ]
        
        y_offset = SCREEN_HEIGHT // 2
        for stat in stats:
            text = self.font_medium.render(stat, True, COLORS['ui_text'])
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 40
    
    def render_victory(self, resource_manager):
        """Render victory screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))
        
        # Victory text
        victory_text = self.font_large.render("VICTORY!", True, COLORS['tower_measurement'])
        victory_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(victory_text, victory_rect)
        
        # Statistics
        stats = [
            f"All Waves Completed!",
            f"Enemies Killed: {resource_manager.enemies_killed}",
            f"Final Score: {resource_manager.score}",
            f"Lives Remaining: {resource_manager.lives}",
            "",
            "Press R to Play Again",
            "Press ESC to Quit"
        ]
        
        y_offset = SCREEN_HEIGHT // 2
        for stat in stats:
            text = self.font_medium.render(stat, True, COLORS['ui_text'])
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 40
