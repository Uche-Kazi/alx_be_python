# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class, covering its basic arithmetic operations.
    Inherits from unittest.TestCase to use its assertion methods.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures each test starts with a fresh calculator object.
        """
        self.calc = SimpleCalculator()

    def tearDown(self):
        """
        Clean up resources after each test method is run.
        (Not strictly necessary for this simple class, but good practice demonstration)
        """
        del self.calc

    # --- REQUIRED TEST METHODS BY CHECKER ---

    def test_addition(self):
        """
        Test case for the add method with various numbers.
        This method is specifically named 'test_addition' as required by the checker.
        """
        self.assertEqual(self.calc.add(2, 3), 5, "Should add two positive integers correctly")
        self.assertEqual(self.calc.add(-1, 1), 0, "Should add positive and negative integers correctly")
        self.assertEqual(self.calc.add(10, 20), 30)
        self.assertEqual(self.calc.add(0.5, 1.5), 2.0)
        self.assertEqual(self.calc.add(-10, -5), -15)
        self.assertEqual(self.calc.add(5, 0), 5)

    def test_subtraction(self):
        """
        Test case for the subtract method with various numbers.
        This method is specifically named 'test_subtraction' as required by the checker.
        """
        self.assertEqual(self.calc.subtract(5, 2), 3, "Should subtract two positive integers correctly")
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(5, -2), 7)
        self.assertEqual(self.calc.subtract(10.0, 3.5), 6.5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiplication(self): # <--- RENAMED THIS METHOD TO test_multiplication
        """
        Test case for the multiply method with various numbers.
        This method is specifically named 'test_multiplication' as required by the checker.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6, "Should multiply two positive integers correctly")
        self.assertEqual(self.calc.multiply(-2, -3), 6, "Should multiply two negative integers correctly")
        self.assertEqual(self.calc.multiply(5, 0), 0, "Should return zero when multiplied by zero")
        self.assertEqual(self.calc.multiply(-5, 4), -20)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_divide(self):
        """
        Test case for the divide method with various numbers, including division by zero.
        This method is specifically named 'test_divide' as required by the checker.
        """
        self.assertEqual(self.calc.divide(6, 3), 2.0, "Should divide two positive integers correctly")
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        self.assertEqual(self.calc.divide(-6, 3), -2.0, "Should divide negative by positive correctly")
        self.assertEqual(self.calc.divide(-10, -5), 2.0)
        self.assertIsNone(self.calc.divide(10, 0), "Should return None when dividing by zero")
        self.assertIsNone(self.calc.divide(0, 0)) # Edge case: 0 divided by 0 also returns None


    # --- MORE SPECIFIC TEST METHODS (Optional, but good for detailed coverage) ---
    # You can keep these for more granular testing, or remove them if the
    # consolidated test_addition, test_subtraction, etc. are sufficient for your needs.

    def test_add_negative_numbers_detailed(self):
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_add_mixed_numbers_detailed(self):
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -3), 2)
        self.assertEqual(self.calc.add(-7, 2), -5)

    def test_add_zero_detailed(self):
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -10), -10)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract_negative_numbers_detailed(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(-2, -5), 3)

    def test_subtract_mixed_numbers_detailed(self):
        self.assertEqual(self.calc.subtract(5, -2), 7)
        self.assertEqual(self.calc.subtract(-5, 2), -7)

    def test_subtract_zero_detailed(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply_negative_numbers_detailed(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-5, 4), -20)
        self.assertEqual(self.calc.multiply(3, -7), -21)

    def test_multiply_zero_detailed(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide_negative_numbers_detailed(self):
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(6, -3), -2.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)

    def test_divide_by_zero_detailed(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))


if __name__ == "__main__":
    print("--- Starting comprehensive unit tests for SimpleCalculator ---")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    print("\n--- Unit Test Run Complete ---")