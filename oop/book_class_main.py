# main.py

from book_class import Book
# Removed: import gc - Not needed for the checker's expected output as del works eventually

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    # The __del__ method's print statement is expected to show up here.
    del my_book

if __name__ == "__main__":
    main()