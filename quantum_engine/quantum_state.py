"""
Quantum State Manager for Tower Defense
Handles qubit representation of enemies and quantum operations
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import numpy as np
from typing import List, Tuple, Optional


class QuantumStateManager:
    """Manages quantum states for the game"""
    
    def __init__(self, num_paths: int = 4):
        """
        Initialize quantum state manager
        
        Args:
            num_paths: Number of possible paths (must be power of 2)
        """
        self.num_paths = num_paths
        self.num_qubits = int(np.log2(num_paths))
        self.simulator = AerSimulator()
        
    def create_superposition_state(self, probabilities: Optional[List[float]] = None) -> QuantumCircuit:
        """
        Create a quantum circuit with enemy in superposition across paths
        
        Args:
            probabilities: Optional probability amplitudes for each path
                          If None, creates equal superposition
        
        Returns:
            QuantumCircuit representing the superposition state
        """
        qc = QuantumCircuit(self.num_qubits)
        
        if probabilities is None:
            # Equal superposition using Hadamard gates
            for i in range(self.num_qubits):
                qc.h(i)
        else:
            # Custom superposition using state initialization
            # Normalize probabilities to amplitudes
            amplitudes = np.sqrt(probabilities)
            amplitudes = amplitudes / np.linalg.norm(amplitudes)
            
            # Pad to power of 2 if needed
            if len(amplitudes) < 2**self.num_qubits:
                amplitudes = np.pad(amplitudes, (0, 2**self.num_qubits - len(amplitudes)))
            
            qc.initialize(amplitudes, range(self.num_qubits))
        
        return qc
    
    def apply_phase_gate(self, qc: QuantumCircuit, path_index: int, phase: float) -> QuantumCircuit:
        """
        Apply phase rotation to specific path (used for tower effects)
        
        Args:
            qc: Quantum circuit
            path_index: Index of path to apply phase to
            phase: Phase angle in radians
        
        Returns:
            Modified quantum circuit
        """
        # Convert path index to binary string for controlled phase
        binary = format(path_index, f'0{self.num_qubits}b')
        
        # Apply X gates to set up controlled phase
        for i, bit in enumerate(reversed(binary)):
            if bit == '0':
                qc.x(i)
        
        # Apply controlled phase
        if self.num_qubits == 1:
            qc.p(phase, 0)
        else:
            qc.mcp(phase, list(range(self.num_qubits - 1)), self.num_qubits - 1)
        
        # Undo X gates
        for i, bit in enumerate(reversed(binary)):
            if bit == '0':
                qc.x(i)
        
        return qc
    
    def get_path_probabilities(self, qc: QuantumCircuit) -> np.ndarray:
        """
        Get probability distribution over paths without measurement (peek)
        
        Args:
            qc: Quantum circuit
        
        Returns:
            Array of probabilities for each path
        """
        statevector = Statevector(qc)
        probabilities = statevector.probabilities()
        return probabilities[:self.num_paths]
    
    def measure_path(self, qc: QuantumCircuit, shots: int = 1) -> int:
        """
        Measure the quantum state to collapse to a definite path
        
        Args:
            qc: Quantum circuit
            shots: Number of measurements (usually 1 for single collapse)
        
        Returns:
            Measured path index
        """
        # Add classical register for measurement
        cr = ClassicalRegister(self.num_qubits)
        measured_qc = qc.copy()
        measured_qc.add_register(cr)
        measured_qc.measure(range(self.num_qubits), range(self.num_qubits))
        
        # Execute measurement
        job = self.simulator.run(measured_qc, shots=shots)
        result = job.result()
        counts = result.get_counts()
        
        # Get most common result (for shots=1, this is the only result)
        measured_state = max(counts, key=counts.get)
        path_index = int(measured_state, 2)
        
        return path_index
    
    def calculate_quantum_coherence(self, qc: QuantumCircuit) -> float:
        """
        Calculate coherence measure (resource cost)
        Based on purity of the quantum state
        
        Args:
            qc: Quantum circuit
        
        Returns:
            Coherence value (0 to 1, higher = more superposition)
        """
        statevector = Statevector(qc)
        density_matrix = statevector.to_operator()
        
        # Calculate purity: Tr(ρ²)
        purity = np.real(np.trace(density_matrix.data @ density_matrix.data))
        
        # Coherence is inverse of purity (pure state = low coherence cost)
        coherence = 1.0 - purity
        
        return coherence
    
    def create_entangled_pair(self) -> QuantumCircuit:
        """
        Create two entangled enemy states (Bell state)
        
        Returns:
            QuantumCircuit with entangled pair
        """
        qc = QuantumCircuit(self.num_qubits * 2)
        
        # Create equal superposition on first enemy
        for i in range(self.num_qubits):
            qc.h(i)
        
        # Entangle with second enemy using CNOT gates
        for i in range(self.num_qubits):
            qc.cx(i, self.num_qubits + i)
        
        return qc
    
    def apply_cnot_damage(self, qc: QuantumCircuit, control_qubits: List[int], 
                          target_qubits: List[int]) -> QuantumCircuit:
        """
        Apply CNOT gates to propagate damage between entangled enemies
        
        Args:
            qc: Quantum circuit
            control_qubits: Control qubit indices
            target_qubits: Target qubit indices
        
        Returns:
            Modified quantum circuit
        """
        for control, target in zip(control_qubits, target_qubits):
            qc.cx(control, target)
        
        return qc
