# main.py

import sys
# Import the safe_divide function from our robust_division_calculator module
from robust_division_calculator import safe_divide

def main():
    """
    Parses command-line arguments for numerator and denominator,
    calls safe_divide, and prints the result.
    """
    # Check if the correct number of command-line arguments are provided.
    # sys.argv[0] is the script name itself, so we expect 3 total elements.
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1) # Exit with an error code

    # Extract numerator and denominator from command-line arguments.
    # They are initially strings.
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function and store its string result.
    result_message = safe_divide(numerator, denominator)

    # Print the result returned by safe_divide.
    print(result_message)

# Ensure main() is called when the script is executed directly.
if __name__ == "__main__":
    main()