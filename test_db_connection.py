import MySQLdb
import sys

# Database credentials - ENSURE THESE MATCH YOUR settings.py EXACTLY
DB_CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'mydatabaseuser',
    'passwd': 'Keeona+kayla#kian@23',
    'db': 'mydatabase',
}

try:
    # Attempt to connect to the MySQL database
    conn = MySQLdb.connect(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        user=DB_CONFIG['user'],
        passwd=DB_CONFIG['passwd'],
        db=DB_CONFIG['db']
    )
    print("Successfully connected to MySQL database!")
    conn.close()
    print("Connection closed.")
except MySQLdb.Error as e:
    print(f"Error connecting to MySQL: {e}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)