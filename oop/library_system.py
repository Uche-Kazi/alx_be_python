# library_system.py

class Book:
    """
    Base class representing a generic book in the library.
    Demonstrates basic attributes and a string representation.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        This will be the default format for a generic Book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and adds a file_size attribute.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes a new EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Overrides the __str__ method to include the file size specific to EBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a physical print book.
    Inherits from Book and adds a page_count attribute.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a new PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Overrides the __str__ method to include the page count specific to PrintBook.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Manages a collection of various types of books (Book, EBook, PrintBook).
    Demonstrates composition by holding instances of Book and its subclasses.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list to store books.
        """
        self.books = [] # This list will hold instances of Book, EBook, or PrintBook

    def add_book(self, book: Book):
        """
        Adds a book (can be Book, EBook, or PrintBook) to the library's collection.

        Args:
            book (Book): An instance of Book or any of its subclasses.
        """
        # Basic validation to ensure a Book type object is added
        if isinstance(book, Book):
            self.books.append(book)
            # print(f"Added '{book.title}' to the library.") # Optional: for verbose output
        else:
            print("Error: Only instances of Book or its subclasses can be added to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        Polymorphism ensures that the correct __str__ method (from Book, EBook, or PrintBook)
        is called for each object in the list.
        """
        if not self.books:
            print("The library is currently empty.")
            return

        for book in self.books:
            print(book) # This call will automatically use the correct __str__ method