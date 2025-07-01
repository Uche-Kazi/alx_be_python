from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains the current date and time, and prints it in a specific format.
    """
    current_date = datetime.now()

    formatted_current_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_datetime}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date
    by adding those days to the current date, and prints the result.
    """
    try:
        num_days_str = input("Enter the number of days to add to the current date: ")
        num_days = int(num_days_str)

        if num_days < 0:
            print("Please enter a non-negative number of days.")
            return

        current_date_only = datetime.now().date()

        future_date = current_date_only + timedelta(days=num_days)

        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter a whole number for the number of days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    display_current_datetime()

    calculate_future_date()