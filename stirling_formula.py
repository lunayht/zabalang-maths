import matplotlib.pyplot as plt
import numpy as np

from scipy.special import gamma, factorial


def stirling_function(n: np.ndarray):
    approximate_nfac = np.multiply(n ** (n + 1 / 2), np.exp(-n)) * np.sqrt(2 * np.pi)
    return approximate_nfac


if __name__ == "__main__":
    values = np.linspace(0, 3, 2000)
    factorial_values = factorial([0, 1, 2, 3])
    gamma_values = gamma(values + 1)
    stirling_values = stirling_function(values)
    plt.scatter([0, 1, 2, 3], factorial_values, label="n!", marker="o", c="r")
    plt.plot(values, gamma_values, label="Γ(n+1)")
    plt.plot(values, stirling_values, label="Stirling's Formula")
    plt.ylabel("f(n)")
    plt.xlabel("n")
    plt.grid(True)
    plt.ylim(0, 6)
    plt.legend()
    plt.show()
