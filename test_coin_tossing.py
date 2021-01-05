import numpy as np

from coin_tossing import uT_A, uH_A, Q_A, Q_B


class TestCoinTossing:
    def test_uT_A(self):
        a = np.arange(1, 5)
        b = np.array([1, 2, 3, 5], dtype=int)
        comparison = uT_A(a) == b
        equal_arrays = comparison.all()
        assert (
            equal_arrays == True
        ), "expect function uT_A to return Fibonacci sequence."

    def test_uH_A(self):
        a = np.arange(1, 5)
        b = np.array([1, 1, 2, 3], dtype=int)
        comparison = uH_A(a) == b
        equal_arrays = comparison.all()
        assert (
            equal_arrays == True
        ), "expect function uH_A to return Fibonacci sequence of k-1"

    def test_Q_A(self):
        a = np.arange(1, 5)
        b = np.array([0, 0.25, 0.375, 0.5], dtype=float)
        comparison = Q_A(a) == b
        equal_arrays = comparison.all()
        assert (
            equal_arrays == True
        ), "expect function Q_A to return 1 - (uH_A + uT_A)/2**k"

    def test_Q_B(self):
        a = np.arange(1, 5)
        b = np.array([0, 0.25, 0.5, 0.6875], dtype=float)
        comparison = Q_B(a) == b
        equal_arrays = comparison.all()
        assert (
            equal_arrays == True
        ), "expect function Q_B to return 1 - (k + 1)/2**k"
