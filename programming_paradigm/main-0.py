# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Initialize the bank account with an example starting balance
    # You can change this value for testing different scenarios.
    account = BankAccount(100.0)

    # Check if enough command-line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and optional amount from the first argument
    # sys.argv[1] would be something like "deposit:50" or "display"
    parts = sys.argv[1].split(':')
    command = parts[0].strip().lower() # Get the command (e.g., 'deposit', 'withdraw', 'display')

    # Extract the amount if available (for 'deposit' or 'withdraw')
    amount = None
    if len(parts) > 1:
        try:
            amount = float(parts[1]) # Convert the amount part to a float
        except ValueError:
            print(f"Error: Invalid amount '{parts[1]}'. Please enter a numeric value.")
            sys.exit(1) # Exit if amount is not a valid number

    # Perform the banking operation based on the command
    if command == "deposit":
        if amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Error: Deposit command requires an amount (e.g., deposit:50).")
            sys.exit(1)
    elif command == "withdraw":
        if amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Error: Withdraw command requires an amount (e.g., withdraw:20).")
            sys.exit(1)
    elif command == "display":
        if amount is None: # Ensure no extra amount is passed for display
            account.display_balance()
        else:
            print("Error: Display command does not take an amount (e.g., display).")
            sys.exit(1)
    else:
        print(f"Invalid command: '{command}'. Valid commands are deposit, withdraw, display.")
        sys.exit(1)

# This ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()