# test_simple_calculator.py

import unittest
# Import the SimpleCalculator class from the simple_calculator.py file
# Ensure simple_calculator.py is in the same directory as this test file
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
        print(f"\n--- Setting up calculator for a new test ---") # Optional: for verbose output during setup

    def tearDown(self):
        """
        Clean up resources after each test method is run.
        (Not strictly necessary for this simple class, but good practice demonstration)
        """
        del self.calc # Delete the calculator instance
        print(f"--- Tearing down calculator after test ---") # Optional: for verbose output during teardown

    def test_add_positive_numbers(self):
        """
        Test case for the add method with two positive numbers.
        """
        print("Running test_add_positive_numbers...")
        self.assertEqual(self.calc.add(2, 3), 5, "Should add two positive integers correctly")
        self.assertEqual(self.calc.add(10, 20), 30)
        self.assertEqual(self.calc.add(0.5, 1.5), 2.0)

    def test_add_negative_numbers(self):
        """
        Test case for the add method with two negative numbers.
        """
        print("Running test_add_negative_numbers...")
        self.assertEqual(self.calc.add(-1, -1), -2, "Should add two negative integers correctly")
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_add_mixed_numbers(self):
        """
        Test case for the add method with a positive and a negative number.
        """
        print("Running test_add_mixed_numbers...")
        self.assertEqual(self.calc.add(-1, 1), 0, "Should add positive and negative integers correctly")
        self.assertEqual(self.calc.add(5, -3), 2)
        self.assertEqual(self.calc.add(-7, 2), -5)

    def test_add_zero(self):
        """
        Test case for the add method with zero.
        """
        print("Running test_add_zero...")
        self.assertEqual(self.calc.add(5, 0), 5, "Should correctly add zero to a number")
        self.assertEqual(self.calc.add(0, -10), -10)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract_positive_numbers(self):
        """
        Test case for the subtract method with positive numbers.
        """
        print("Running test_subtract_positive_numbers...")
        self.assertEqual(self.calc.subtract(5, 2), 3, "Should subtract two positive integers correctly")
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(10.0, 3.5), 6.5)

    def test_subtract_negative_numbers(self):
        """
        Test case for the subtract method with negative numbers.
        """
        print("Running test_subtract_negative_numbers...")
        self.assertEqual(self.calc.subtract(-5, -2), -3, "Should subtract two negative integers correctly")
        self.assertEqual(self.calc.subtract(-2, -5), 3)

    def test_subtract_mixed_numbers(self):
        """
        Test case for the subtract method with mixed positive and negative numbers.
        """
        print("Running test_subtract_mixed_numbers...")
        self.assertEqual(self.calc.subtract(5, -2), 7, "Should subtract a negative from a positive correctly")
        self.assertEqual(self.calc.subtract(-5, 2), -7)

    def test_subtract_zero(self):
        """
        Test case for the subtract method with zero.
        """
        print("Running test_subtract_zero...")
        self.assertEqual(self.calc.subtract(5, 0), 5, "Should subtract zero correctly")
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply_positive_numbers(self):
        """
        Test case for the multiply method with positive numbers.
        """
        print("Running test_multiply_positive_numbers...")
        self.assertEqual(self.calc.multiply(2, 3), 6, "Should multiply two positive integers correctly")
        self.assertEqual(self.calc.multiply(10, 10), 100)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_multiply_negative_numbers(self):
        """
        Test case for the multiply method with negative numbers.
        """
        print("Running test_multiply_negative_numbers...")
        self.assertEqual(self.calc.multiply(-2, -3), 6, "Should multiply two negative integers correctly")
        self.assertEqual(self.calc.multiply(-5, 4), -20)
        self.assertEqual(self.calc.multiply(3, -7), -21)

    def test_multiply_zero(self):
        """
        Test case for the multiply method with zero.
        """
        print("Running test_multiply_zero...")
        self.assertEqual(self.calc.multiply(5, 0), 0, "Should return zero when multiplied by zero")
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide_positive_numbers(self):
        """
        Test case for the divide method with positive numbers.
        """
        print("Running test_divide_positive_numbers...")
        self.assertEqual(self.calc.divide(6, 3), 2.0, "Should divide two positive integers correctly")
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        self.assertEqual(self.calc.divide(10.0, 5.0), 2.0)

    def test_divide_negative_numbers(self):
        """
        Test case for the divide method with negative numbers.
        """
        print("Running test_divide_negative_numbers...")
        self.assertEqual(self.calc.divide(-6, 3), -2.0, "Should divide negative by positive correctly")
        self.assertEqual(self.calc.divide(6, -3), -2.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)

    def test_divide_by_zero(self):
        """
        Test case for the divide method when the denominator is zero.
        The SimpleCalculator's divide method is designed to return None for this case.
        """
        print("Running test_divide_by_zero...")
        self.assertIsNone(self.calc.divide(10, 0), "Should return None when dividing by zero")
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Edge case: 0 divided by 0 also returns None as per class spec


# This block allows you to run all tests in this file when executed directly.
if __name__ == "__main__":
    print("--- Starting comprehensive unit tests for SimpleCalculator ---")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    print("\n--- Unit Test Run Complete ---")