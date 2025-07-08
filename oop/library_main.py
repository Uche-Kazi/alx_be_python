# library_main.py

# Import all necessary classes from the library_system module
from library_system import Book, EBook, PrintBook, Library

def main():
    """
    Main function to demonstrate the Library Management System.
    Creates different book types, adds them to a library, and lists them.
    """
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    print("--- Creating Book Instances ---")
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    print("\n--- Adding Books to Library ---")
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    print("\n--- Listing All Books in Library ---")
    my_library.list_books()

    # Optional: Demonstrate adding an invalid object
    # print("\n--- Attempting to add an invalid object ---")
    # my_library.add_book("Not a book string")
    # print("\n--- Listing All Books after invalid add attempt ---")
    # my_library.list_books()


if __name__ == "__main__":
    main()