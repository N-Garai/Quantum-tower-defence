"""
Enemy Superposition - Handles quantum enemy states and behaviors
"""

from dataclasses import dataclass
from typing import Optional, List, Tuple
import numpy as np
from qiskit import QuantumCircuit


@dataclass
class EnemySuperposition:
    """Represents an enemy in quantum superposition"""
    
    enemy_id: int
    quantum_circuit: QuantumCircuit
    health: float
    speed: float
    position_progress: float  # 0.0 to 1.0 along path
    is_measured: bool
    measured_path: Optional[int]
    is_entangled: bool
    entangled_partner_id: Optional[int]
    spawn_time: float
    
    def __init__(self, enemy_id: int, qc: QuantumCircuit, health: float = 100.0, 
                 speed: float = 1.0, spawn_time: float = 0.0):
        self.enemy_id = enemy_id
        self.quantum_circuit = qc
        self.health = health
        self.speed = speed
        self.position_progress = 0.0
        self.is_measured = False
        self.measured_path = None
        self.is_entangled = False
        self.entangled_partner_id = None
        self.spawn_time = spawn_time
    
    def update_position(self, delta_time: float):
        """Update enemy position along path"""
        self.position_progress += self.speed * delta_time
        
    def is_alive(self) -> bool:
        """Check if enemy is still alive"""
        return self.health > 0
    
    def is_at_end(self) -> bool:
        """Check if enemy reached the end"""
        return self.position_progress >= 1.0
    
    def take_damage(self, damage: float) -> float:
        """
        Apply damage to enemy
        
        Args:
            damage: Amount of damage
            
        Returns:
            Actual damage dealt (before death)
        """
        actual_damage = min(damage, self.health)
        self.health -= actual_damage
        return actual_damage
    
    def collapse_to_path(self, path_index: int):
        """Collapse superposition to definite path"""
        self.is_measured = True
        self.measured_path = path_index
    
    def get_active_paths(self, quantum_state_manager) -> List[Tuple[int, float]]:
        """
        Get paths where enemy exists with their probabilities
        
        Returns:
            List of (path_index, probability) tuples
        """
        if self.is_measured:
            return [(self.measured_path, 1.0)]
        
        probabilities = quantum_state_manager.get_path_probabilities(self.quantum_circuit)
        return [(i, p) for i, p in enumerate(probabilities) if p > 0.01]


class EntangledEnemyPair:
    """Manages a pair of entangled enemies"""
    
    def __init__(self, enemy1: EnemySuperposition, enemy2: EnemySuperposition, 
                 entangled_qc: QuantumCircuit, num_qubits_per_enemy: int):
        self.enemy1 = enemy1
        self.enemy2 = enemy2
        self.entangled_circuit = entangled_qc
        self.num_qubits_per_enemy = num_qubits_per_enemy
        
        # Mark enemies as entangled
        enemy1.is_entangled = True
        enemy1.entangled_partner_id = enemy2.enemy_id
        enemy2.is_entangled = True
        enemy2.entangled_partner_id = enemy1.enemy_id
    
    def propagate_damage(self, source_enemy: EnemySuperposition, damage: float) -> float:
        """
        Propagate damage from one entangled enemy to its partner
        
        Args:
            source_enemy: Enemy that took damage
            damage: Amount of damage
            
        Returns:
            Damage dealt to partner
        """
        # Entanglement means damage correlation (not necessarily equal damage)
        # Use quantum correlation coefficient
        correlation_strength = 0.5  # 50% damage transfer
        partner_damage = damage * correlation_strength
        
        if source_enemy.enemy_id == self.enemy1.enemy_id:
            return self.enemy2.take_damage(partner_damage)
        else:
            return self.enemy1.take_damage(partner_damage)
    
    def measure_both(self, quantum_state_manager) -> Tuple[int, int]:
        """
        Measure both entangled enemies (correlates results)
        
        Returns:
            Tuple of (path1, path2)
        """
        # Measure the entangled circuit
        path1 = quantum_state_manager.measure_path(self.entangled_circuit)
        
        # Extract second enemy's path (entangled qubits)
        # For Bell state, second path correlates with first
        path2 = path1  # Perfect correlation for Bell state
        
        self.enemy1.collapse_to_path(path1)
        self.enemy2.collapse_to_path(path2)
        
        return path1, path2


class EnemySpawner:
    """Handles enemy spawning with quantum properties"""
    
    def __init__(self, quantum_state_manager):
        self.quantum_state_manager = quantum_state_manager
        self.next_enemy_id = 0
        self.entanglement_probability = 0.3  # 30% chance of entangled pair
        
    def spawn_single_enemy(self, health: float = 100.0, speed: float = 1.0, 
                           path_probabilities: Optional[List[float]] = None,
                           current_time: float = 0.0) -> EnemySuperposition:
        """
        Spawn a single enemy in superposition
        
        Args:
            health: Enemy health
            speed: Enemy speed
            path_probabilities: Custom path probabilities (None for equal superposition)
            current_time: Current game time
            
        Returns:
            EnemySuperposition object
        """
        qc = self.quantum_state_manager.create_superposition_state(path_probabilities)
        enemy = EnemySuperposition(
            enemy_id=self.next_enemy_id,
            qc=qc,
            health=health,
            speed=speed,
            spawn_time=current_time
        )
        self.next_enemy_id += 1
        return enemy
    
    def spawn_entangled_pair(self, health: float = 100.0, speed: float = 1.0,
                            current_time: float = 0.0) -> EntangledEnemyPair:
        """
        Spawn an entangled pair of enemies
        
        Args:
            health: Enemy health for each
            speed: Enemy speed for each
            current_time: Current game time
            
        Returns:
            EntangledEnemyPair object
        """
        # Create entangled quantum circuit
        entangled_qc = self.quantum_state_manager.create_entangled_pair()
        num_qubits = self.quantum_state_manager.num_qubits
        
        # Create individual quantum circuits for each enemy (will be synced)
        qc1 = self.quantum_state_manager.create_superposition_state()
        qc2 = self.quantum_state_manager.create_superposition_state()
        
        enemy1 = EnemySuperposition(self.next_enemy_id, qc1, health, speed, current_time)
        self.next_enemy_id += 1
        
        enemy2 = EnemySuperposition(self.next_enemy_id, qc2, health, speed, current_time + 0.5)
        self.next_enemy_id += 1
        
        pair = EntangledEnemyPair(enemy1, enemy2, entangled_qc, num_qubits)
        return pair
