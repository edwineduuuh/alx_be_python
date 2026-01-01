# from arithmetic_operations import perform_operation

# def main():
#     print("Arithmetic Operations")
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

#     result = perform_operation(num1, num2, operation)
#     print(f"Result: {result}")

# if __name__ == "__main__":
#     main()

# main.py
# This is the entry point that uses the module

import shopping_list_manager

def run_shopping_list():
    shopping_list = []
    
    while True:
        shopping_list_manager.display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.\n")
            else:
                print("No item entered.\n")

        elif choice == '2':
            if not shopping_list:
                print("List is empty - nothing to remove.\n")
            else:
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' removed from the list.\n")
                else:
                    print("Item not found.\n")

        elif choice == '3':
            print("\nCurrent Shopping List:")
            if not shopping_list:
                print("   (empty)\n")
            else:
                for i, item in enumerate(shopping_list, 1):
                    print(f"   {i}. {item}")
                print()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    run_shopping_list()