"""
UI Manager - User Interface Rendering and Interaction
Handles all UI elements, buttons, and player interactions
"""

import pygame
from config.game_config import *


class UIManager:
    """Manages all user interface elements and interactions"""
    
    def __init__(self, screen):
        """
        Initialize UI Manager
        
        Args:
            screen: Pygame screen surface
        """
        self.screen = screen
        
        # Load fonts
        try:
            self.font_large = pygame.font.Font(None, 28)
            self.font_medium = pygame.font.Font(None, 24)
            self.font_small = pygame.font.Font(None, 20)
            self.font_tiny = pygame.font.Font(None, 18)
        except:
            # Fallback to system fonts
            self.font_large = pygame.font.SysFont('arial', 28)
            self.font_medium = pygame.font.SysFont('arial', 24)
            self.font_small = pygame.font.SysFont('arial', 20)
            self.font_tiny = pygame.font.SysFont('arial', 18)
    
    def render_ui(self, resource_manager, selected_tower, wave_active, fps):
        """
        Render main game UI
        
        Args:
            resource_manager: Resource manager instance
            selected_tower: Currently selected tower type
            wave_active: Whether wave is currently active
            fps: Current frames per second
        """
        # Draw bottom UI panel
        panel_rect = pygame.Rect(0, SCREEN_HEIGHT - UI_PANEL_HEIGHT, SCREEN_WIDTH, UI_PANEL_HEIGHT)
        pygame.draw.rect(self.screen, COLORS['ui_panel'], panel_rect)
        
        # Draw panel border
        pygame.draw.rect(self.screen, COLORS['ui_text'], panel_rect, width=2)
        
        # === LEFT SECTION: Resources ===
        
        # Money
        money_text = self.font_medium.render(
            f"💰 ${resource_manager.money}",
            True,
            COLORS['ui_text']
        )
        self.screen.blit(money_text, (20, SCREEN_HEIGHT - 85))
        
        # Lives
        lives_color = COLORS['health_bar'] if resource_manager.lives > 5 else (255, 100, 100)
        lives_text = self.font_medium.render(
            f"❤️  {resource_manager.lives}",
            True,
            lives_color
        )
        self.screen.blit(lives_text, (20, SCREEN_HEIGHT - 55))
        
        # Quantum Coherence with bar
        coherence_text = self.font_small.render(
            f"⚛️  Coherence:",
            True,
            COLORS['quantum_coherence']
        )
        self.screen.blit(coherence_text, (180, SCREEN_HEIGHT - 85))
        
        # Coherence bar
        bar_width = 120
        bar_height = 18
        bar_x = 180
        bar_y = SCREEN_HEIGHT - 60
        
        # Background
        pygame.draw.rect(
            self.screen,
            (40, 40, 40),
            (bar_x, bar_y, bar_width, bar_height),
            border_radius=4
        )
        
        # Fill
        fill_width = int(bar_width * (resource_manager.quantum_coherence / resource_manager.max_coherence))
        if fill_width > 0:
            pygame.draw.rect(
                self.screen,
                COLORS['quantum_coherence'],
                (bar_x, bar_y, fill_width, bar_height),
                border_radius=4
            )
        
        # Border
        pygame.draw.rect(
            self.screen,
            COLORS['quantum_coherence'],
            (bar_x, bar_y, bar_width, bar_height),
            width=2,
            border_radius=4
        )
        
        # Coherence text
        coherence_value_text = self.font_tiny.render(
            f"{resource_manager.quantum_coherence:.1f}/{resource_manager.max_coherence}",
            True,
            COLORS['ui_text']
        )
        self.screen.blit(coherence_value_text, (bar_x + 5, bar_y + 2))
        
        # Wave number
        wave_text = self.font_small.render(
            f"🌊 Wave {resource_manager.wave}",
            True,
            COLORS['ui_text']
        )
        self.screen.blit(wave_text, (180, SCREEN_HEIGHT - 35))
        
        # === CENTER SECTION: Tower Selection ===
        
        tower_types = ['measurement', 'phase', 'entanglement', 'teleportation']
        tower_colors = [
            COLORS['tower_measurement'],
            COLORS['tower_phase'],
            COLORS['tower_entanglement'],
            COLORS['tower_teleportation']
        ]
        tower_icons = ['M', 'P', 'E', 'T']
        
        for i, (ttype, color, icon) in enumerate(zip(tower_types, tower_colors, tower_icons)):
            x = 380 + i * 115
            y = SCREEN_HEIGHT - 90
            
            # Button rectangle
            button_rect = pygame.Rect(x, y, 105, 80)
            
            # Determine button state
            is_selected = (selected_tower == ttype)
            can_afford = resource_manager.can_afford(TOWER_CONFIG[ttype]['cost'])
            
            # Button background
            if is_selected:
                button_color = COLORS['button_hover']
                border_width = 4
            elif can_afford:
                button_color = COLORS['button']
                border_width = 2
            else:
                button_color = (40, 40, 40)
                border_width = 2
            
            pygame.draw.rect(self.screen, button_color, button_rect, border_radius=8)
            
            # Button border (tower color)
            border_color = color if can_afford else (80, 80, 80)
            pygame.draw.rect(self.screen, border_color, button_rect, width=border_width, border_radius=8)
            
            # Tower icon (large letter)
            icon_color = color if can_afford else (100, 100, 100)
            icon_text = self.font_large.render(icon, True, icon_color)
            icon_rect = icon_text.get_rect(center=(x + 52, y + 22))
            self.screen.blit(icon_text, icon_rect)
            
            # Cost
            cost = TOWER_CONFIG[ttype]['cost']
            cost_color = COLORS['ui_text'] if can_afford else (150, 150, 150)
            cost_text = self.font_small.render(f"${cost}", True, cost_color)
            cost_rect = cost_text.get_rect(center=(x + 52, y + 48))
            self.screen.blit(cost_text, cost_rect)
            
            # Hotkey indicator
            hotkey_text = self.font_tiny.render(f"[{i+1}]", True, COLORS['quantum_coherence'])
            hotkey_rect = hotkey_text.get_rect(center=(x + 52, y + 68))
            self.screen.blit(hotkey_text, hotkey_rect)
        
        # === RIGHT SECTION: Controls ===
        
        # Wave start button (if wave not active)
        if not wave_active:
            wave_button_rect = pygame.Rect(SCREEN_WIDTH - 160, SCREEN_HEIGHT - 85, 140, 45)
            pygame.draw.rect(self.screen, (80, 180, 80), wave_button_rect, border_radius=10)
            pygame.draw.rect(self.screen, (100, 255, 100), wave_button_rect, width=3, border_radius=10)
            
            wave_button_text = self.font_medium.render("START WAVE", True, (0, 0, 0))
            wave_button_text_rect = wave_button_text.get_rect(center=wave_button_rect.center)
            self.screen.blit(wave_button_text, wave_button_text_rect)
            
            # Space key hint
            space_hint = self.font_tiny.render("[SPACE]", True, (200, 255, 200))
            space_hint_rect = space_hint.get_rect(center=(wave_button_rect.centerx, SCREEN_HEIGHT - 30))
            self.screen.blit(space_hint, space_hint_rect)
        
        # FPS counter
        fps_text = self.font_tiny.render(f"FPS: {int(fps)}", True, (150, 150, 150))
        self.screen.blit(fps_text, (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 95))
        
        # Score
        score_text = self.font_small.render(
            f"Score: {resource_manager.score}",
            True,
            COLORS['ui_text']
        )
        self.screen.blit(score_text, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 70))
    
    def handle_click(self, pos, game):
        """
        Handle mouse click on UI elements
        
        Args:
            pos: Mouse position (x, y)
            game: Main game instance
        """
        # Check if click is in UI panel
        if pos[1] < SCREEN_HEIGHT - UI_PANEL_HEIGHT:
            return  # Click is in game area, not UI
        
        # Tower button clicks
        tower_types = ['measurement', 'phase', 'entanglement', 'teleportation']
        for i, ttype in enumerate(tower_types):
            x = 380 + i * 115
            y = SCREEN_HEIGHT - 90
            button_rect = pygame.Rect(x, y, 105, 80)
            
            if button_rect.collidepoint(pos):
                # Check if can afford
                if game.resource_manager.can_afford(TOWER_CONFIG[ttype]['cost']):
                    game.selected_tower_type = ttype
                return
        
        # Wave start button click
        if not game.wave_manager.wave_active:
            wave_button_rect = pygame.Rect(SCREEN_WIDTH - 160, SCREEN_HEIGHT - 85, 140, 45)
            if wave_button_rect.collidepoint(pos):
                game.start_next_wave()
    
    def render_tutorial(self):
        """Render tutorial overlay"""
        # Create semi-transparent overlay
        overlay_width = 500
        overlay_height = 460
        overlay = pygame.Surface((overlay_width, overlay_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 230))
        
        # Border
        pygame.draw.rect(
            overlay,
            COLORS['quantum_coherence'],
            overlay.get_rect(),
            width=3,
            border_radius=10
        )
        
        # Tutorial content
        tutorial_lines = [
            ("🎮 QUANTUM TOWER DEFENSE", True, 20, COLORS['quantum_coherence']),
            ("", False, 12, COLORS['ui_text']),
            ("━━━ Controls ━━━", True, 16, COLORS['ui_text']),
            ("  1-4 Keys: Select tower type", False, 14, COLORS['ui_text']),
            ("  Mouse Click: Place tower", False, 14, COLORS['ui_text']),
            ("  Right Click: Select tower", False, 14, (255, 200, 100)),
            ("  DELETE/BACKSPACE: Remove tower (50% refund)", False, 14, (255, 200, 100)),
            ("  SPACE: Start wave", False, 14, COLORS['ui_text']),
            ("  ESC: Pause game", False, 14, COLORS['ui_text']),
            ("  T: Toggle this tutorial", False, 14, COLORS['ui_text']),
            ("  R: Restart (when game over)", False, 14, COLORS['ui_text']),
            ("", False, 12, COLORS['ui_text']),
            ("━━━ Quantum Mechanics ━━━", True, 16, COLORS['quantum_coherence']),
            ("  Unmeasured enemies exist in", False, 14, (100, 180, 255)),
            ("  SUPERPOSITION on all paths!", False, 14, (100, 180, 255)),
            ("", False, 8, COLORS['ui_text']),
            ("  Use Measurement Tower to", False, 14, (100, 255, 100)),
            ("  collapse superposition first!", False, 14, (100, 255, 100)),
            ("", False, 8, COLORS['ui_text']),
            ("  Entangled enemies share damage!", False, 14, (200, 100, 255)),
            ("  Phase towers shift probabilities!", False, 14, (255, 200, 100)),
        ]
        
        y = 20
        for text, is_bold, size, color in tutorial_lines:
            if text:
                font = pygame.font.Font(None, size)
                if is_bold:
                    font.set_bold(True)
                text_surface = font.render(text, True, color)
                overlay.blit(text_surface, (25, y))
            y += size + 6
        
        # Blit overlay to screen (top-right corner)
        self.screen.blit(overlay, (SCREEN_WIDTH - overlay_width - 20, 20))
    
    def render_tower_info(self, tower_type, mouse_pos):
        """
        Render tower information tooltip
        
        Args:
            tower_type: Type of tower
            mouse_pos: Mouse position for tooltip placement
        """
        if tower_type not in TOWER_CONFIG:
            return
        
        config = TOWER_CONFIG[tower_type]
        
        # Create tooltip
        tooltip_width = 220
        tooltip_height = 140
        tooltip = pygame.Surface((tooltip_width, tooltip_height), pygame.SRCALPHA)
        tooltip.fill((20, 20, 20, 240))
        
        # Border
        tower_colors = {
            'measurement': COLORS['tower_measurement'],
            'phase': COLORS['tower_phase'],
            'entanglement': COLORS['tower_entanglement'],
            'teleportation': COLORS['tower_teleportation']
        }
        border_color = tower_colors.get(tower_type, COLORS['ui_text'])
        pygame.draw.rect(tooltip, border_color, tooltip.get_rect(), width=2, border_radius=5)
        
        # Tower name
        name_text = self.font_medium.render(tower_type.upper(), True, border_color)
        tooltip.blit(name_text, (10, 10))
        
        # Stats
        stats = [
            f"Cost: ${config['cost']}",
            f"Damage: {config['damage']}",
            f"Range: {config['range']}",
            f"Speed: {config['attack_speed']}/s",
            f"",
            config['description']
        ]
        
        y = 40
        for stat in stats:
            stat_text = self.font_tiny.render(stat, True, COLORS['ui_text'])
            tooltip.blit(stat_text, (10, y))
            y += 18
        
        # Position tooltip near mouse
        tooltip_x = min(mouse_pos[0] + 15, SCREEN_WIDTH - tooltip_width - 10)
        tooltip_y = max(10, mouse_pos[1] - tooltip_height - 10)
        
        self.screen.blit(tooltip, (tooltip_x, tooltip_y))
