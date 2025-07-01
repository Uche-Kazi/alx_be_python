print("--- Simple Calculator ---")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
	print("Invalid number input. Please enter numeric values.")
exit()

operation = input("Choose the operation (+, -, *, /): ").strip()

result = None

match operation:
	case '+':
		result = num1 + num2
	case '-':
		result = num1 - num2
	case '*':
		result = num1 * num2
	case '/':

		if num2 == 0:
			print("Cannot divide by zero.")

		else:
			result = num1 / num2
	case _:
		print("Invalid operation. Please choose from +, -, *, or /.")


if result is not None:
	print(f"The result is {result}.")
