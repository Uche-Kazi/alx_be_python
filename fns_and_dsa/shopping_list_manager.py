def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    """
    Manages the shopping list by continuously displaying options
    and performing actions based on user input.
    """
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
           
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")

        elif choice == '2':
            
            if not shopping_list:
                print("Your shopping list is already empty. Nothing to remove.")
            else:
                item_to_remove = input("Enter the item to remove: ").strip()
                if item_to_remove:
                    try:
                        shopping_list.remove(item_to_remove)
                        print(f"'{item_to_remove}' has been removed from your shopping list.")
                    except ValueError:
                        
                        print(f"'{item_to_remove}' was not found in your shopping list.")
                else:
                    print("Item name cannot be empty. Please try again.")

        elif choice == '3':
            
            if not shopping_list:
                print("\nYour shopping list is currently empty.")
            else:
                print("\n--- YOUR CURRENT SHOPPING LIST ---")
                
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("----------------------------------")

        elif choice == '4':
            
            print("Exiting Shopping List Manager. Goodbye!")
            break

        else:
            
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()