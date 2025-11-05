"""
Main Game Entry Point
Quantum Tower Defense - IBM Qiskit Educational Game
"""

import pygame
import sys
import logging
from pathlib import Path

# Import game modules
from quantum_engine.quantum_state import QuantumStateManager
from game_logic.resource_manager import ResourceManager
from game_logic.wave_manager import WaveManager
from game_logic.tower import TowerManager
from rendering.game_renderer import GameRenderer
from rendering.ui import UIManager
from config.game_config import *
from rendering.effects import EffectsManager

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('quantum_td.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class QuantumTowerDefense:
    """Main game class"""
    
    def __init__(self):
        """Initialize game systems"""
        logger.info("Initializing Quantum Tower Defense...")
        
        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()
        
        # Create display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Quantum Tower Defense - IBM Qiskit")
        
        # Set icon (if available)
        try:
            icon = pygame.image.load('assets/images/icon.png')
            pygame.display.set_icon(icon)
        except:
            logger.warning("Game icon not found, using default")
        
        # Initialize clock
        self.clock = pygame.time.Clock()
        
        # Initialize game systems
        self.quantum_manager = QuantumStateManager(NUM_PATHS)
        self.resource_manager = ResourceManager()
        self.tower_manager = TowerManager(self.quantum_manager)
        self.wave_manager = WaveManager(
            self.quantum_manager, 
            WAVE_CONFIG, 
            ENEMY_CONFIG
        )
        
        # Initialize rendering
        self.renderer = GameRenderer(self.screen)
        self.ui_manager = UIManager(self.screen)
        self.effects_manager = EffectsManager()
        # Game state
        self.game_state = "menu"  # menu, playing, paused, game_over, victory
        self.selected_tower_type = None
        self.selected_path_for_phase = 0
        self.mouse_pos = (0, 0)
        self.show_tutorial = True
        
        # Performance tracking
        self.frame_count = 0
        self.fps_history = []
        
        logger.info("Game initialized successfully")
    
    def run(self):
        """Main game loop"""
        logger.info("Starting game loop...")
        
        running = True
        while running:
            # Calculate delta time
            delta_time = self.clock.tick(FPS) / 1000.0
            self.frame_count += 1
            
            # Track FPS
            current_fps = self.clock.get_fps()
            self.fps_history.append(current_fps)
            if len(self.fps_history) > 60:
                self.fps_history.pop(0)
            
            # Handle events
            running = self.handle_events()
            
            # Update game state
            if self.game_state == "playing":
                self.update(delta_time)
            
            # Render
            self.render()
            
            # Update display
            pygame.display.flip()
        
        logger.info("Game loop ended")
        self.cleanup()
    
    def handle_events(self):
        """Handle all input events"""
        self.mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.game_state == "playing":
                        self.game_state = "paused"
                    elif self.game_state == "paused":
                        self.game_state = "playing"
                    elif self.game_state in ["menu", "game_over", "victory"]:
                        return False
                
                elif event.key == pygame.K_SPACE:
                    if self.game_state == "menu":
                        self.start_game()
                    elif self.game_state == "playing" and not self.wave_manager.wave_active:
                        self.start_next_wave()
                    elif self.game_state == "paused":
                        self.game_state = "playing"
                
                elif event.key == pygame.K_r:
                    if self.game_state in ["game_over", "victory"]:
                        self.restart_game()
                
                elif event.key == pygame.K_t:
                    self.show_tutorial = not self.show_tutorial
                
                # Tower selection hotkeys
                elif event.key == pygame.K_1:
                    self.selected_tower_type = "measurement"
                    logger.debug("Selected Measurement Tower")
                elif event.key == pygame.K_2:
                    self.selected_tower_type = "phase"
                    logger.debug("Selected Phase Tower")
                elif event.key == pygame.K_3:
                    self.selected_tower_type = "entanglement"
                    logger.debug("Selected Entanglement Tower")
                elif event.key == pygame.K_4:
                    self.selected_tower_type = "teleportation"
                    logger.debug("Selected Teleportation Tower")
                
                # Path selection for phase tower
                elif event.key in [pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3]:
                    if event.key == pygame.K_KP0:
                        self.selected_path_for_phase = 0
                    elif event.key == pygame.K_KP1:
                        self.selected_path_for_phase = 1
                    elif event.key == pygame.K_KP2:
                        self.selected_path_for_phase = 2
                    elif event.key == pygame.K_KP3:
                        self.selected_path_for_phase = 3
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.handle_mouse_click(event.pos)
                elif event.button == 3:  # Right click
                    self.selected_tower_type = None
        
        return True
    
    def handle_mouse_click(self, pos):
        """Handle mouse click events"""
        # Check if clicking on UI
        if pos[1] > SCREEN_HEIGHT - UI_PANEL_HEIGHT:
            # UI click - handle button presses
            self.ui_manager.handle_click(pos, self)
            return
        
        # Game area click - place tower
        if self.selected_tower_type and self.game_state == "playing":
            self.try_place_tower(pos)
    
    def try_place_tower(self, position):
        """Attempt to place a tower at position"""
        # Check if valid placement
        if not is_valid_tower_placement(position):
            logger.warning(f"Invalid tower placement at {position}")
            return
        
        # Check if can afford
        tower_cost = TOWER_CONFIG[self.selected_tower_type]['cost']
        if not self.resource_manager.can_afford(tower_cost):
            logger.warning(f"Cannot afford {self.selected_tower_type} tower (${tower_cost})")
            return
        
        # Place tower with appropriate parameters
        kwargs = {}
        if self.selected_tower_type == "phase":
            kwargs['target_path'] = self.selected_path_for_phase
        elif self.selected_tower_type == "teleportation":
            # Set target position to opposite side of map
            kwargs['target_position'] = (SCREEN_WIDTH - position[0], position[1])
        
        tower = self.tower_manager.place_tower(
            self.selected_tower_type, 
            position, 
            **kwargs
        )
        
        if tower:
            self.resource_manager.spend_money(tower_cost)
            logger.info(f"Placed {self.selected_tower_type} tower at {position}")
            # Don't deselect - allow multiple placements
    
    def start_game(self):
        """Start a new game"""
        logger.info("Starting new game")
        self.game_state = "playing"
        self.resource_manager.reset()
        self.tower_manager.clear_all_towers()
        self.wave_manager.reset()
        self.start_next_wave()
    
    def start_next_wave(self):
        """Start the next wave"""
        wave_num = self.resource_manager.wave
        logger.info(f"Starting wave {wave_num + 1}")
        self.wave_manager.start_wave(wave_num)
        self.resource_manager.wave += 1
    
    def restart_game(self):
        """Restart the game"""
        logger.info("Restarting game")
        self.start_game()
    
    def update(self, delta_time):
        """Update game state"""
        import time
        current_time = time.time()
        
        # Update wave manager
        result = self.wave_manager.update(delta_time, current_time)
        
        if result == -1:  # Enemy reached end
            self.resource_manager.lose_life()
            logger.info(f"Life lost! Lives remaining: {self.resource_manager.lives}")
            
            if self.resource_manager.lives <= 0:
                self.game_state = "game_over"
                logger.info("Game Over!")
        
        elif result == 1:  # Wave completed
            reward = int(100 * self.wave_manager.get_wave_multiplier())
            self.resource_manager.earn_money(reward)
            logger.info(f"Wave {self.resource_manager.wave - 1} completed! Earned ${reward}")
            
            # Check victory condition
            if self.resource_manager.wave > len(WAVE_CONFIG):
                self.game_state = "victory"
                logger.info("Victory! All waves completed!")
        
        # Update towers
        self.tower_manager.update_all_towers(
            self.wave_manager.enemies, 
            self.wave_manager.entangled_pairs,
            current_time
        )
        
        # Update resources
        self.resource_manager.regenerate_coherence(delta_time)
        
        # Calculate coherence drain from unmeasured enemies
        coherence_drain = self.wave_manager.calculate_coherence_drain(delta_time)
        self.resource_manager.consume_coherence(coherence_drain)
        # Update effects
        self.effects_manager.update(delta_time)
    
    def render(self):
        """Render game"""
        # Clear screen
        self.screen.fill(COLORS['background'])
        
        if self.game_state == "menu":
            self.renderer.render_menu()
        
        elif self.game_state in ["playing", "paused"]:
            # Render game elements
            self.renderer.render_paths()
            self.renderer.render_towers(self.tower_manager.towers)
            self.renderer.render_enemies(
                self.wave_manager.enemies,
                self.quantum_manager
            )
            self.renderer.render_entanglement_lines(
                self.wave_manager.entangled_pairs
            )
            # ADD EFFECTS 
            self.effects_manager.render(self.screen)
            # Render tower placement preview
            if self.selected_tower_type:
                self.renderer.render_tower_preview(
                    self.mouse_pos,
                    self.selected_tower_type,
                    is_valid_tower_placement(self.mouse_pos)
                )
            
            # Render UI
            self.ui_manager.render_ui(
                self.resource_manager,
                self.selected_tower_type,
                self.wave_manager.wave_active,
                sum(self.fps_history) / len(self.fps_history) if self.fps_history else 60
            )
            
            # Render tutorial
            if self.show_tutorial:
                self.ui_manager.render_tutorial()
            
            # Render pause overlay
            if self.game_state == "paused":
                self.renderer.render_pause_overlay()
        
        elif self.game_state == "game_over":
            self.renderer.render_game_over(self.resource_manager)
        
        elif self.game_state == "victory":
            self.renderer.render_victory(self.resource_manager)
    
    def cleanup(self):
        """Cleanup resources"""
        logger.info("Cleaning up resources...")
        pygame.quit()
        logger.info("Quantum Tower Defense shut down successfully")


def main():
    """Entry point"""
    try:
        game = QuantumTowerDefense()
        game.run()
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        pygame.quit()
        sys.exit(1)


if __name__ == "__main__":
    main()
