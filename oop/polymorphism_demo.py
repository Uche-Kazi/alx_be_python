# polymorphism_demo.py

import math # Required for math.pi in the Circle class

class Shape:
    """
    Base class for geometric shapes.
    Defines a generic area method that must be overridden by derived classes.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by concrete shape classes.
        Raises NotImplementedError if not overridden.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    Calculates its area based on length and width.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a new Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Overrides the area method from the Shape base class.
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    Calculates its area based on its radius.
    """
    def __init__(self, radius: float):
        """
        Initializes a new Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Overrides the area method from the Shape base class.
        Calculates the area of the circle using math.pi.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)