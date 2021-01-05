# Mathematics
My mathematics repo for various experiments.

## Getting Started
### Prerequisites
- Python 3.6 or later

### Installation
Run ```pip3 install -r requirements.txt``` to install following packages:
- black (Python code formatter)
- pytest (Python test suite)
- numpy
- matplotlib

### Pytest Test Suite
```bash
$ pytest
```
## List of Topics
1. **Coin Tossing Game** 
    - 2 players, each of them has their own coin. Note that all coins are fair.
    - Rules:
        - A wins on contiguous Head Head
        - B wins on Head Tail
    - Question: Does P[A wins] = P[B wins]? Is this a fair game?

2. **Stirling's Formula**
    - <img src="https://render.githubusercontent.com/render/math?math=n! \sim \sqrt{2\pi}n^{n%2B\frac{1}{2}}e^{-n}">
    - Approximation for factorials. A good approximation as n gets large, the proportional error goes to zero. 