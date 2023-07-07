import unittest
from math_functions import Math

class MathFunctionsTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Math.add(2,3), 5)

    def test_sub(self):
        self.assertEqual(Math.add(4,3), 1)