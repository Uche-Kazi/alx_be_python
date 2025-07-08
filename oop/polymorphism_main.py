# main.py

# Import all necessary classes from the polymorphism_demo module
# No need to import math here explicitly as it's used within polymorphism_demo.py
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    """
    Demonstrates polymorphism by calculating and printing areas of different shapes.
    """
    # Create a list containing instances of different shape classes.
    # Due to polymorphism, we can treat them all as generic 'Shape' objects
    # when iterating and calling the 'area()' method.
    shapes = [
        Rectangle(10, 5), # A rectangle with length 10 and width 5
        Circle(7)         # A circle with radius 7
    ]

    print("--- Calculating Areas ---")
    # Iterate through the list of shapes
    for shape in shapes:
        # The 'area()' method is called polymorphically.
        # Python automatically determines whether to call Rectangle's area()
        # or Circle's area() based on the actual object type at runtime.
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

    print("\n--- Demonstration Complete ---")

if __name__ == "__main__":
    main()