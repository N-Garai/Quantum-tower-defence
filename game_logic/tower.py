"""
Tower System - Measurement towers and quantum effects
"""

from dataclasses import dataclass
from typing import List, Tuple, Optional
import numpy as np
from qiskit import QuantumCircuit
import logging

logger = logging.getLogger(__name__)


@dataclass
class Tower:
    """Base tower class"""
    
    tower_id: int
    tower_type: str
    position: Tuple[float, float]
    range: float
    damage: float
    attack_speed: float  # Attacks per second
    cost: int
    last_attack_time: float
    
    def can_attack(self, current_time: float) -> bool:
        """Check if tower can attack based on attack speed"""
        return (current_time - self.last_attack_time) >= (1.0 / self.attack_speed)
    
    def update_attack_time(self, current_time: float):
        """Update last attack time"""
        self.last_attack_time = current_time


class MeasurementTower(Tower):
    """
    Measurement tower - collapses enemy superposition
    """
    
    def __init__(self, tower_id: int, position: Tuple[float, float]):
        super().__init__(
            tower_id=tower_id,
            tower_type="measurement",
            position=position,
            range=150.0,
            damage=20.0,
            attack_speed=1.0,
            cost=100,
            last_attack_time=0.0
        )
        self.collapse_preference = None  # Which path to bias measurement toward
    
    def measure_enemy(self, enemy, quantum_state_manager, current_time: float) -> Optional[int]:
        """
        Measure enemy and collapse its superposition
        
        Args:
            enemy: EnemySuperposition object
            quantum_state_manager: Quantum state manager
            current_time: Current game time
            
        Returns:
            Measured path index or None if already measured
        """
        if not self.can_attack(current_time):
            return None
        
        if enemy.is_measured:
            return enemy.measured_path
        
        # Perform quantum measurement
        measured_path = quantum_state_manager.measure_path(enemy.quantum_circuit)
        enemy.collapse_to_path(measured_path)
        
        self.update_attack_time(current_time)
        return measured_path
    
    def attack_measured_enemy(self, enemy, current_time: float) -> float:
        """
        Attack enemy on collapsed path
        
        Returns:
            Damage dealt
        """
        if not self.can_attack(current_time):
            return 0.0
        
        if not enemy.is_measured:
            return 0.0
        
        damage_dealt = enemy.take_damage(self.damage)
        self.update_attack_time(current_time)
        return damage_dealt


class PhaseTower(Tower):
    """
    Phase tower - applies quantum phase to specific paths
    Reduces probability of enemy being on targeted path
    """
    
    def __init__(self, tower_id: int, position: Tuple[float, float], target_path: int):
        super().__init__(
            tower_id=tower_id,
            tower_type="phase",
            position=position,
            range=120.0,
            damage=0.0,  # Doesn't deal direct damage
            attack_speed=0.5,
            cost=150,
            last_attack_time=0.0
        )
        self.target_path = target_path
        self.phase_angle = np.pi / 4  # 45 degrees
    
    def apply_phase_shift(self, enemy, quantum_state_manager, current_time: float):
        """
        Apply phase gate to reduce probability on target path
        """
        if not self.can_attack(current_time):
            return
        
        if enemy.is_measured:
            return  # Can't affect measured enemies
        
        # Apply phase rotation to target path
        enemy.quantum_circuit = quantum_state_manager.apply_phase_gate(
            enemy.quantum_circuit,
            self.target_path,
            self.phase_angle
        )
        
        self.update_attack_time(current_time)


class EntanglementTower(Tower):
    """
    Entanglement tower - creates damage correlation between nearby enemies
    """
    
    def __init__(self, tower_id: int, position: Tuple[float, float]):
        super().__init__(
            tower_id=tower_id,
            tower_type="entanglement",
            position=position,
            range=100.0,
            damage=15.0,
            attack_speed=0.75,
            cost=200,
            last_attack_time=0.0
        )
    
    def create_entanglement(self, enemy1, enemy2, quantum_state_manager):
        """
        Create entanglement between two enemies (if not already entangled)
        """
        if enemy1.is_entangled or enemy2.is_entangled:
            return None
        
        # Create entangled state
        entangled_qc = quantum_state_manager.create_entangled_pair()
        
        # Link enemies
        enemy1.is_entangled = True
        enemy1.entangled_partner_id = enemy2.enemy_id
        enemy2.is_entangled = True
        enemy2.entangled_partner_id = enemy1.enemy_id
        
        return entangled_qc


class TeleportationTower(Tower):
    """
    Teleportation tower - instantly moves attack effects across map
    Uses quantum teleportation protocol
    """
    
    def __init__(self, tower_id: int, position: Tuple[float, float],
                 target_position: Tuple[float, float]):
        super().__init__(
            tower_id=tower_id,
            tower_type="teleportation",
            position=position,
            range=80.0,
            damage=30.0,
            attack_speed=0.5,
            cost=250,
            last_attack_time=0.0
        )
        self.target_position = target_position  # Where damage appears
        self.teleport_range = 100.0  # Range at target position
    
    def teleport_attack(self, enemy, current_time: float) -> float:
        """
        Attack enemy through quantum teleportation
        Damage appears at target_position instead of tower position
        """
        if not self.can_attack(current_time):
            return 0.0
        
        # Check if enemy is in range of TARGET position
        enemy_pos = self.get_enemy_position(enemy)
        if enemy_pos is None:
            return 0.0
        
        distance = np.sqrt(
            (enemy_pos[0] - self.target_position[0])**2 +
            (enemy_pos[1] - self.target_position[1])**2
        )
        
        if distance <= self.teleport_range:
            damage_dealt = enemy.take_damage(self.damage)
            self.update_attack_time(current_time)
            return damage_dealt
        
        return 0.0
    
    def get_enemy_position(self, enemy) -> Optional[Tuple[float, float]]:
        """Get enemy position (simplified)"""
        # In full implementation, this would calculate from path and progress
        return (0, 0)  # Placeholder


class TowerManager:
    """Manages all towers in the game"""
    
    def __init__(self, quantum_state_manager):
        self.towers: List[Tower] = []
        self.quantum_state_manager = quantum_state_manager
        self.next_tower_id = 0
    
    def place_tower(self, tower_type: str, position: Tuple[float, float],
                    **kwargs) -> Optional[Tower]:
        """
        Place a new tower
        
        Args:
            tower_type: Type of tower
            position: (x, y) position
            **kwargs: Additional tower-specific arguments
            
        Returns:
            Tower object or None if placement failed
        """
        tower = None
        
        if tower_type == "measurement":
            tower = MeasurementTower(self.next_tower_id, position)
        elif tower_type == "phase":
            target_path = kwargs.get("target_path", 0)
            tower = PhaseTower(self.next_tower_id, position, target_path)
        elif tower_type == "entanglement":
            tower = EntanglementTower(self.next_tower_id, position)
        elif tower_type == "teleportation":
            target_pos = kwargs.get("target_position", (0, 0))
            tower = TeleportationTower(self.next_tower_id, position, target_pos)
        
        if tower:
            self.towers.append(tower)
            self.next_tower_id += 1
            return tower
        
        return None
    
    def remove_tower(self, tower_id: int):
        """Remove a tower"""
        self.towers = [t for t in self.towers if t.tower_id != tower_id]
    
    def clear_all_towers(self):
        """Remove all towers from the game"""
        self.towers.clear()
        self.next_tower_id = 0
        logger.info("All towers cleared")
    
    def get_towers_in_range(self, position: Tuple[float, float]) -> List[Tower]:
        """Get all towers that can reach a position"""
        in_range = []
        for tower in self.towers:
            distance = np.sqrt(
                (tower.position[0] - position[0])**2 +
                (tower.position[1] - position[1])**2
            )
            if distance <= tower.range:
                in_range.append(tower)
        return in_range
    
    def update_all_towers(self, enemies: List, entangled_pairs: List, current_time: float, effects_manager=None):
        """
        Update all towers and execute attacks
        
        Args:
            enemies: List of active enemies
            entangled_pairs: List of entangled enemy pairs
            current_time: Current game time
            effects_manager: Visual effects manager (optional)
        """
        for tower in self.towers:
            # Find enemies in range
            targets = self.find_targets_in_range(tower, enemies)
            
            if tower.tower_type == "measurement":
                self.handle_measurement_tower(tower, targets, current_time, effects_manager)
            elif tower.tower_type == "phase":
                self.handle_phase_tower(tower, targets, current_time, effects_manager)
            elif tower.tower_type == "entanglement":
                self.handle_entanglement_tower(tower, targets, effects_manager)
            elif tower.tower_type == "teleportation":
                self.handle_teleportation_tower(tower, targets, current_time, effects_manager)
    
    def find_targets_in_range(self, tower: Tower, enemies: List) -> List:
        """Find enemies in tower's range"""
        # Simplified - in full implementation, check actual positions
        return [e for e in enemies if e.is_alive()][:3]  # Max 3 targets
    
    def handle_measurement_tower(self, tower: MeasurementTower, targets: List, current_time: float, effects_manager=None):
        """Handle measurement tower logic"""
        if not targets:
            return
        
        target = targets[0]
        
        if current_time - tower.last_attack_time >= 1.0 / tower.attack_speed:
            if not target.is_measured:
                # Measure
                measured_path = self.quantum_state_manager.measure_path(target.quantum_circuit)
                target.collapse_to_path(measured_path)
                
                # ADD EFFECT HERE
                if effects_manager:
                    from config.game_config import get_position_on_path
                    pos = get_position_on_path(measured_path, target.position_progress)
                    effects_manager.add_measurement_effect(pos, (100, 255, 100))
            
            # Deal damage
            damage = tower.damage
            actual_damage = target.take_damage(damage)
            
            # ADD DAMAGE NUMBER
            if effects_manager and actual_damage > 0:
                from config.game_config import get_position_on_path
                pos = get_position_on_path(target.measured_path, target.position_progress)
                effects_manager.add_damage_number(pos, int(actual_damage), (255, 100, 100))
            
            tower.last_attack_time = current_time
    
    def handle_phase_tower(self, tower: PhaseTower, targets: List, current_time: float, effects_manager=None):
        """Handle phase tower logic"""
        for enemy in targets:
            if not enemy.is_measured:
                tower.apply_phase_shift(enemy, self.quantum_state_manager, current_time)
                
                # ADD PHASE EFFECT
                if effects_manager and current_time - tower.last_attack_time < 0.1:
                    from config.game_config import get_position_on_path
                    # Show effect on all possible paths for unmeasured enemy
                    positions = []
                    for path_idx in range(4):
                        pos = get_position_on_path(path_idx, enemy.position_progress)
                        positions.append(pos)
                    effects_manager.add_phase_shift_effect(tower.position, tower.target_path)
                break
    
    def handle_entanglement_tower(self, tower: EntanglementTower, targets: List, effects_manager=None):
        """Handle entanglement tower logic"""
        if len(targets) >= 2:
            # Check if targets are not already entangled
            if not targets[0].is_entangled and not targets[1].is_entangled:
                tower.create_entanglement(targets[0], targets[1], self.quantum_state_manager)
                
                # ADD ENTANGLEMENT EFFECT
                if effects_manager:
                    from config.game_config import get_position_on_path
                    if targets[0].is_measured and targets[1].is_measured:
                        pos1 = get_position_on_path(targets[0].measured_path, targets[0].position_progress)
                        pos2 = get_position_on_path(targets[1].measured_path, targets[1].position_progress)
                        effects_manager.add_entanglement_effect(pos1, pos2, (200, 100, 255))
    
    def handle_teleportation_tower(self, tower: TeleportationTower, targets: List, current_time: float, effects_manager=None):
        """Handle teleportation tower logic"""
        for enemy in targets:
            damage = tower.teleport_attack(enemy, current_time)
            
            # ADD TELEPORTATION EFFECT
            if effects_manager and damage > 0:
                from config.game_config import get_position_on_path
                if enemy.is_measured:
                    end_pos = get_position_on_path(enemy.measured_path, enemy.position_progress)
                    effects_manager.add_teleportation_effect(tower.position, end_pos)
                    effects_manager.add_damage_number(end_pos, int(damage), (100, 255, 255))
