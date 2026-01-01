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

import shopping_list_manager

def main():
    shopping_list = []
    
    print("Welcome to Shopping List Manager!\n")
    
    while True:
        shopping_list_manager.display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            shopping_list_manager.add_item(shopping_list)
            
        elif choice == '2':
            shopping_list_manager.remove_item(shopping_list)
            
        elif choice == '3':
            shopping_list_manager.view_list(shopping_list)
            
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()