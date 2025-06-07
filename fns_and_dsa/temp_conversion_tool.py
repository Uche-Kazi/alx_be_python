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
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  """
  Handles user interaction for temperature conversion.
  Prompts for temperature and unit, then displays the converted temperature.
  Handles invalid temperature input.
  """
  try:
    temp_input_str = input("Enter the temperature to convert: ")
    temperature = float(temp_input_str)

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
      converted_temp = convert_to_celsius(temperature)
      print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
      converted_temp = convert_to_fahrenheit(temperature)
      print(f"{temperature}°C is {converted_temp}°F")
    else:
      print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

  except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
  main()