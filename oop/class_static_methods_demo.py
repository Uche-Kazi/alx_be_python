# class_static_methods_demo.py

class Calculator:
    """
    A class demonstrating static and class methods.
    """
    calculation_type = "Arithmetic Operations" # Class attribute

    @staticmethod
    def add(a, b):
        """
        A static method that sums two numbers.
        It doesn't use 'self' or 'cls'.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that multiplies two numbers and prints the class attribute.
        It receives 'cls' (the class itself) as its first argument.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b