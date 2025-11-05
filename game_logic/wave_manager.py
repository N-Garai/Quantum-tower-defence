"""
Wave Manager - Handles enemy wave spawning and management
"""

import time
import logging
import numpy as np
from typing import List
from quantum_engine.enemy_superposition import EnemySpawner, EnemySuperposition, EntangledEnemyPair

logger = logging.getLogger(__name__)


class WaveManager:
    """Manages enemy waves and spawning"""
    
    def __init__(self, quantum_state_manager, wave_config, enemy_config):
        """
        Initialize wave manager
        
        Args:
            quantum_state_manager: Quantum state manager instance
            wave_config: Wave configuration list
            enemy_config: Enemy type configuration
        """
        self.spawner = EnemySpawner(quantum_state_manager)
        self.wave_config = wave_config
        self.enemy_config = enemy_config
        
        self.current_wave = -1
        self.enemies: List[EnemySuperposition] = []
        self.entangled_pairs: List[EntangledEnemyPair] = []
        self.spawn_queue = []
        self.last_spawn_time = 0
        self.wave_active = False
        self.wave_start_time = 0
        
        logger.info("Wave Manager initialized")
    
    def reset(self):
        """Reset wave manager"""
        self.current_wave = -1
        self.enemies.clear()
        self.entangled_pairs.clear()
        self.spawn_queue.clear()
        self.last_spawn_time = 0
        self.wave_active = False
        logger.info("Wave Manager reset")
    
    def start_wave(self, wave_number: int):
        """
        Start a new wave
        
        Args:
            wave_number: Wave number to start (0-indexed)
        """
        self.current_wave = wave_number
        
        # Get wave configuration (use last config for waves beyond defined ones)
        config_index = min(wave_number, len(self.wave_config) - 1)
        config = self.wave_config[config_index]
        
        # Build spawn queue
        self.spawn_queue = []
        for enemy_type, count in config['enemies']:
            for _ in range(count):
                self.spawn_queue.append(enemy_type)
        
        # Shuffle for variety
        np.random.shuffle(self.spawn_queue)
        
        self.wave_active = True
        self.wave_start_time = time.time()
        self.last_spawn_time = time.time()
        
        logger.info(f"Wave {wave_number + 1} started with {len(self.spawn_queue)} enemies")
    
    def update(self, delta_time: float, current_time: float) -> int:
        """
        Update wave state
        
        Args:
            delta_time: Time since last update (seconds)
            current_time: Current time
            
        Returns:
            0: Wave ongoing
            1: Wave completed
            -1: Enemy reached end (life lost)
        """
        if not self.wave_active:
            return 0
        
        # Spawn enemies from queue
        config_index = min(self.current_wave, len(self.wave_config) - 1)
        spawn_delay = self.wave_config[config_index]['spawn_delay']
        
        if self.spawn_queue and current_time - self.last_spawn_time >= spawn_delay:
            self.spawn_next_enemy(current_time)
            self.last_spawn_time = current_time
        
        # Update all enemies
        life_lost = False
        for enemy in self.enemies[:]:
            enemy.update_position(delta_time)
            
            # Check if dead
            if not enemy.is_alive():
                self.remove_enemy(enemy)
                continue
            
            # Check if reached end
            if enemy.is_at_end():
                self.remove_enemy(enemy)
                life_lost = True
        
        # Check wave completion
        if not self.spawn_queue and len(self.enemies) == 0:
            self.wave_active = False
            logger.info(f"Wave {self.current_wave + 1} completed")
            return 1
        
        if life_lost:
            return -1
        
        return 0
    
    def spawn_next_enemy(self, current_time: float):
        """
        Spawn the next enemy from queue
        
        Args:
            current_time: Current time
        """
        if not self.spawn_queue:
            return
        
        enemy_type = self.spawn_queue.pop(0)
        config = self.enemy_config[enemy_type]
        
        # 30% chance for entangled pair (if another enemy available)
        if np.random.random() < 0.3 and len(self.spawn_queue) > 0:
            # Spawn entangled pair
            enemy_type2 = self.spawn_queue.pop(0)
            config2 = self.enemy_config[enemy_type2]
            
            # Use average stats for pair
            avg_health = (config['health'] + config2['health']) / 2
            avg_speed = (config['speed'] + config2['speed']) / 2
            
            pair = self.spawner.spawn_entangled_pair(
                health=avg_health,
                speed=avg_speed,
                current_time=current_time
            )
            
            self.entangled_pairs.append(pair)
            self.enemies.extend([pair.enemy1, pair.enemy2])
            
            logger.debug(f"Spawned entangled pair: {enemy_type} + {enemy_type2}")
        else:
            # Spawn single enemy
            enemy = self.spawner.spawn_single_enemy(
                health=config['health'],
                speed=config['speed'],
                current_time=current_time
            )
            self.enemies.append(enemy)
            
            logger.debug(f"Spawned {enemy_type} enemy (ID: {enemy.enemy_id})")
    
    def remove_enemy(self, enemy: EnemySuperposition):
        """
        Remove enemy from game
        
        Args:
            enemy: Enemy to remove
        """
        if enemy in self.enemies:
            self.enemies.remove(enemy)
        
        # Remove from entangled pairs if applicable
        if enemy.is_entangled:
            for pair in self.entangled_pairs[:]:
                if pair.enemy1 == enemy or pair.enemy2 == enemy:
                    self.entangled_pairs.remove(pair)
                    
                    # Mark partner as no longer entangled
                    partner = pair.enemy2 if pair.enemy1 == enemy else pair.enemy1
                    partner.is_entangled = False
                    partner.entangled_partner_id = None
    
    def get_wave_multiplier(self) -> float:
        """
        Get reward multiplier for current wave
        
        Returns:
            Multiplier value
        """
        if self.current_wave < 0:
            return 1.0
        
        config_index = min(self.current_wave, len(self.wave_config) - 1)
        return self.wave_config[config_index]['reward_multiplier']
    
    def calculate_coherence_drain(self, delta_time: float) -> float:
        """
        Calculate quantum coherence drain from unmeasured enemies
        
        Args:
            delta_time: Time since last update (seconds)
            
        Returns:
            Total coherence drain
        """
        total_drain = 0.0
        
        for enemy in self.enemies:
            if not enemy.is_measured:
                # Get enemy type from health (approximate)
                coherence_cost = 0.5  # Default basic enemy
                if enemy.health >= 900:
                    coherence_cost = 1.0  # Boss
                elif enemy.health >= 250:
                    coherence_cost = 0.8  # Tank
                elif enemy.health <= 60:
                    coherence_cost = 0.3  # Fast
                
                total_drain += coherence_cost * delta_time
        
        return total_drain
    
    def get_enemy_by_id(self, enemy_id: int) -> EnemySuperposition:
        """
        Get enemy by ID
        
        Args:
            enemy_id: Enemy ID
            
        Returns:
            Enemy object or None
        """
        for enemy in self.enemies:
            if enemy.enemy_id == enemy_id:
                return enemy
        return None
    
    def get_enemies_in_range(self, position: tuple, range_dist: float) -> List[EnemySuperposition]:
        """
        Get all enemies within range of position
        
        Args:
            position: (x, y) position
            range_dist: Range distance
            
        Returns:
            List of enemies in range
        """
        from config.game_config import get_position_on_path
        
        in_range = []
        for enemy in self.enemies:
            # Check all possible paths for unmeasured enemies
            if enemy.is_measured:
                pos = get_position_on_path(enemy.measured_path, enemy.position_progress)
                distance = np.sqrt(
                    (pos[0] - position[0])**2 + (pos[1] - position[1])**2
                )
                if distance <= range_dist:
                    in_range.append(enemy)
            else:
                # Check each path with probability
                for path_idx in range(4):
                    pos = get_position_on_path(path_idx, enemy.position_progress)
                    distance = np.sqrt(
                        (pos[0] - position[0])**2 + (pos[1] - position[1])**2
                    )
                    if distance <= range_dist:
                        in_range.append(enemy)
                        break  # Only add once
        
        return in_range
