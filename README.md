# Mathematics
Mathematics repo for various experiments.

## Getting Started
### Prerequisites
- Python 3.6 or later

### Installation
Run ```pip3 install -r requirements.txt``` to install following packages:
- black (Python code formatter)
- pytest (Python test suite)
- numpy
- matplotlib
- scipy

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
    - Approximation for factorials. A good approximation as n gets large, the proportional error goes to zero. 
    - Read more: https://en.wikipedia.org/wiki/Stirling%27s_approximation

3. **Poisson Arrival Process/ Poisson Traffic**
    - Arrivals occur in a memoryless manner, a stochastic process. 
    - Number of arrivals during time interval has Poisson distribution.
    - A memoryless pdf is an exponential pdf (inter arrival time is exponential)
    - Queueing theory to model random process: arrival of customers in a store, occurance of earthquakes, telephone call attempts.
    - Read more: http://www.wirelesscommunication.nl/reference/appendix/poisson.htm 