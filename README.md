# Quantum Tower Defense 🎮⚛️

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Qiskit](https://img.shields.io/badge/qiskit-1.0.0-purple.svg)
![Pygame](https://img.shields.io/badge/pygame-2.5.2-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

An educational tower defense game that brings quantum computing concepts to life using IBM's Qiskit SDK. Experience real quantum mechanics through engaging gameplay where enemies exist in superposition and collapse when measured!

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Game Mechanics](#-game-mechanics)
- [Quantum Concepts](#-quantum-concepts-explained)
- [Installation](#-installation)
- [How to Play](#-how-to-play)
- [Tower Types](#-tower-types)
- [Enemy Types](#-enemy-types)
- [Controls](#-controls)
- [Game Strategy](#-game-strategy)
- [Technical Architecture](#-technical-architecture)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

Quantum Tower Defense is an innovative educational game that bridges quantum computing and gaming. Built with **IBM Qiskit** and **Pygame**, it transforms abstract quantum mechanics into tangible gameplay mechanics. Enemies exist in quantum superposition across multiple paths simultaneously until observed, creating unique strategic challenges based on real quantum phenomena.

**Educational Purpose:** Learn quantum computing concepts like superposition, entanglement, measurement, and phase shifts through interactive gameplay.

**Target Audience:** Students, educators, quantum computing enthusiasts, and gamers interested in science.

---

## 🎯 Key Features

### Quantum Mechanics Implementation
- ⚛️ **Real Quantum Circuits**: Uses actual Qiskit quantum circuits
- 🌊 **Superposition States**: Enemies exist on multiple paths with probability amplitudes
- 📊 **Wave Function Collapse**: Measurement towers collapse superposition to definite states
- 🔗 **Quantum Entanglement**: Enemy pairs share quantum states and damage
- 🌀 **Phase Manipulation**: Rotate probability distributions using quantum gates
- 📡 **Quantum Teleportation**: Transfer damage through entangled states

### Gameplay Features
- 🎮 **4 Unique Tower Types**: Each represents a different quantum operation
- 👾 **2 Enemy Types**: Standard enemies and entangled enemy pairs
- 📈 **Progressive Difficulty**: 6+ waves with increasing complexity
- 💰 **Resource Management**: Balance money, lives, and quantum coherence
- ✨ **Visual Effects**: Beautiful quantum operation animations
- 🗑️ **Tower Removal**: Right-click and DELETE/BACKSPACE to remove towers (50% refund)
- 📝 **In-Game Tutorial**: Learn as you play with helpful tooltips

---

## 🎮 Game Mechanics

### Core Loop

1. **Enemy Spawning**: Enemies spawn in quantum superposition across 4 paths
2. **Superposition Movement**: Enemies progress along ALL paths simultaneously
3. **Tower Placement**: Strategically place towers to measure, manipulate, or damage enemies
4. **Measurement**: When measured, enemies collapse to a single path
5. **Defense**: Prevent enemies from reaching the end to protect your base

### Resource System

**💵 Money**
- Starting amount: $400
- Earn money by defeating enemies
- Spend on towers ($100-$250 each)
- Get 50% refund when removing towers

**❤️ Lives**
- Starting lives: 20
- Lose 1 life per enemy that reaches the end
- Game over at 0 lives

**🌊 Quantum Coherence**
- Starting coherence: 10.0 units
- Maximum: 20.0 units
- Regenerates at 0.1 units/second
- Lost when enemies spawn in superposition
- Required for maintaining quantum states

### Path System

The game features **4 distinct paths** representing the computational basis states:
- **Path 0 (|00⟩)**: Top route
- **Path 1 (|01⟩)**: Upper-middle route
- **Path 2 (|10⟩)**: Lower-middle route
- **Path 3 (|11⟩)**: Bottom route

Each enemy starts in equal superposition: `|ψ⟩ = ½(|00⟩ + |01⟩ + |10⟩ + |11⟩)`

---

## 🔬 Quantum Concepts Explained

### 1. Superposition
A quantum system existing in multiple states simultaneously. In the game, enemies appear semi-transparent on all 4 paths at once, with each path having a probability amplitude.

**Quantum Circuit**: Hadamard gates create equal superposition:
```
H gate: |0⟩ → (|0⟩ + |1⟩)/√2
Result: (|00⟩ + |01⟩ + |10⟩ + |11⟩)/2
```

### 2. Measurement & Collapse
Observing a quantum system forces it into a definite state. Measurement towers collapse enemy superposition to one path based on probability distribution.

### 3. Quantum Entanglement
Two particles become correlated; measuring one affects the other. Entanglement towers link enemies so damage to one is shared with its partner (50% transfer).

### 4. Phase Shift
Rotating the phase of probability amplitudes to change probability distribution. Phase towers reduce the probability of enemies being on specific paths.

### 5. Quantum Teleportation
Transferring quantum states using entanglement. Teleportation towers transfer damage instantly across the map.

### 6. Decoherence
Quantum states degrading due to environmental interaction. Represented by the quantum coherence resource that decreases over time.

---

## 📥 Installation

### Prerequisites

- **Python**: 3.9 or higher
- **pip**: Package manager
- **Operating System**: Windows, macOS, or Linux
- **RAM**: 4GB minimum

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/N-Garai/Quantum-tower-defence.git
cd Quantum-tower-defence

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the game
python main.py
```

### Dependency List

- **qiskit 1.0.0**: Quantum computing framework
- **qiskit-aer 0.13.3**: Quantum circuit simulator
- **pygame 2.5.2**: Game development
- **numpy 1.26.0**: Numerical computing
- **matplotlib 3.8.0**: Visualization

---

## 🎮 How to Play

### Starting the Game

1. Launch the game: `python main.py`
2. Main menu appears
3. Press **SPACE** to start or **T** to toggle tutorial
4. Game begins in wave preparation mode

### Objective

**Survive all waves by preventing enemies from reaching the end of paths!**
- Protect your base (20 lives)
- Defeat enemies to earn money
- Build towers strategically
- Manage quantum coherence wisely

### Game Flow

1. **Preparation Phase**
   - Place towers before wave starts
   - Check resources (money & coherence)

2. **Wave Phase**
   - Enemies spawn in superposition
   - Towers automatically engage enemies
   - Monitor progress on all paths
   - Watch for entangled pairs (purple link)

3. **Between Waves**
   - Collect rewards from defeated enemies
   - Reposition towers
   - Prepare for next wave
   - Press **SPACE** to start next wave

4. **Victory or Defeat**
   - **Victory**: Survive all waves with lives remaining
   - **Defeat**: All lives lost
   - Press **R** to restart

---

## 🗼 Tower Types

### 1. 📐 Measurement Tower
**Cost**: $100 | **Hotkey**: `1` | **Range**: 150px | **Damage**: 20/sec

**Function**: Collapses enemy superposition to single path

**Strategy**:
- Place near path intersections
- Essential for dealing damage
- Cheapest tower - good for early game
- Use multiple towers for continuous measurement

---

### 2. 🌀 Phase Tower
**Cost**: $150 | **Hotkey**: `2` | **Range**: 120px | **Damage**: None (probability shift)

**Function**: Applies phase shift to reduce probability on specific paths

**Strategy**:
- Place before measurement towers
- Target shortest path to force enemies onto longer paths
- Combine with measurement towers for control
- Press numpad `0-3` to select target path

---

### 3. 🔗 Entanglement Tower
**Cost**: $200 | **Hotkey**: `3` | **Range**: 100px | **Damage**: 15/sec

**Function**: Links two nearby enemies - damage is shared (50% transfer)

**Strategy**:
- Place where enemies group
- Doubles effective damage output
- Very effective against multiple enemies
- Entanglement persists until one dies

---

### 4. 📡 Teleportation Tower
**Cost**: $250 | **Hotkey**: `4` | **Range**: 80px (attack) | **Damage**: 30/sec

**Function**: Instantly transfers damage across the map using quantum teleportation

**Strategy**:
- Place at key choke points
- Highest damage output
- Most expensive but most powerful
- Use to cover areas other towers can't reach

---

## 👾 Enemy Types

### Standard Enemy
- **Health**: 100 HP
- **Speed**: 0.02 (moderate)
- **Reward**: $10
- **Coherence Cost**: 0.5/second
- **Spawn Rate**: 70%

**Appearance**: Blue semi-transparent (superposition) / Red solid (measured)

**Strategy**: Use measurement towers for reliable takedown

---

### Entangled Enemy Pair
- **Health**: 100 HP each
- **Speed**: 0.02 (synchronized)
- **Reward**: $15 each (total $30)
- **Coherence Cost**: 0.8/second
- **Spawn Rate**: 30%
- **Special**: Damage shared between pair (50% correlation)

**Appearance**: Purple link connecting entangled enemies

**Strategy**: Focus damage on one enemy to damage both, use entanglement towers

---

## 🎯 Controls

### Keyboard Controls

| Key | Action |
|-----|--------|
| **1-4** | Select tower type (M, P, E, T) |
| **SPACE** | Start next wave / Start game |
| **ESC** | Pause / Resume / Exit |
| **R** | Restart game (after game over) |
| **T** | Toggle tutorial |
| **Numpad 0-3** | Select path for Phase Tower |
| **DELETE/BACKSPACE** | Remove selected tower (50% refund) |

### Mouse Controls

| Action | Function |
|--------|----------|
| **Left Click** | Place selected tower |
| **Right Click** | Select tower for removal |
| **Hover** | Preview tower range |

---

## ✨ Visual Effects (November 2025)

The game now includes professional visual effects for all quantum operations:

- **✨ Measurement Effect**: Green expanding circles showing wave function collapse
- **💥 Damage Numbers**: Floating red numbers showing damage dealt
- **🔄 Phase Effect**: Orange rotating particles showing phase manipulation
- **🔗 Entanglement Effect**: Purple particle links between entangled enemies
- **⚡ Teleportation Effect**: Cyan lightning beams showing instant attacks

---

## 🧠 Game Strategy

### Early Game (Waves 1-2)
1. Start with Measurement Towers
2. Place 2-3 towers covering multiple paths
3. Build up economy by defeating enemies

### Mid Game (Waves 3-4)
1. Diversify tower types
2. Add Phase Towers before measurement points
3. Place Entanglement Towers in dense areas

### Late Game (Waves 5+)
1. Maximum synergy between tower types
2. Add Teleportation Towers for bosses
3. Focus fire on high-value targets

---

## 🏗️ Technical Architecture

### System Architecture

```
┌─────────────────────────────────────────┐
│   Main Game Loop (60 FPS)               │
│  Input → Update → Render                │
└─────────────────────────────────────────┘
   ↓           ↓            ↓
Quantum     Game         Rendering
Engine      Logic        System
```

### Key Components

**Quantum Engine** (`quantum_engine/`)
- Manages quantum circuits and state vectors
- Handles enemy quantum states and entanglement
- Uses Qiskit for real simulation

**Game Logic** (`game_logic/`)
- Tower entities and attack logic
- Enemy spawning and wave progression
- Resource tracking

**Rendering** (`rendering/`)
- Main graphics engine
- UI components
- Visual effects system

**Configuration** (`config/`)
- Game constants and settings
- Path definitions
- Tower and enemy configurations

---

## 📁 Project Structure

```
quantum-tower-defense/
├── main.py                      # Game entry point
├── requirements.txt             # Dependencies
├── README.md                    # This file
│
├── config/
│   ├── __init__.py
│   └── game_config.py          # Constants
│
├── quantum_engine/
│   ├── __init__.py
│   ├── quantum_state.py         # Quantum management
│   └── enemy_superposition.py   # Enemy quantum behavior
│
├── game_logic/
│   ├── __init__.py
│   ├── tower.py                 # Tower types
│   ├── wave_manager.py          # Wave system
│   └── resource_manager.py      # Resources
│
├── rendering/
│   ├── __init__.py
│   ├── game_renderer.py         # Graphics
│   ├── ui.py                    # UI elements
│   └── effects.py               # Visual effects
│
└── notebooks/
    ├── 01-quantum-concepts.ipynb
    ├── 02-game-prototype.ipynb
    └── 03-full-demo.ipynb
```

---

## 🤝 Contributing

We welcome contributions! Please see guidelines for:
- Bug reports
- Feature requests
- Documentation improvements
- Asset contributions
- Quantum accuracy verification

### Contribution Process

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see LICENSE file for details.

---

## 🙏 Acknowledgments

- **IBM Qiskit Team**: For the incredible quantum computing framework
- **Pygame Community**: For the robust game development library
- **Quantum Computing Community**: For education and research resources

---

## 📞 Contact & Support

- **GitHub Issues**: Report bugs or request features
- **Email**: For private inquiries

---

**Built with ❤️ and ⚛️ by quantum computing enthusiasts**

*Making quantum mechanics accessible through gaming!*

---

**Last Updated**: November 7, 2025
**Version**: 1.1.0
**Status**: Production Ready ✅
