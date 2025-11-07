# 🎮⚛️ Quantum Tower Defense - Complete Setup Guide

## 📖 Table of Contents

1. [System Requirements](#-system-requirements)
2. [Installation Methods](#-installation-methods)
3. [Step-by-Step Setup](#-step-by-step-setup)
4. [Verification & Testing](#-verification--testing)
5. [Troubleshooting](#-troubleshooting)
6. [Running the Game](#-running-the-game)
7. [Project Structure](#-project-structure)
8. [Development Setup](#-development-setup)
9. [FAQ](#-faq)

---

## 💻 System Requirements

### Minimum Requirements

| Component | Requirement |
|-----------|-------------|
| **Operating System** | Windows 10/11, macOS 10.14+, or Linux (Ubuntu 20.04+) |
| **Python** | 3.9 or higher |
| **RAM** | 4GB minimum |
| **Storage** | 500MB free space |
| **Graphics** | OpenGL 2.0+ support |
| **Display** | 1200x800 resolution or higher |
| **Internet** | Required for initial installation only |

### Recommended Requirements

| Component | Recommendation |
|-----------|----------------|
| **Operating System** | Windows 11 or macOS 12+ |
| **Python** | 3.11+ for best performance |
| **RAM** | 8GB or more |
| **Storage** | 1GB free space |
| **Display** | 1920x1080 resolution |
| **CPU** | Multi-core processor for quantum simulations |

---

## 📦 Installation Methods

### Method 1: Quick Install (Recommended)

**Best for**: Users who want to play immediately

```bash
# Clone the repository
git clone https://github.com/N-Garai/Quantum-tower-defence.git
cd Quantum-tower-defence

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python main-game.py
```

### Method 2: Manual Setup

**Best for**: Advanced users or troubleshooting

See [Step-by-Step Setup](#-step-by-step-setup) section below.

### Method 3: Development Install

**Best for**: Contributors and developers

See [Development Setup](#-development-setup) section below.

---

## 🚀 Step-by-Step Setup

### Step 1: Install Python

#### Windows

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run installer
3. **Important**: Check ☑️ "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
   ```powershell
   python --version
   ```

#### macOS

```bash
# Using Homebrew (recommended)
brew install python@3.11

# Verify installation
python3 --version
```

#### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python 3.11
sudo apt install python3.11 python3.11-venv python3-pip

# Verify installation
python3 --version
```

### Step 2: Install Git

#### Windows
- Download from [git-scm.com](https://git-scm.com/)
- Run installer with default options

#### macOS
```bash
brew install git
```

#### Linux
```bash
sudo apt install git
```

Verify Git installation:
```bash
git --version
```

### Step 3: Clone the Repository

```bash
# Navigate to desired location
cd ~/Documents  # or any preferred directory

# Clone the repository
git clone https://github.com/N-Garai/Quantum-tower-defence.git

# Enter project directory
cd Quantum-tower-defence

# Verify files
ls  # macOS/Linux
dir  # Windows
```

### Step 4: Create Virtual Environment

**Why virtual environment?**
- Isolates project dependencies
- Prevents conflicts with other Python projects
- Makes dependency management easier

#### Windows
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# You should see (venv) prefix in terminal
```

#### macOS/Linux
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# You should see (venv) prefix in terminal
```

### Step 5: Install Dependencies

```bash
# Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

**This installs**:
- qiskit 1.0.0 (Quantum computing framework)
- qiskit-aer 0.13.3 (Quantum simulator)
- pygame 2.5.2 (Game engine)
- numpy 1.26.0 (Numerical computing)
- matplotlib 3.8.0 (Plotting)
- seaborn 0.13.0 (Visualization)
- dataclasses-json 0.6.1 (Data serialization)

**Installation time**: 2-5 minutes (depending on internet speed)

### Step 6: Verify Installation

```bash
# Check if all packages are installed
pip list

# Verify Qiskit
python -c "import qiskit; print(qiskit.__version__)"

# Verify Pygame
python -c "import pygame; print(pygame.__version__)"

# Check Python path
python -c "import sys; print(sys.executable)"
```

Expected output:
```
1.0.0  # Qiskit version
2.5.2  # Pygame version
/path/to/venv/bin/python  # Virtual environment Python
```

---

## ✅ Verification & Testing

### Test 1: Import Modules

```bash
python -c "from quantum_engine.quantum_state import QuantumStateManager; print('✓ Quantum engine OK')"
python -c "from game_logic.tower import TowerManager; print('✓ Game logic OK')"
python -c "from rendering.game_renderer import GameRenderer; print('✓ Rendering OK')"
```

### Test 2: Run Quantum Circuit Test

```python
# test_quantum.py
from qiskit import QuantumCircuit
from qiskit_aer import Aer

# Create simple circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.h(1)
qc.measure_all()

# Simulate
simulator = Aer.get_backend('qasm_simulator')
job = simulator.run(qc, shots=100)
result = job.result()
counts = result.get_counts()

print("Quantum simulation successful!")
print(f"Measurement results: {counts}")
```

Run test:
```bash
python test_quantum.py
```

### Test 3: Pygame Window Test

```python
# test_pygame.py
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test Window")

print("Pygame initialized successfully!")
print(f"Display size: {screen.get_size()}")

running = True
clock = pygame.time.Clock()

for i in range(60):  # Run for 1 second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Test completed successfully!")
```

Run test:
```bash
python test_pygame.py
```

---

## 🎮 Running the Game

### Launch Game

```bash
# Make sure virtual environment is activated
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Run the game
python main-game.py
```

### Expected Launch Sequence

1. **Console Output**:
   ```
   pygame 2.5.2 (SDL 2.28.3, Python 3.11.x)
   Hello from the pygame community. https://www.pygame.org/contribute.html
   2025-11-07 XX:XX:XX,XXX - __main__ - INFO - Initializing Quantum Tower Defense...
   2025-11-07 XX:XX:XX,XXX - __main__ - WARNING - Game icon not found, using default
   2025-11-07 XX:XX:XX,XXX - game_logic.resource_manager - INFO - Resources reset to starting values
   2025-11-07 XX:XX:XX,XXX - game_logic.wave_manager - INFO - Wave Manager initialized
   2025-11-07 XX:XX:XX,XXX - rendering.game_renderer - INFO - Game Renderer initialized
   2025-11-07 XX:XX:XX,XXX - __main__ - INFO - Game initialized successfully
   2025-11-07 XX:XX:XX,XXX - __main__ - INFO - Starting game loop...
   ```

2. **Game Window Opens**:
   - Title: "Quantum Tower Defense - IBM Qiskit"
   - Resolution: 1200x800
   - Main menu visible

3. **No Error Messages**: If you see errors, see [Troubleshooting](#-troubleshooting)

### Command Line Options

Currently, the game doesn't have command-line options, but you can modify settings in `config/game_config.py`:

```python
# config/game_config.py

# Change resolution
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Change FPS
FPS = 144

# Adjust difficulty
STARTING_MONEY = 500  # Default: 400
STARTING_LIVES = 30   # Default: 20
```

---

## 🔧 Troubleshooting

### Common Issues

#### Issue 1: "Python not found" or "command not found"

**Symptoms**:
```
'python' is not recognized as an internal or external command
```

**Solutions**:
1. **Windows**: Add Python to PATH
   - Search "Environment Variables" in Start Menu
   - Edit "Path" variable
   - Add Python installation directory (e.g., `C:\Python311`)
   - Add Scripts directory (e.g., `C:\Python311\Scripts`)
   - Restart terminal

2. **macOS/Linux**: Use `python3` instead of `python`
   ```bash
   python3 --version
   python3 main-game.py
   ```

3. **Create alias** (macOS/Linux):
   ```bash
   echo "alias python=python3" >> ~/.bashrc
   source ~/.bashrc
   ```

---

#### Issue 2: "No module named 'qiskit'"

**Symptoms**:
```
ModuleNotFoundError: No module named 'qiskit'
```

**Solutions**:
1. **Verify virtual environment is activated**:
   ```bash
   # You should see (venv) in terminal prompt
   which python  # Should point to venv/bin/python
   ```

2. **Reinstall dependencies**:
   ```bash
   pip install --force-reinstall -r requirements.txt
   ```

3. **Check Python path**:
   ```bash
   python -c "import sys; print(sys.executable)"
   # Should be in your venv folder
   ```

---

#### Issue 3: Pygame window doesn't open

**Symptoms**:
- No window appears
- Black screen
- "SDL" errors

**Solutions**:

**Windows**:
1. Install Microsoft Visual C++ Redistributable
2. Update graphics drivers
3. Run as administrator

**macOS**:
```bash
# Install SDL2 dependencies
brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer
```

**Linux**:
```bash
# Install SDL2 dependencies
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

# Install audio dependencies
sudo apt install pulseaudio

# Reinstall pygame
pip uninstall pygame
pip install pygame
```

---

#### Issue 4: Game runs slowly / Low FPS

**Symptoms**:
- Stuttering
- FPS below 30
- Lag during waves

**Solutions**:

1. **Reduce resolution** (edit `config/game_config.py`):
   ```python
   SCREEN_WIDTH = 1024
   SCREEN_HEIGHT = 768
   ```

2. **Lower FPS cap**:
   ```python
   FPS = 30  # Instead of 60
   ```

3. **Disable visual effects** (edit `rendering/effects.py`):
   ```python
   ENABLE_PARTICLES = False
   ENABLE_GLOW = False
   ```

4. **Close other applications**
5. **Update graphics drivers**

---

#### Issue 5: "AttributeError: 'TowerManager' object has no attribute"

**Symptoms**:
```
AttributeError: 'TowerManager' object has no attribute 'clear_all_towers'
```

**Solutions**:

1. **Pull latest changes**:
   ```bash
   git pull origin main
   ```

2. **Check file integrity**:
   ```bash
   git status
   # Should show "Your branch is up to date"
   ```

3. **Verify tower.py** has all methods:
   ```bash
   grep "def clear_all_towers" game_logic/tower.py
   ```

---

#### Issue 6: Import errors after installation

**Symptoms**:
```
ImportError: cannot import name 'X' from 'Y'
```

**Solutions**:

1. **Check __init__.py files exist**:
   ```bash
   # These files should exist (can be empty):
   quantum_engine/__init__.py
   game_logic/__init__.py
   rendering/__init__.py
   config/__init__.py
   ```

2. **Create missing __init__.py**:
   ```bash
   touch quantum_engine/__init__.py
   touch game_logic/__init__.py
   touch rendering/__init__.py
   touch config/__init__.py
   ```

---

### Performance Optimization

#### Optimize Python

```bash
# Use PyPy for faster execution (experimental)
pip install pypy3

# Or enable Python optimizations
python -O main-game.py
```

#### Reduce Quantum Simulation Overhead

Edit `quantum_engine/quantum_state.py`:

```python
# Use fewer shots for measurements
shots = 100  # Instead of 1000

# Cache quantum circuits
@lru_cache(maxsize=128)
def create_superposition_circuit(num_qubits):
    # ... circuit creation
```

---

## 📁 Project Structure

```
Quantum-tower-defence/
│
├── 📄 main-game.py                  # Game entry point
├── 📄 requirements.txt              # Python dependencies
├── 📄 .gitignore                    # Git ignore rules
├── 📄 README.md                     # Project documentation
├── 📄 SETUP-GUIDE.md               # This file
├── 📄 LICENSE                       # MIT License
│
├── 📁 config/                       # Configuration files
│   ├── __init__.py
│   └── game_config.py               # Game constants, paths, settings
│       ├── Display settings (resolution, FPS)
│       ├── Game paths (4 quantum paths)
│       ├── Enemy configuration (4 types)
│       ├── Tower configuration (4 types)
│       ├── Wave configuration (6+ waves)
│       └── Resource settings (money, lives, coherence)
│
├── 📁 quantum_engine/               # Quantum mechanics core
│   ├── __init__.py
│   ├── quantum_state.py             # Quantum state manager
│   │   ├── QuantumStateManager class
│   │   ├── Circuit creation (H gates, CNOT, U3)
│   │   ├── Measurement operations
│   │   ├── Path probability calculations
│   │   └── Phase gate applications
│   │
│   └── enemy_superposition.py       # Enemy quantum behaviors
│       ├── EnemySuperposition class
│       ├── EntangledEnemyPair class
│       ├── EnemySpawner class
│       ├── Superposition state management
│       └── Entanglement mechanics
│
├── 📁 game_logic/                   # Game systems
│   ├── __init__.py
│   ├── tower.py                     # Tower entities and logic
│   │   ├── Tower (base class)
│   │   ├── MeasurementTower
│   │   ├── PhaseTower
│   │   ├── EntanglementTower
│   │   ├── TeleportationTower
│   │   └── TowerManager
│   │
│   ├── wave_manager.py              # Wave spawning system
│   │   ├── WaveManager class
│   │   ├── Enemy spawning queue
│   │   ├── Wave progression logic
│   │   └── Difficulty scaling
│   │
│   └── resource_manager.py          # Resource tracking
│       ├── ResourceManager class
│       ├── Money management
│       ├── Lives tracking
│       └── Quantum coherence system
│
├── 📁 rendering/                    # Graphics and UI
│   ├── __init__.py
│   ├── game_renderer.py             # Main renderer
│   │   ├── GameRenderer class
│   │   ├── Path rendering
│   │   ├── Enemy rendering (superposition effects)
│   │   ├── Tower rendering
│   │   └── Visual effects
│   │
│   ├── ui.py                        # UI components
│   │   ├── UIManager class
│   │   ├── Tower selection panel
│   │   ├── Resource display
│   │   ├── Wave information
│   │   └── Tutorial overlay
│   │
│   └── effects.py                   # Visual effects
│       ├── EffectsManager class
│       ├── Measurement effects
│       ├── Entanglement visualizations
│       └── Particle systems
│
├── 📁 notebooks/                    # Educational Jupyter notebooks
│   ├── 01-quantum-concepts.ipynb   # Quantum mechanics introduction
│   ├── 02-game-prototype.ipynb     # Game mechanics testing
│   └── 03-full-demo.ipynb          # Interactive visualization
│
└── 📁 venv/                        # Virtual environment (not in git)
    └── (Python packages installed here)
```

### File Descriptions

#### Core Files

**main-game.py** (387 lines):
- `QuantumTowerDefense` class: Main game controller
- Game loop (60 FPS)
- Event handling (keyboard, mouse)
- Game state management (menu, playing, paused, game_over, victory)
- Tower placement logic
- Wave progression

#### Configuration

**config/game_config.py** (275 lines):
- Display settings: 1200x800 resolution, 60 FPS
- 4 game paths (representing |00⟩, |01⟩, |10⟩, |11⟩)
- Enemy stats (Basic, Fast, Tank, Boss)
- Tower stats (Measurement, Phase, Entanglement, Teleportation)
- 6 wave configurations
- Resource constants (money, lives, coherence)
- Helper functions (path calculations, collision detection)

#### Quantum Engine

**quantum_engine/quantum_state.py**:
- Manages Qiskit quantum circuits
- Creates superposition states
- Performs measurements
- Calculates probabilities
- Applies quantum gates (H, CNOT, U3)

**quantum_engine/enemy_superposition.py** (204 lines):
- `EnemySuperposition`: Enemy with quantum properties
- `EntangledEnemyPair`: Linked enemy pairs
- `EnemySpawner`: Creates enemies with quantum circuits
- Position tracking across multiple paths
- Damage sharing through entanglement

#### Game Logic

**game_logic/tower.py** (391 lines):
- `Tower`: Base tower class
- `MeasurementTower`: Collapses superposition
- `PhaseTower`: Applies phase rotation
- `EntanglementTower`: Links enemies
- `TeleportationTower`: Instant damage transfer
- `TowerManager`: Manages all towers
- Attack logic and targeting

**game_logic/wave_manager.py** (283 lines):
- Spawn queue management
- Enemy spawning with delays
- Wave progression
- Difficulty scaling
- Enemy lifecycle management

**game_logic/resource_manager.py**:
- Money tracking
- Lives management
- Quantum coherence system
- Decoherence calculations

#### Rendering

**rendering/game_renderer.py**:
- Pygame drawing operations
- Path visualization
- Enemy rendering (with transparency for superposition)
- Tower rendering with range indicators
- Entanglement line drawing
- Quantum state visualizations

**rendering/ui.py**:
- Tower selection buttons
- Resource display (money, lives, coherence)
- Wave counter
- Tutorial overlays
- Button interactions

**rendering/effects.py**:
- Measurement collapse effects
- Phase rotation animations
- Entanglement particles
- Teleportation effects

---

## 👨‍💻 Development Setup

### For Contributors

```bash
# 1. Fork repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/Quantum-tower-defence.git
cd Quantum-tower-defence

# 3. Add upstream remote
git remote add upstream https://github.com/N-Garai/Quantum-tower-defence.git

# 4. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Install development tools
pip install pytest pytest-cov black flake8 mypy jupyter

# 7. Create feature branch
git checkout -b feature/your-feature-name

# 8. Make changes and test
pytest tests/

# 9. Format code
black .
flake8 .

# 10. Commit and push
git add .
git commit -m "Add: your feature description"
git push origin feature/your-feature-name

# 11. Create Pull Request on GitHub
```

### Development Tools

```bash
# Code formatting
black quantum_engine/ game_logic/ rendering/

# Linting
flake8 --max-line-length=100 .

# Type checking
mypy quantum_engine/

# Run tests with coverage
pytest --cov=quantum_engine --cov=game_logic tests/

# Generate coverage report
pytest --cov-report=html --cov=. tests/
```

### Testing

Create `tests/test_basic.py`:

```python
import pytest
from quantum_engine.quantum_state import QuantumStateManager
from game_logic.tower import MeasurementTower

def test_quantum_state_manager():
    qsm = QuantumStateManager(num_paths=4)
    qc = qsm.create_superposition_circuit()
    assert qc.num_qubits == 2
    
    probs = qsm.get_path_probabilities(qc)
    assert len(probs) == 4
    assert abs(sum(probs) - 1.0) < 0.01  # Total probability = 1

def test_measurement_tower():
    tower = MeasurementTower(tower_id=0, position=(100, 100))
    assert tower.tower_type == "measurement"
    assert tower.cost == 100
    assert tower.range == 150.0
```

Run tests:
```bash
pytest tests/ -v
```

---

## ❓ FAQ

### General Questions

**Q: Do I need quantum computing knowledge to play?**
A: No! The game teaches quantum concepts through gameplay. However, understanding basics helps appreciate the mechanics.

**Q: Is this a real quantum computing application?**
A: Yes! The game uses actual Qiskit quantum circuits, not simulations of quantum behavior.

**Q: Can I run this on a real quantum computer?**
A: Currently, the game uses Qiskit-Aer simulator. Integration with IBM Quantum hardware is planned for v2.0.

**Q: How long does a typical game session last?**
A: 15-30 minutes to complete 6 waves. You can pause anytime.

### Technical Questions

**Q: Why does installation take so long?**
A: Qiskit and its dependencies (scipy, numpy) are large packages. First install typically takes 5-10 minutes.

**Q: Can I modify game parameters?**
A: Yes! Edit `config/game_config.py` to change enemy health, tower damage, wave composition, etc.

**Q: Does the game have save/load functionality?**
A: Not currently. Each session is standalone. Feature planned for v1.1.

**Q: What's the performance impact of quantum simulation?**
A: Minimal! 2-qubit circuits are fast. Game maintains 60 FPS on most systems.

**Q: Can I add my own tower types?**
A: Yes! Create new tower class in `game_logic/tower.py` inheriting from `Tower` base class.

### Troubleshooting Questions

**Q: Game window is too large/small**
A: Edit `SCREEN_WIDTH` and `SCREEN_HEIGHT` in `config/game_config.py`

**Q: Getting "ImportError" despite installing requirements**
A: Ensure virtual environment is activated. Check with `which python` (should show venv path).

**Q: Pygame audio errors on Linux**
A: Install pulseaudio: `sudo apt install pulseaudio`

**Q: Game crashes on wave 5**
A: Possible memory issue. Try closing other applications or reducing `MAX_ENEMIES` in config.

---

## 📚 Additional Resources

### Learning Resources

- **Qiskit Documentation**: https://qiskit.org/documentation/
- **Pygame Documentation**: https://www.pygame.org/docs/
- **Quantum Computing for Everyone**: MIT OCW
- **IBM Quantum Learning**: https://learning.quantum.ibm.com/

### Community

- **GitHub Issues**: Report bugs or request features
- **GitHub Discussions**: Ask questions and share strategies
- **Discord** (coming soon): Real-time community chat

### Related Projects

- **Qiskit Games**: Other educational quantum games
- **Quantum Katas**: Quantum programming exercises
- **Quantum Education Resources**: Curated learning materials

---

## 🎓 Educational Use

### For Teachers

This game can be used in:
- **Physics classes**: Quantum mechanics introduction
- **Computer Science**: Quantum computing fundamentals
- **STEM workshops**: Interactive learning
- **Science fairs**: Project demonstration

### Lesson Plan Ideas

1. **Introduction to Superposition** (30 min)
   - Play first wave
   - Observe enemy behavior
   - Discuss quantum states

2. **Measurement and Collapse** (45 min)
   - Focus on measurement towers
   - Explain irreversibility
   - Compare to real quantum systems

3. **Entanglement** (60 min)
   - Use entanglement towers
   - Discuss spooky action at a distance
   - Compare to Bell pairs

### Classroom Activities

- Predict measurement outcomes
- Calculate probabilities
- Design optimal tower strategies
- Compare to classical tower defense

---

## 📝 Changelog

### Version 1.0.0 (Current)
- ✅ Initial release
- ✅ 4 tower types
- ✅ 4 enemy types
- ✅ 6 waves
- ✅ Quantum superposition mechanics
- ✅ Entanglement system
- ✅ Phase manipulation
- ✅ Tutorial system
- ✅ Full Qiskit integration

### Version 0.9.0 (Beta)
- Added teleportation tower
- Improved visual effects
- Performance optimizations
- Bug fixes

---

## 🤝 Support

Need help? Try these options:

1. **Check FAQ** (above)
2. **Search existing issues**: [GitHub Issues](https://github.com/N-Garai/Quantum-tower-defence/issues)
3. **Create new issue**: Provide error messages, system info, steps to reproduce
4. **Discussion forum**: [GitHub Discussions](https://github.com/N-Garai/Quantum-tower-defence/discussions)

When reporting issues, include:
- Operating System and version
- Python version (`python --version`)
- Error messages (full traceback)
- Steps to reproduce
- Screenshots if applicable

---

## ✅ Post-Installation Checklist

Before playing, verify:

- [ ] Python 3.9+ installed
- [ ] Git installed
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip list` shows qiskit, pygame)
- [ ] Test imports successful
- [ ] Game launches without errors
- [ ] Game window appears (1200x800)
- [ ] Main menu visible
- [ ] Can place towers
- [ ] Enemies spawn correctly

---

**Setup complete! Press SPACE to start your quantum adventure! 🎮⚛️**

---

*Last updated: November 7, 2025*
*For latest setup instructions, visit: https://github.com/N-Garai/Quantum-tower-defence*

# Create subdirectories
mkdir -p quantum_engine
mkdir -p game_logic
mkdir -p rendering
mkdir -p config
mkdir -p notebooks
mkdir -p assets/fonts
mkdir -p assets/sounds
mkdir -p assets/images
mkdir -p tests
mkdir -p docs
```

### Step 2: Place Downloaded Files

Move files to their respective directories:

```
quantum-tower-defense/
├── README.md                          ← Place here
├── requirements.txt                   ← Place here
├── directory-structure.md             ← Place here
├── main.py                           ← Rename main-game.py to this
│
├── quantum_engine/
│   ├── quantum_state.py              ← Place here
│   └── enemy_superposition.py        ← Place here
│
├── game_logic/
│   ├── tower.py                      ← Place here
│   ├── resource_manager.py           ← Place here
│   └── wave_manager.py               ← Place here
│
├── rendering/
│   └── game_renderer.py              ← Place here
│
├── config/
│   └── game_config.py                ← Place here
│
└── notebooks/
    ├── 01-quantum-concepts.ipynb     ← Place here
    ├── 02-game-prototype.ipynb       ← Place here
    └── 03-full-demo.ipynb            ← Place here
```

### Step 3: Create __init__.py Files

Create these 4 small initialization files:

**`quantum_engine/__init__.py`**
```python
from .quantum_state import QuantumStateManager
from .enemy_superposition import EnemySuperposition, EnemySpawner, EntangledEnemyPair

__all__ = ['QuantumStateManager', 'EnemySuperposition', 'EnemySpawner', 'EntangledEnemyPair']
```

**`game_logic/__init__.py`**
```python
from .resource_manager import ResourceManager
from .wave_manager import WaveManager
from .tower import TowerManager

__all__ = ['ResourceManager', 'WaveManager', 'TowerManager']
```

**`rendering/__init__.py`**
```python
from .game_renderer import GameRenderer

__all__ = ['GameRenderer']
```

**`config/__init__.py`**
```python
from .game_config import *
```

### Step 4: Create UI Manager

Create **`rendering/ui.py`** with this content:

```python
import pygame
from config.game_config import *

class UIManager:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
    
    def render_ui(self, resource_manager, selected_tower, wave_active, fps):
        # Bottom panel
        panel_rect = pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100)
        pygame.draw.rect(self.screen, COLORS['ui_panel'], panel_rect)
        
        # Money
        money_text = self.font.render(f"${resource_manager.money}", True, COLORS['ui_text'])
        self.screen.blit(money_text, (20, SCREEN_HEIGHT - 80))
        
        # Lives
        lives_text = self.font.render(f"❤️ {resource_manager.lives}", True, (255, 100, 100))
        self.screen.blit(lives_text, (20, SCREEN_HEIGHT - 50))
        
        # Coherence
        coherence_text = self.small_font.render(
            f"⚛️ {resource_manager.quantum_coherence:.1f}/{resource_manager.max_coherence}",
            True, COLORS['quantum_coherence']
        )
        self.screen.blit(coherence_text, (150, SCREEN_HEIGHT - 80))
        
        # Wave
        wave_text = self.small_font.render(f"Wave {resource_manager.wave}", True, COLORS['ui_text'])
        self.screen.blit(wave_text, (150, SCREEN_HEIGHT - 50))
        
        # FPS
        fps_text = self.small_font.render(f"FPS: {int(fps)}", True, (200, 200, 200))
        self.screen.blit(fps_text, (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 80))
        
        # Tower selection buttons
        tower_types = ['measurement', 'phase', 'entanglement', 'teleportation']
        tower_colors = [
            COLORS['tower_measurement'],
            COLORS['tower_phase'],
            COLORS['tower_entanglement'],
            COLORS['tower_teleportation']
        ]
        
        for i, (ttype, color) in enumerate(zip(tower_types, tower_colors)):
            x = 400 + i * 110
            y = SCREEN_HEIGHT - 90
            
            # Button background
            button_color = COLORS['button_hover'] if selected_tower == ttype else COLORS['button']
            button_rect = pygame.Rect(x, y, 100, 80)
            pygame.draw.rect(self.screen, button_color, button_rect, border_radius=8)
            pygame.draw.rect(self.screen, color, button_rect, width=3, border_radius=8)
            
            # Tower name (first letter)
            name_text = self.font.render(ttype[0].upper(), True, color)
            name_rect = name_text.get_rect(center=(x + 50, y + 25))
            self.screen.blit(name_text, name_rect)
            
            # Cost
            cost_text = self.small_font.render(f"${TOWER_CONFIG[ttype]['cost']}", True, COLORS['ui_text'])
            cost_rect = cost_text.get_rect(center=(x + 50, y + 50))
            self.screen.blit(cost_text, cost_rect)
            
            # Hotkey
            key_text = self.small_font.render(f"[{i+1}]", True, COLORS['quantum_coherence'])
            key_rect = key_text.get_rect(center=(x + 50, y + 70))
            self.screen.blit(key_text, key_rect)
        
        # Wave start button
        if not wave_active:
            wave_button_rect = pygame.Rect(SCREEN_WIDTH - 150, SCREEN_HEIGHT - 90, 130, 40)
            pygame.draw.rect(self.screen, (100, 200, 100), wave_button_rect, border_radius=8)
            wave_button_text = self.font.render("START WAVE", True, (0, 0, 0))
            wave_button_text_rect = wave_button_text.get_rect(center=wave_button_rect.center)
            self.screen.blit(wave_button_text, wave_button_text_rect)
    
    def handle_click(self, pos, game):
        # Handle tower button clicks
        if SCREEN_HEIGHT - 100 < pos[1] < SCREEN_HEIGHT:
            tower_types = ['measurement', 'phase', 'entanglement', 'teleportation']
            for i, ttype in enumerate(tower_types):
                x = 400 + i * 110
                if x < pos[0] < x + 100:
                    game.selected_tower_type = ttype
                    return
            
            # Wave start button
            if not game.wave_manager.wave_active:
                if SCREEN_WIDTH - 150 < pos[0] < SCREEN_WIDTH - 20:
                    if SCREEN_HEIGHT - 90 < pos[1] < SCREEN_HEIGHT - 50:
                        game.start_next_wave()
    
    def render_tutorial(self):
        # Tutorial overlay
        overlay = pygame.Surface((450, 350), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 220))
        pygame.draw.rect(overlay, COLORS['quantum_coherence'], overlay.get_rect(), width=3)
        
        tutorial_lines = [
            ("🎮 QUANTUM TOWER DEFENSE", True, 16),
            ("", False, 12),
            ("Controls:", True, 14),
            ("  1-4 Keys: Select tower type", False, 12),
            ("  Mouse: Place tower / Click UI", False, 12),
            ("  SPACE: Start next wave", False, 12),
            ("  ESC: Pause game", False, 12),
            ("  T: Toggle this tutorial", False, 12),
            ("  R: Restart (when game over)", False, 12),
            ("", False, 12),
            ("⚛️ Quantum Mechanics:", True, 14),
            ("  Unmeasured enemies are in", False, 12),
            ("  SUPERPOSITION on all paths!", False, 12),
            ("  Use Measurement Tower to", False, 12),
            ("  collapse them first!", False, 12),
        ]
        
        y = 15
        for text, is_bold, size in tutorial_lines:
            if text:
                font = pygame.font.Font(None, size)
                if is_bold:
                    font.set_bold(True)
                text_surface = font.render(text, True, COLORS['ui_text'])
                overlay.blit(text_surface, (20, y))
            y += size + 5
        
        self.screen.blit(overlay, (SCREEN_WIDTH - 480, 20))
```

### Step 5: Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Expected installations:**
- qiskit 1.0.0
- qiskit-aer 0.13.3
- pygame 2.5.2
- numpy 1.26.0
- matplotlib 3.8.0
- seaborn 0.13.0

### Step 6: Test Installation

Run this command to verify everything is installed:

```bash
python -c "import qiskit; import pygame; import numpy; print('✅ All dependencies installed!')"
```

### Step 7: Test with Notebooks First

```bash
jupyter notebook notebooks/01-quantum-concepts.ipynb
```

Work through the notebooks in order:
1. `01-quantum-concepts.ipynb` - Learn quantum mechanics
2. `02-game-prototype.ipynb` - Test game mechanics
3. `03-full-demo.ipynb` - See full visualization

### Step 8: Run the Game!

```bash
python main.py
```

**Game Controls:**
- **1-4**: Select tower type
- **Mouse Click**: Place tower
- **SPACE**: Start wave
- **ESC**: Pause
- **T**: Toggle tutorial
- **R**: Restart (after game over)

---

## 🎯 Quick Start Summary

```bash
# 1. Download all 14 files from this conversation
# 2. Create directory structure
mkdir quantum-tower-defense && cd quantum-tower-defense
mkdir -p quantum_engine game_logic rendering config notebooks

# 3. Place files in correct directories (see structure above)

# 4. Create 4 __init__.py files (see Step 3)

# 5. Create ui.py file (see Step 4)

# 6. Install dependencies
pip install -r requirements.txt

# 7. Run the game!
python main.py
```

---

## 📚 File Summary

| Category | Files | Status |
|----------|-------|--------|
| **Documentation** | 2 | ✅ Downloaded |
| **Core Game** | 7 | ✅ Downloaded |
| **Notebooks** | 3 | ✅ Downloaded |
| **Init Files** | 4 | 📝 Create (simple) |
| **UI Manager** | 1 | 📝 Create (copy code) |
| **Total** | **17 files** | **14 ready + 3 to create** |

---

## 🎓 Learning Path

1. **Start with Notebooks** (30 minutes)
   - Understand quantum concepts
   - Test mechanics interactively
   - See visualizations

2. **Play the Game** (1 hour)
   - Learn through gameplay
   - Experiment with strategies
   - Observe quantum effects

3. **Read the Code** (2 hours)
   - Understand implementation
   - Modify parameters
   - Add features

---

## 🐛 Troubleshooting

### Import Errors
```bash
# Make sure you created all __init__.py files
# Check that main.py is in the root directory
```

### Qiskit Installation Issues
```bash
# Try installing specific version
pip install qiskit==1.0.0 qiskit-aer==0.13.3
```

### Pygame Not Starting
```bash
# On Mac, you might need:
pip install pygame --pre --user

# On Linux:
sudo apt-get install python3-pygame
```

### Module Not Found
```bash
# Make sure you're in the project root directory
cd quantum-tower-defense
python main.py
```

---

## ✅ Verification Checklist

Before running, verify:

- [ ] All 14 downloaded files are in correct directories
- [ ] Created 4 `__init__.py` files
- [ ] Created `ui.py` file
- [ ] Installed dependencies from `requirements.txt`
- [ ] Python 3.9+ is installed
- [ ] In the project root directory
- [ ] `main.py` exists (renamed from `main-game.py`)

---

## 🚀 You're Ready!

Once all files are in place and dependencies are installed:

```bash
python main.py
```

**Enjoy your quantum tower defense game powered by IBM Qiskit!** 🎮⚛️

---

## 📞 Support

- Check `README.md` for detailed documentation
- Review `directory-structure.md` for file organization
- Run notebooks for interactive tutorials
- Read quantum_mechanics concepts in notebooks

**Happy Quantum Gaming!** ⚛️🎮
