# Root Algorithmic Analysis

A comprehensive exploration of mathematical root computations—primarily square roots—implemented from first principles in both JavaScript and Python.

## 1. Project Overview

This project aims to re-implement fundamental mathematical functions from scratch—without relying on built-in libraries—using JavaScript and Python.
It focuses on numerical root-finding and related core computations, reconstructed manually to gain a deeper understanding of how such operations work internally.

Unlike relying on high-level functions like `Math.sqrt()` or `** 0.5`, this project reconstructs these methods from first principles. This deliberate avoidance of built-in math functions serves two key goals:

1. **Mathematical Exploration**: To study and understand the underlying numerical methods—such as iteration, convergence, and precision—involved in computing roots, powers, and transcendental functions.
2. **Cross-language Consistency**: By avoiding platform-specific math libraries, the implementations provide more transparent and consistent numerical behavior across JavaScript and Python.

All algorithms are implemented manually without the use of generative AI or automated code tools. Every line of logic was hand-crafted to encourage algorithmic thinking and reinforce mathematical insight through programming.

### Implemented Features

- **Root-finding algorithms**:
  - Babylonian method
  - Newton–Raphson method
  - Binary search method
- **Exponentiation** (`pow`):
  - Integer powers via fast exponentiation
  - Fractional powers via iterative methods
- **π Approximation** using Ramanujan’s infinite series
- **Trigonometric functions** (`sin`, `cos`, `atan`) via Taylor expansion
- **Complex root extraction** using De Moivre’s theorem
- **Utility methods**:
  - Absolute value
  - Factorial
  - Greatest common divisor (GCD)
  - Decimal → fraction conversion

Each algorithm is implemented independently in both JavaScript and Python for language-level comparison and numerical behavior analysis.

## 2. Motivation

While high-level functions like `Math.sqrt()` or `** 0.5` are convenient, this project asks:

> *What happens under the hood of these “black box” mathematical methods?*

By reconstructing them manually, the project explores:
- The mathematical principles behind root-finding and function approximation
- The numerical behavior and convergence of different methods
- How the same algorithm behaves differently in JavaScript vs Python
- Language-level quirks and floating-point behavior in each

This also serves as a learning tool to deepen understanding of both math and programming.

## 3. Algorithms and Methods

### 3.1 Root Finding

- **Babylonian Method**  
  Iteratively refines the estimate `x` using:  
  `x = (x + n / x) / 2`

- **Newton–Raphson Method**  
  Solves `x^r = n` by updating:  
  `x = x - (x^r - n) / (r * x^(r - 1))`

### 3.2 Exponentiation (`pow`)

- Integer powers are handled with fast exponentiation (`O(log n)`).
- Rational powers (like `x^(1/2)`) are computed by solving `x^r = n` using iterative methods (Newton or binary).

### 3.3 π Approximation

Ramanujan's formula:

π ≈ 1 / [ (2√2 / 9801) × Σ ( (4k)! (1103 + 26390k) ) / ( (k!)⁴ 396^(4k) ) ]

Very rapid convergence: accurate to many digits with just a few terms.

### 3.4 Trigonometric Functions

- **sin(x)** and **cos(x)** use Maclaurin/Taylor series up to the 99th degree.
- **atan(x)**:
  - For |x| ≤ 1: Taylor expansion directly.
  - For |x| > 1: Uses identity: `atan(x) = π/2 - atan(1/x)` to ensure convergence.

### 3.5 Complex Roots

Given a complex number `z = a + bi`, compute all `n` roots using:

1. Convert to polar form: `r = √(a² + b²)`, `θ = atan(b / a)`
2. Apply De Moivre’s theorem:

root_k = r^(1/n) × [cos((θ + 2πk)/n) + i·sin((θ + 2πk)/n)]

Returns results either as:
- Fixed-decimal approximation (default 3 places)
- Reduced fractions (e.g., `"3/4"`), depending on output mode

### 3.6 Utilities

- **abs(x)**: Returns `x` if non-negative, `-x` otherwise
- **gcd(a, b, ...)**: Euclidean algorithm, optionally applied to arrays
- **fac(n)**: Computes `n!` using iteration
- **toFrac(d)**: Converts decimal to lowest-term fraction (e.g., `0.75 → "3/4"`)

## 4. Environment

- **JavaScript**: Vanilla JS (works in any modern JS engine including V8, Node.js, or browsers)  
- **Python**: Pure Python 3. No external libraries used.

Both environments use native syntax and arithmetic. No external packages are required in either language.

## 5. License

This project is released under the MIT License. See `LICENSE` for full terms.

## 6. Author

[**seojun0602**](https://github.com/seojun0602)