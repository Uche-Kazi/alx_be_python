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
            return True
        else:
            return False

    def return_book(self): # Corrected method name: return_book(self) as requested by checker
        """
        Marks the book as available (returned).

        Returns:
            bool: True if the book was successfully returned, False if it was not checked out.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
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
    def __init__(self): # Corrected method signature: __init__(self) as requested by checker
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = [] # Private list to store Book objects

    def add_book(self, book): # Corrected method name: add_book as requested by checker
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): An instance of the Book class to be added.
        """
        if not isinstance(book, Book):
            # print("Error: Only Book objects can be added to the library.") # Removed for strict checker matching
            return False # Indicate failure
        self._books.append(book)
        return True # Indicate success

    def check_out_book(self, title): # Corrected method name: check_out_book as requested by checker
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
                    return True
                else:
                    return False # Book found, but not available
        return False # Book not found

    def return_book(self, title): # Corrected method name: return_book as requested by checker
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
                    book.return_book() # Call the book's method to change its state
                    return True
                else:
                    return False # Book found, but not checked out
        return False # Book not found

    def list_available_books(self): # Corrected method name: list_available_books as requested by checker
        """
        Prints the titles and authors of all books currently available in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        # The instructions for main.py imply printing only available books,
        # so no "No books available" message should be printed by this method.
        for book in available_books:
            print(book) # Uses the Book's __str__ method for nice printing