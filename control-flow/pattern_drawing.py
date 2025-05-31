print("--- Pattern Drawing ---")

try:
    size = int(input("Enter the size of the pattern: "))

    if size <= 0:
        print("Please enter a positive integer for the pattern size.")

except ValueError:
    print("Invalid input. Please enter a whole number.")
exit()

row_count = 0

while row_count < size:

    for col_count in range(size):

        print("*", end="")
    
    print()

    row_count += 1