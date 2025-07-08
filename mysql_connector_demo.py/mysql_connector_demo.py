import mysql.connector
from mysql.connector import Error # Import Error for specific exception handling

# --- Connection Attempt ---
mydb = None # Initialize mydb to None
mycursor = None # Initialize mycursor to None

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Keeona+kayla#kian@23",
        database="students"
    )

    if mydb.is_connected():
        # If we reach here, the connection was successful
        print(f"Successfully connected to MySQL Server version: {mydb.server_info}")
        print("Database connection established successfully!")

        # You can also try to create a cursor to further confirm
        mycursor = mydb.cursor()
        print("Cursor created successfully.")

        # Example: Execute a simple query to prove connection is active
        mycursor.execute("SELECT DATABASE();")
        db_name = mycursor.fetchone()[0]
        print(f"Currently connected to database: {db_name}")

    else:
        # This block would typically not be reached if connect() fails,
        # as an exception would be raised. But it's good for clarity.
        print("Failed to connect to the database.")

except Error as e:
    # This block catches any errors during the connection attempt or subsequent operations
    print(f"Error connecting to MySQL database: {e}")

finally:
    # --- Cleanup ---
    # Ensure cursor and connection are closed, even if errors occurred
    if mycursor:
        mycursor.close()
        print("Cursor closed.")
    if mydb and mydb.is_connected():
        mydb.close()
        print("MySQL connection closed.")