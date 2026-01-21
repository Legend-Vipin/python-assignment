# Python Assignment
These are all questions for basic Python. 
python 3.12.8 use in the all codes.
This repository contains assignments and projects related to Python programming. The assignments cover various topics and are designed to help improve your Python coding skills.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started
To get a local copy of this project up and running, follow these simple steps.

## Prerequisites
- Python 3.12 or higher
- uv (recommended) or pip package manager

You can download Python from [Python Official Website](https://www.python.org/).  
You can install uv from [UV Installation Guide](https://github.com/astral-sh/uv).

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Legend-Vipin/python-assignment.git
    ```

2. Navigate to the project directory:
    ```bash
    cd python-assignment
    ```

3. (Optional) Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. Install the required dependencies:

    **Using uv (recommended)**:
    ```bash
    uv pip install -r requirements.txt
    ```

    **Or using pip**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running Individual Modules

You can run Python scripts using the module syntax:

**Basics** (Fundamental concepts):
```bash
python -m src.basics.1_simple_interest
python -m src.basics.4_fibonacci_series
python -m src.basics.10_string_methods_demo
```

**OOP** (Object-Oriented Programming):
```bash
python -m src.oop.5_polymorphism
python -m src.oop.2_inheritance
python -m src.oop.10_abstract_class
```

**Algorithms**:
```bash
python -m src.algorithms.9_search_algorithms
python -m src.algorithms.11_sorting_merging
python -m src.algorithms.12_tower_of_hanoi
```

**Projects**:
```bash
python -m src.projects.1_force_calculator
python -m src.projects.3_electricity_bill
python -m src.projects.2_area_lab
```

### Importing as a Library

You can also import functions/classes from the modules:
```python
from src.basics import simple_interest
from src.oop import polymorphism
from src.algorithms import search_algorithms
```

## Repository Structure

```
python-assignment/
├── src/
│   ├── basics/          # Fundamental Python concepts (11 files)
│   ├── oop/             # Object-Oriented Programming (17 files)
│   ├── algorithms/      # Algorithms & problem-solving (13 files)
│   └── projects/        # Utility projects (7 files)
├── README.md
├── requirements.txt
└── pyproject.toml
```