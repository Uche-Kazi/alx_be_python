def main():
    print("Arithmetic Operations")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
        
        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers for numerical values.")
        
if __name__ == "__main__":
    main()