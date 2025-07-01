# bank_account.py

class BankAccount:
    """
    A simple bank account class that encapsulates banking operations.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes a new BankAccount object with an optional initial balance.

        Args:
            initial_balance (float): The starting balance for the account. Defaults to 0.0.
        """
        # Encapsulation: The account_balance is an internal attribute.
        # It should only be modified via deposit/withdraw methods.
        if initial_balance < 0:
            print("Warning: Initial balance cannot be negative. Setting to 0.0.")
            self._account_balance = 0.0 # Use _ for convention, indicating it's intended for internal use
        else:
            self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False # Indicate failure
        self._account_balance += amount
        # print(f"Successfully deposited ${amount:.2f}.") # Optional: print confirmation within method
        return True # Indicate success

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds or invalid amount).
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self._account_balance >= amount:
            self._account_balance -= amount
            # print(f"Successfully withdrew ${amount:.2f}.") # Optional: print confirmation within method
            return True
        else:
            # print("Insufficient funds for withdrawal.") # Optional: print message within method
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")