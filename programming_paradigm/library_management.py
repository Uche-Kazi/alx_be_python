# library_management.py

class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        # Private attribute to track availability, defaults to False (not checked out)
        self._is_checked_out = False

    def check_out(self):
        """
        Marks the book as checked out.

        Returns:
            bool: True if the book was successfully checked out, False if it was already checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            # print(f"'{self.title}' has been checked out.") # Optional: for internal confirmations
            return True
        else:
            # print(f"'{self.title}' is already checked out.")
            return False

    def return_book_instance(self):
        """
        Marks the book as available (returned).

        Returns:
            bool: True if the book was successfully returned, False if it was not checked out.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            # print(f"'{self.title}' has been returned.") # Optional: for internal confirmations
            return True
        else:
            # print(f"'{self.title}' was not checked out.")
            return False

    def is_available(self):
        """
        Checks if the book is currently available in the library.

        Returns:
            bool: True if the book is not checked out, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        Used when printing the book.
        """
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        """
        Defines equality comparison for Book objects, useful for finding books.
        Two books are considered equal if they have the same title and author.
        """
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    def __hash__(self):
        """
        Defines a hash for Book objects, necessary if using Books in sets or as dictionary keys.
        """
        return hash((self.title, self.author))


class Library:
    """
    Manages a collection of books, allowing adding, checking out, returning,
    and listing available books.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = [] # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): An instance of the Book class to be added.
        """
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return
        # Optional: Prevent adding the same book (title and author) multiple times
        # if book in self._books:
        #     print(f"Book '{book.title}' by {book.author} already exists in the library.")
        #     return
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def check_out_book(self, title):
        """
        Finds a book by its title and marks it as checked out if available.

        Args:
            title (str): The title of the book to check out.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.is_available():
                    book.check_out() # Call the book's method to change its state
                    print(f"Successfully checked out '{title}'.")
                    return True
                else:
                    print(f"'{title}' is currently checked out and cannot be checked out again.")
                    return False
        if not found:
            print(f"'{title}' not found in the library.")
        return False

    def return_book(self, title):
        """
        Finds a book by its title and marks it as available (returned).

        Args:
            title (str): The title of the book to return.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if not book.is_available(): # Check if it's currently checked out
                    book.return_book_instance() # Call the book's method to change its state
                    print(f"Successfully returned '{title}'.")
                    return True
                else:
                    print(f"'{title}' was not checked out, so it cannot be returned.")
                    return False
        if not found:
            print(f"'{title}' not found in the library.")
        return False

    def list_available_books(self):
        """
        Prints the titles and authors of all books currently available in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available in the library.")
            return

        for book in available_books:
            print(book) # Uses the Book's __str__ method for nice printing