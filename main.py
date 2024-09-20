from cli import book_reservation, list_guests, list_inventory, assign_inventory_item, assign_task, checkout_guest

def cli():
    while True:
        print("\nThis is Serena Hotel Management System. Below are the functions for Serena:")
        print("1. Add a reservation")
        print("2. List guests")
        print("3. Assign inventory item to guest")
        print("4. List inventory")
        print("5. Assign task to staff")
        print("6. Checkout a guest")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_reservation()
        elif choice == "2":
            list_guests()
        elif choice == "3":
            assign_inventory_item()
        elif choice == "4":
            list_inventory()
        elif choice == "5":
            assign_task()
        elif choice == "6":
            checkout_guest()
        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    cli()

