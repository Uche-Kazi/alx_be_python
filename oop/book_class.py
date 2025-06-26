# book_class.py

class Book:
    """
    A class to represent a book, demonstrating Python's magic methods:
    __init__, __del__, __str__, and __repr__.
    """

    def __init__(self, title, author, year):
        """
        Constructor method: Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.") # Optional: Confirmation of creation

    def __del__(self):
        """
        Destructor method: Called when the Book object is about to be deleted or
        its reference count drops to zero.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation method: Provides an informal, human-readable
        string representation of the Book object. This is typically used by print().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation method: Provides an unambiguous, developer-friendly
        string representation that could (ideally) recreate the object.
        """
        # Using f-string to create a string that looks like a constructor call
        return f"Book('{self.title}', '{self.author}', {self.year})"