def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter item to add: ").strip()
    if item:
        if item.lower() in [x.lower() for x in shopping_list]:
            print(f"{item} already in shopping list")
        else:
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list")
    else:
        print("Nothing entered.")

def remove_item(shopping_list):
    if not shopping_list:
        print("List is empty, nothing to remove")
        return
    item = input("Enter item to remove: ").strip()

    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} successfully removed from shopping list")
    else:
        print(f"{item} not found in list")

def view_list(shopping_list):
    print("\n Your shopping list: ")
    if not shopping_list:
        print(" (Empty)")
    else:
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
print()