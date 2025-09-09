# DSP Python Implementations

A collection of Digital Signal Processing (DSP) algorithms and filters implemented in Python, designed for educational purposes and practical applications.

## Overview

This repository contains Python implementations of various DSP concepts, filters, and algorithms. Each implementation includes visualization tools and comprehensive examples to help understand the underlying mathematical concepts and their practical applications.

## Features

- 🔧 **Modular Design**: Each DSP component is implemented as a standalone module
- 📊 **Visualization**: Built-in plotting functions for signal analysis
- 📚 **Educational**: Well-commented code with clear explanations
- 🧮 **Mathematical Accuracy**: Implementations follow standard DSP theory
- 🚀 **Performance**: Optimized using NumPy for efficient computation

## Current Implementations

### 1. Accumulator (`Accumulator.py`)
A basic accumulator implementation that demonstrates:
- Synchronous and asynchronous operations
- DAC (Digital-to-Analog Converter) translation
- Signal accumulation over time
- Visualization of input vs output signals

**Features:**
- Configurable bit depth
- Real-time signal processing simulation
- Statistical analysis of input/output signals
- Time-domain plotting

## Prerequisites

### System Requirements
- macOS (optimized for Apple Silicon)
- Python 3.12+
- Conda package manager

### Dependencies
The project uses a curated set of scientific computing packages:
- **NumPy**: Numerical computing
- **Matplotlib**: Plotting and visualization
- **SciPy**: Scientific computing algorithms
- **Pandas**: Data manipulation
- **Jupyter**: Interactive development
- **Spyder**: IDE for scientific computing

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd DSP_Python_Implementations
```

### 2. Create Conda Environment
For macOS (Apple Silicon):
```bash
conda env create -f python_dsp-macOS_Mx.yml
conda activate python_dsp
```

For macOS (Intel):
```bash
conda env create -f python_dsp-macOS14Mx.yml
conda activate python_dsp
```

### 3. Verify Installation
```bash
python -c "import numpy, matplotlib, scipy; print('All dependencies installed successfully!')"
```

## Usage

### Running the Accumulator Example
```bash
python Accumulator.py
```

Or use Jupyter notebook/VS Code interactive mode:
1. Open `Accumulator.py`
2. Execute each cell (`# %%`) sequentially
3. View the generated plots and statistics

### Example Output
The accumulator will generate:
- Input signal plot (constant value over time)
- DAC output plot (accumulated signal over time)
- Statistical summary of both signals

## Project Structure

```
DSP_Python_Implementations/
├── README.md                    # This file
├── Accumulator.py              # Accumulator implementation
├── python_dsp-macOS_Mx.yml     # Conda environment (Apple Silicon)
├── python_dsp-macOS14Mx.yml    # Conda environment (Intel)
└── (future implementations)
```

## Planned Implementations

- [ ] **FIR Filters**: Finite Impulse Response filters
- [ ] **IIR Filters**: Infinite Impulse Response filters
- [ ] **FFT/DFT**: Fast Fourier Transform implementations
- [ ] **Window Functions**: Hamming, Hanning, Blackman, etc.
- [ ] **Digital Oscillators**: Sine, cosine, and complex oscillators
- [ ] **Noise Generators**: White, pink, and colored noise
- [ ] **Adaptive Filters**: LMS, RLS algorithms
- [ ] **Multirate DSP**: Decimation and interpolation
- [ ] **Spectral Analysis**: Power spectral density, spectrograms

## Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use descriptive variable names
- Include comprehensive docstrings
- Add inline comments for complex algorithms

### Testing
- Include example usage in each implementation
- Provide visualization for verification
- Add statistical analysis where applicable

### Documentation
- Document mathematical foundations
- Include references to DSP literature
- Provide usage examples

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-filter`)
3. Implement your DSP algorithm following the project guidelines
4. Add comprehensive documentation and examples
5. Test your implementation thoroughly
6. Submit a pull request

## References

- **Digital Signal Processing** by John G. Proakis and Dimitris G. Manolakis
- **Understanding Digital Signal Processing** by Richard G. Lyons
- **Discrete-Time Signal Processing** by Alan V. Oppenheim and Ronald W. Schafer

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions, suggestions, or contributions, please open an issue or submit a pull request.

---

**Note**: This repository is primarily educational and may not be optimized for production use. For production applications, consider using established DSP libraries like SciPy's signal processing module.
# Digital-Signal-Processing-in-Python
