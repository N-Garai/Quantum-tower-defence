# Quantum Tower Defense 🎮⚛️

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Qiskit](https://img.shields.io/badge/qiskit-1.0.0-purple.svg)
![Pygame](https://img.shields.io/badge/pygame-2.5.2-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Overview

Quantum Tower Defense is an educational game that combines tower defense gameplay with real quantum computing concepts using IBM's Qiskit SDK. Enemies exist in quantum superposition across multiple paths until measured by towers, creating unique strategic gameplay based on actual quantum mechanics.

## 🎯 Key Features

- **Quantum Superposition**: Enemies exist on multiple paths simultaneously
- **Wave Function Collapse**: Measurement towers force enemies to single paths
- **Quantum Entanglement**: Enemy pairs share damage through quantum correlation
- **Phase Manipulation**: Shift probability distributions of unmeasured enemies
- **Quantum Teleportation**: Instant damage transfer across the map
- **Resource Management**: Balance quantum coherence budget with enemy spawns

## 🔬 Quantum Concepts Implemented

- Hadamard gates for equal superposition
- Quantum measurement and state collapse
- Bell states for entanglement
- Phase rotation gates
- Decoherence mechanics
- No-cloning theorem

## 📋 Prerequisites

- Python 3.9 or higher
- pip package manager
- 4GB RAM minimum
- Graphics support (OpenGL)

## 🚀 Installation

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/quantum-tower-defense.git
cd quantum-tower-defense

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

### Docker Installation (Alternative)

```bash
docker build -t quantum-td .
docker run -it --rm -e DISPLAY=$DISPLAY quantum-td
```

## 🎮 How to Play

### Controls

- **1-4 Keys**: Select tower type (Measurement, Phase, Entanglement, Teleportation)
- **Mouse Click**: Place selected tower
- **SPACE**: Start next wave
- **ESC**: Pause game
- **R**: Restart game
- **Q**: Quit

### Tower Types

| Tower | Cost | Function | Quantum Concept |
|-------|------|----------|-----------------|
| **Measurement** | $100 | Collapses superposition, deals damage | Wave function collapse |
| **Phase** | $150 | Shifts path probabilities | Phase rotation |
| **Entanglement** | $200 | Links enemies for shared damage | Quantum entanglement |
| **Teleportation** | $250 | Instant damage across map | Quantum teleportation |

### Enemy Types

- **Basic**: Standard enemy (100 HP, 0.5 coherence)
- **Fast**: Quick but fragile (50 HP, 0.3 coherence)
- **Tank**: Slow and durable (300 HP, 0.8 coherence)
- **Boss**: Massive threat (1000 HP, 1.0 coherence)

## 📊 Project Structure

```
quantum-tower-defense/
├── main.py                      # Game entry point
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Container configuration
├── README.md                    # This file
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore rules
│
├── quantum_engine/              # Quantum mechanics core
│   ├── __init__.py
│   ├── quantum_state.py         # State management
│   ├── enemy_superposition.py   # Enemy quantum states
│   ├── entanglement.py          # Entanglement mechanics
│   └── measurement.py           # Measurement operations
│
├── game_logic/                  # Game systems
│   ├── __init__.py
│   ├── enemy.py                 # Enemy entities
│   ├── tower.py                 # Tower entities
│   ├── wave_manager.py          # Wave spawning
│   └── resource_manager.py      # Money/lives/coherence
│
├── rendering/                   # Graphics and UI
│   ├── __init__.py
│   ├── game_renderer.py         # Main renderer
│   ├── ui.py                    # UI components
│   └── effects.py               # Visual effects
│
├── config/                      # Configuration
│   ├── __init__.py
│   └── game_config.py           # Game constants
│
├── assets/                      # Game assets
│   ├── fonts/                   # Font files
│   ├── sounds/                  # Sound effects
│   └── images/                  # Sprites/icons
│
├── tests/                       # Unit tests
│   ├── __init__.py
│   ├── test_quantum.py          # Quantum mechanics tests
│   ├── test_game_logic.py       # Game logic tests
│   └── test_integration.py      # Integration tests
│
├── notebooks/                   # Educational notebooks
│   ├── 01_quantum_concepts.ipynb
│   ├── 02_game_prototype.ipynb
│   ├── 03_full_demo.ipynb
│   └── 04_analysis.ipynb
│
└── docs/                        # Documentation
    ├── architecture.md
    ├── quantum_mechanics.md
    ├── gameplay_guide.md
    └── api_reference.md
```

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=quantum_engine tests/

# Run specific test file
pytest tests/test_quantum.py -v
```

## 📚 Educational Notebooks

Launch Jupyter to explore quantum concepts:

```bash
jupyter notebook notebooks/01_quantum_concepts.ipynb
```

**Notebooks included:**
1. **Quantum Concepts** - Introduction to superposition, measurement, entanglement
2. **Game Prototype** - Interactive game mechanics demonstration
3. **Full Demo** - Complete gameplay with visualization
4. **Analysis** - Performance metrics and quantum statistics

## 🎓 Learning Objectives

Players will understand:
- Quantum superposition and its collapse through measurement
- Entanglement and non-local correlations
- Phase manipulation and interference
- Decoherence and quantum resource management
- Practical applications of quantum computing concepts

## 🛠️ Development

### Setting Up Development Environment

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run linting
flake8 quantum_engine/ game_logic/
black quantum_engine/ game_logic/
```

### Building from Source

```bash
# Build package
python setup.py build

# Create distribution
python setup.py sdist bdist_wheel
```

## 📈 Performance

- **Target FPS**: 60
- **Max Enemies**: 100 simultaneous
- **Max Towers**: 50 placed
- **Memory Usage**: ~200MB
- **CPU**: Single-core optimized

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **IBM Qiskit Team** - Quantum computing framework
- **Pygame Community** - Game development library
- **Quantum Computing Researchers** - Educational inspiration

## 📧 Contact

- **Project Lead**: IBM Quantum Education Team
- **Email**: quantum-games@ibm.com
- **Issues**: [GitHub Issues](https://github.com/yourusername/quantum-tower-defense/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/quantum-tower-defense/discussions)

## 🔗 Links

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Experience](https://quantum-computing.ibm.com/)
- [Game Design Document](docs/design_document.pdf)
- [Video Tutorial Series](https://youtube.com/playlist?list=...)

## 📊 Metrics & Analytics

![GitHub Stars](https://img.shields.io/github/stars/yourusername/quantum-tower-defense)
![GitHub Forks](https://img.shields.io/github/forks/yourusername/quantum-tower-defense)
![GitHub Issues](https://img.shields.io/github/issues/yourusername/quantum-tower-defense)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/yourusername/quantum-tower-defense)

## 🗺️ Roadmap

### Version 1.0 (Current)
- ✅ Core quantum mechanics
- ✅ 4 tower types
- ✅ 4 enemy types
- ✅ 6 waves
- ✅ Educational notebooks

### Version 1.1 (Planned)
- [ ] Multiplayer support
- [ ] Custom wave editor
- [ ] Achievement system
- [ ] Leaderboards

### Version 2.0 (Future)
- [ ] 3D graphics
- [ ] Real quantum hardware integration
- [ ] Advanced quantum gates
- [ ] Campaign mode

---

**Made with ❤️ and ⚛️ by IBM Quantum Education Team**
