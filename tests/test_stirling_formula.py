import numpy as np

from stirling_formula import stirling_function


class TestStirlingFunction:
    def test_stirling_func_single_value(self):
        value = 2
        assert (
            abs(stirling_function(value) - 2) < 1
        ), "expect stirling function to return approximate n factorial value (2)"

    def test_stirling_func_multiple_values(self):
        values = np.array([2, 3, 4])
        comparison = (stirling_function(values) - np.array([2, 6, 24])) < 1
        equal_arrays = comparison.all()
        assert (
            equal_arrays == True
        ), "expect stirling function to return approximate n factorial values ([2, 6, 24])"
