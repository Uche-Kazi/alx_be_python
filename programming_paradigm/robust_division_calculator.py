# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division of two numbers, handling ZeroDivisionError and ValueError.

    Args:
        numerator (str): The numerator as a string (from command line).
        denominator (str): The denominator as a string (from command line).

    Returns:
        str: A message indicating the result of the division or an error message.
    """
    try:
        # Attempt to convert both inputs to floats.
        # This will raise a ValueError if conversion fails (non-numeric input).
        num = float(numerator)
        den = float(denominator)

        # Attempt to perform the division.
        # This will raise a ZeroDivisionError if denominator is 0.
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            # Handle the case where the denominator is zero
            return "Error: Cannot divide by zero."

    except ValueError:
        # Handle the case where either input is non-numeric
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Catch any other unexpected errors, though unlikely for this simple case
        return f"An unexpected error occurred: {e}"