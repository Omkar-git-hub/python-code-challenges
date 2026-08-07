import unittest
from main import swap_variables

class TestSwapVariables(unittest.TestCase):
    def test_swap(self):
        a = 5
        b = 10
        swapped_a, swapped_b = swap_variables(a, b)
        self.assertEqual(swapped_a, b)
        self.assertEqual(swapped_b, a)

if __name__ == "__main__":
    unittest.main()