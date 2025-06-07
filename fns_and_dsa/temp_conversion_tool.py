# temp_conversion_tool.py

# Define Global Conversion Factors
# These variables are defined at the top level of the script (global scope).
# They are accessible for reading by all functions within this module without
# needing special keywords.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Accessing the global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Accessing the global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Handles user interaction for temperature conversion.
    Prompts for temperature and unit, then displays the converted temperature.
    Handles invalid temperature input.
    """
    try:
        # Prompt user for temperature and attempt to convert it to a float.
        # This conversion will raise a ValueError if the input is not numeric.
        temp_input_str = input("Enter the temperature to convert: ")
        temperature = float(temp_input_str)

        # Prompt user for the unit and convert to uppercase for consistent comparison
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            # Handle cases where the unit input is not 'C' or 'F'
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        # Catch the ValueError if float(temp_input_str) fails,
        # and print the specific error message as required.
        print("Invalid temperature. Please enter a numeric value.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point for the script execution
if __name__ == "__main__":
    main()