"""Coin Tossing Game

2 players. All coins are fair. Each player has their own coin.
Question: Is this a fair game? Does P[A wins] = P[B wins] ?
Answer: Not a fair game.
"""
import matplotlib.pyplot as plt
import numpy as np


def uT_A(k: np.ndarray):
    """Fibonacci sequence"""
    theta = lambda a: ((1 + a * 5 ** (1 / 2)) / 2) ** (k + 1)
    seq = (theta(1) - theta(-1)) / 5 ** (1 / 2)
    return np.array(seq, dtype=int)


def uH_A(k: np.ndarray):
    return uT_A(k - 1)


def Q_A(k: np.ndarray):
    numerator = 2 ** k - uH_A(k) - uT_A(k)
    answer = numerator / (2 ** k)
    return answer


def Q_B(k: np.ndarray):
    uH_B = k
    uT_B = 1
    numerator = 2 ** k - uH_B - uT_B
    answer = numerator / (2 ** k)
    return answer


def P_A(k: np.ndarray):
    return np.subtract(Q_A(k), Q_A(k - 1))


def P_B(k: np.ndarray):
    return np.subtract(Q_B(k), Q_B(k - 1))


if __name__ == "__main__":
    k = 20
    K_np = np.arange(1, k + 1)
    P_Awins = np.multiply(P_A(K_np), np.subtract(1, Q_B(K_np)))
    P_Bwins = np.multiply(P_B(K_np), np.subtract(1, Q_A(K_np)))
    P_tie = np.multiply(P_A(K_np), P_B(K_np))

    print(f"P[A wins] = {np.sum(P_Awins)}")
    print(f"P[B wins] = {np.sum(P_Bwins)}")
    print(f"P[tie] = {np.sum(P_tie)}")

    plt.plot(P_Awins, label="P[A wins]", marker="o")
    plt.plot(P_Bwins, label="P[B wins]", marker="o")
    plt.plot(P_tie, label="P[tie]", marker="o")
    plt.ylabel("Probability a player wins")
    plt.xlabel("k")
    plt.legend()
    plt.show()
