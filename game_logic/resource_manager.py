"""
Resource Manager - Handles game resources
Money, Lives, Quantum Coherence management
"""

import logging
from config.game_config import *

logger = logging.getLogger(__name__)


class ResourceManager:
    """Manages all game resources"""
    
    def __init__(self):
        """Initialize resources"""
        self.reset()
    
    def reset(self):
        """Reset all resources to starting values"""
        self.money = STARTING_MONEY
        self.lives = STARTING_LIVES
        self.quantum_coherence = STARTING_QUANTUM_COHERENCE
        self.max_coherence = MAX_QUANTUM_COHERENCE
        self.wave = 0
        self.score = 0
        self.enemies_killed = 0
        self.total_damage_dealt = 0
        
        logger.info("Resources reset to starting values")
    
    def can_afford(self, cost: int) -> bool:
        """
        Check if player can afford a purchase
        
        Args:
            cost: Cost in money
            
        Returns:
            True if affordable
        """
        return self.money >= cost
    
    def spend_money(self, amount: int):
        """
        Spend money
        
        Args:
            amount: Amount to spend
        """
        if amount > self.money:
            logger.warning(f"Attempted to spend ${amount} with only ${self.money}")
            return False
        
        self.money -= amount
        logger.debug(f"Spent ${amount}, remaining: ${self.money}")
        return True
    
    def earn_money(self, amount: int):
        """
        Earn money
        
        Args:
            amount: Amount to earn
        """
        self.money += amount
        logger.debug(f"Earned ${amount}, total: ${self.money}")
    
    def lose_life(self):
        """Lose one life"""
        self.lives -= 1
        logger.info(f"Life lost! Remaining: {self.lives}")
        
        if self.lives <= 0:
            logger.info("No lives remaining - Game Over")
    
    def gain_life(self):
        """Gain one life (bonus)"""
        self.lives += 1
        logger.info(f"Bonus life gained! Total: {self.lives}")
    
    def consume_coherence(self, amount: float):
        """
        Consume quantum coherence
        
        Args:
            amount: Amount to consume
        """
        self.quantum_coherence = max(0, self.quantum_coherence - amount)
    
    def regenerate_coherence(self, delta_time: float):
        """
        Regenerate quantum coherence over time
        
        Args:
            delta_time: Time since last update in seconds
        """
        regen = COHERENCE_REGEN_RATE * delta_time
        self.quantum_coherence = min(
            self.max_coherence,
            self.quantum_coherence + regen
        )
    
    def has_coherence(self, amount: float) -> bool:
        """
        Check if enough coherence available
        
        Args:
            amount: Amount needed
            
        Returns:
            True if enough coherence
        """
        return self.quantum_coherence >= amount
    
    def add_score(self, points: int):
        """
        Add to score
        
        Args:
            points: Points to add
        """
        self.score += points
    
    def enemy_killed(self, reward: int):
        """
        Handle enemy death
        
        Args:
            reward: Money reward for kill
        """
        self.enemies_killed += 1
        self.earn_money(reward)
        self.add_score(reward * 10)
    
    def record_damage(self, damage: float):
        """
        Record damage dealt (for statistics)
        
        Args:
            damage: Damage amount
        """
        self.total_damage_dealt += damage
    
    def get_statistics(self) -> dict:
        """
        Get game statistics
        
        Returns:
            Dictionary of statistics
        """
        return {
            'wave': self.wave,
            'score': self.score,
            'money': self.money,
            'lives': self.lives,
            'coherence': self.quantum_coherence,
            'enemies_killed': self.enemies_killed,
            'damage_dealt': self.total_damage_dealt,
        }
    
    def __str__(self):
        """String representation"""
        return (f"Money: ${self.money} | Lives: {self.lives} | "
                f"Coherence: {self.quantum_coherence:.1f}/{self.max_coherence} | "
                f"Wave: {self.wave}")
