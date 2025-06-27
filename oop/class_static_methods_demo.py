# class_static_methods_demo.py

class Calculator:
    """
    A class demonstrating the usage and differences between
    static methods and class methods in Python.
    """

    # Class attribute: shared by all instances of the class and the class itself.
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: int, b: int) -> int:
        """
        A static method that returns the sum of two numbers.
        It does not receive 'self' or 'cls' and cannot access instance
        or class-specific attributes directly. It behaves like a regular function
        that happens to be inside the class's namespace.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a: int, b: int) -> int:
        """
        A class method that returns the product of two numbers.
        It receives the class itself as the first argument (conventionally 'cls').
        This allows it to access and modify class-level attributes.

        Args:
            cls (type): The class itself (e.g., Calculator).
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The product of a and b.
        """
        # Accessing the class attribute 'calculation_type' using 'cls'
        print(f"Calculation type: {cls.calculation_type}")
        return a * b