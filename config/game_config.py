"""
Game Configuration - Constants and settings
"""

import numpy as np
from typing import Dict, List, Tuple

# Display settings
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Grid settings
GRID_SIZE = 40
GRID_ROWS = SCREEN_HEIGHT // GRID_SIZE
GRID_COLS = SCREEN_WIDTH // GRID_SIZE

# Colors (RGB)
COLORS = {
    'background': (20, 24, 28),
    'grid': (40, 44, 48),
    'path': (60, 80, 100),
    'enemy_superposition': (100, 180, 255, 128),  # Semi-transparent blue
    'enemy_measured': (255, 100, 100),
    'enemy_entangled': (200, 100, 255),
    'tower_measurement': (100, 255, 100),
    'tower_phase': (255, 200, 100),
    'tower_entanglement': (200, 100, 255),
    'tower_teleportation': (100, 255, 255),
    'ui_text': (255, 255, 255),
    'ui_panel': (30, 34, 38),
    'button': (60, 70, 80),
    'button_hover': (80, 90, 100),
    'health_bar': (255, 50, 50),
    'quantum_coherence': (100, 200, 255),
}

# Game paths (4 paths for 2 qubits)
PATHS = [
    # Path 0: Top route
    [(0, 200), (300, 200), (300, 100), (600, 100), (600, 200), (1200, 200)],
    # Path 1: Upper-middle route  
    [(0, 350), (200, 350), (400, 350), (600, 350), (800, 350), (1200, 350)],
    # Path 2: Lower-middle route
    [(0, 500), (300, 500), (300, 600), (600, 600), (900, 500), (1200, 500)],
    # Path 3: Bottom route
    [(0, 650), (400, 650), (400, 700), (800, 700), (800, 650), (1200, 650)],
]

# Number of quantum paths
NUM_PATHS = len(PATHS)
NUM_QUBITS = int(np.log2(NUM_PATHS))

# Enemy configuration
ENEMY_CONFIG = {
    'basic': {
        'health': 100,
        'speed': 0.02,  # Progress per frame
        'reward': 10,
        'coherence_cost': 0.5,
    },
    'fast': {
        'health': 50,
        'speed': 0.04,
        'reward': 15,
        'coherence_cost': 0.3,
    },
    'tank': {
        'health': 300,
        'speed': 0.01,
        'reward': 30,
        'coherence_cost': 0.8,
    },
    'boss': {
        'health': 1000,
        'speed': 0.015,
        'reward': 100,
        'coherence_cost': 1.0,
    }
}

# Tower configuration
TOWER_CONFIG = {
    'measurement': {
        'cost': 100,
        'range': 150,
        'damage': 20,
        'attack_speed': 1.0,
        'description': 'Collapses superposition and attacks',
        'hotkey': '1',
    },
    'phase': {
        'cost': 150,
        'range': 120,
        'damage': 0,
        'attack_speed': 0.5,
        'description': 'Shifts probability away from path',
        'hotkey': '2',
    },
    'entanglement': {
        'cost': 200,
        'range': 100,
        'damage': 15,
        'attack_speed': 0.75,
        'description': 'Links enemies for damage sharing',
        'hotkey': '3',
    },
    'teleportation': {
        'cost': 250,
        'range': 80,
        'damage': 30,
        'attack_speed': 0.5,
        'description': 'Attacks across the map instantly',
        'hotkey': '4',
    }
}

# Wave configuration
WAVE_CONFIG = [
    # Wave 1: Introduction
    {
        'enemies': [('basic', 5)],
        'spawn_delay': 2.0,
        'reward_multiplier': 1.0,
    },
    # Wave 2: More enemies
    {
        'enemies': [('basic', 8), ('fast', 2)],
        'spawn_delay': 1.5,
        'reward_multiplier': 1.1,
    },
    # Wave 3: First tank
    {
        'enemies': [('basic', 10), ('fast', 3), ('tank', 1)],
        'spawn_delay': 1.2,
        'reward_multiplier': 1.2,
    },
    # Wave 4: Mixed
    {
        'enemies': [('basic', 12), ('fast', 5), ('tank', 2)],
        'spawn_delay': 1.0,
        'reward_multiplier': 1.3,
    },
    # Wave 5: Boss wave
    {
        'enemies': [('basic', 15), ('fast', 8), ('tank', 3), ('boss', 1)],
        'spawn_delay': 0.8,
        'reward_multiplier': 1.5,
    },
    # Wave 6+: Scaling difficulty
    {
        'enemies': [('basic', 20), ('fast', 10), ('tank', 5), ('boss', 2)],
        'spawn_delay': 0.6,
        'reward_multiplier': 2.0,
    },
]

# Resource configuration
STARTING_MONEY = 400
STARTING_LIVES = 20
STARTING_QUANTUM_COHERENCE = 10.0
MAX_QUANTUM_COHERENCE = 20.0
COHERENCE_REGEN_RATE = 0.1  # Per second

# UI Layout
UI_PANEL_HEIGHT = 100
TOWER_BUTTON_SIZE = 80
TOWER_BUTTON_MARGIN = 10

# Quantum visualization
SUPERPOSITION_ALPHA = 128  # Transparency for superposition
ENTANGLEMENT_LINE_WIDTH = 3
MEASUREMENT_EFFECT_DURATION = 0.5  # seconds
PHASE_EFFECT_DURATION = 0.3  # seconds

# Performance settings
MAX_ENEMIES = 100
MAX_TOWERS = 50

# Game rules
ENTANGLEMENT_PROBABILITY = 0.3  # 30% chance for enemy pairs
DECOHERENCE_RATE = 0.05  # Quantum coherence loss per unmeasured enemy per second

def get_path_length(path_index: int) -> float:
    """Calculate total length of a path"""
    path = PATHS[path_index]
    total_length = 0.0
    for i in range(len(path) - 1):
        dx = path[i+1][0] - path[i][0]
        dy = path[i+1][1] - path[i][1]
        total_length += np.sqrt(dx*dx + dy*dy)
    return total_length

def get_position_on_path(path_index: int, progress: float) -> Tuple[float, float]:
    """
    Get (x, y) position on path given progress (0.0 to 1.0)
    
    Args:
        path_index: Index of the path
        progress: Progress along path (0.0 = start, 1.0 = end)
        
    Returns:
        (x, y) tuple
    """
    path = PATHS[path_index]
    if progress <= 0:
        return path[0]
    if progress >= 1:
        return path[-1]
    
    # Calculate total path length
    total_length = get_path_length(path_index)
    target_distance = progress * total_length
    
    # Find segment containing target distance
    current_distance = 0.0
    for i in range(len(path) - 1):
        dx = path[i+1][0] - path[i][0]
        dy = path[i+1][1] - path[i][1]
        segment_length = np.sqrt(dx*dx + dy*dy)
        
        if current_distance + segment_length >= target_distance:
            # Interpolate within this segment
            segment_progress = (target_distance - current_distance) / segment_length
            x = path[i][0] + dx * segment_progress
            y = path[i][1] + dy * segment_progress
            return (x, y)
        
        current_distance += segment_length
    
    return path[-1]

def is_valid_tower_placement(position: Tuple[float, float]) -> bool:
    """
    Check if tower can be placed at position (not on path)
    
    Args:
        position: (x, y) tuple
        
    Returns:
        True if valid placement
    """
    MIN_DISTANCE_FROM_PATH = 30
    
    # Check distance from all path segments
    for path in PATHS:
        for i in range(len(path) - 1):
            # Check distance to line segment
            dist = point_to_segment_distance(position, path[i], path[i+1])
            if dist < MIN_DISTANCE_FROM_PATH:
                return False
    
    return True

def point_to_segment_distance(point: Tuple[float, float], 
                               seg_start: Tuple[float, float], 
                               seg_end: Tuple[float, float]) -> float:
    """Calculate minimum distance from point to line segment"""
    px, py = point
    x1, y1 = seg_start
    x2, y2 = seg_end
    
    dx = x2 - x1
    dy = y2 - y1
    
    if dx == 0 and dy == 0:
        return np.sqrt((px - x1)**2 + (py - y1)**2)
    
    t = max(0, min(1, ((px - x1) * dx + (py - y1) * dy) / (dx*dx + dy*dy)))
    
    proj_x = x1 + t * dx
    proj_y = y1 + t * dy
    
    return np.sqrt((px - proj_x)**2 + (py - proj_y)**2)
