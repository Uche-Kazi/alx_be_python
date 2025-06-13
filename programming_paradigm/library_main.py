# main.py

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("\nAvailable books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    print("\n--- Attempting to check out '1984' ---")
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate attempting to check out an unavailable book
    print("\n--- Attempting to check out '1984' again ---")
    library.check_out_book("1984")
    print("\nAvailable books after second checkout attempt:")
    library.list_available_books()

    # Simulate returning a book
    print("\n--- Attempting to return '1984' ---")
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

    # Simulate attempting to return an already available book
    print("\n--- Attempting to return '1984' (already available) ---")
    library.return_book("1984")
    print("\nAvailable books after second return attempt:")
    library.list_available_books()

    # Simulate checking out a non-existent book
    print("\n--- Attempting to check out 'The Great Gatsby' (non-existent) ---")
    library.check_out_book("The Great Gatsby")
    print("\nAvailable books after non-existent checkout attempt:")
    library.list_available_books()

    # Simulate returning a non-existent book
    print("\n--- Attempting to return 'Moby Dick' (non-existent) ---")
    library.return_book("Moby Dick")
    print("\nAvailable books after non-existent return attempt:")
    library.list_available_books()


if __name__ == "__main__":
    main()