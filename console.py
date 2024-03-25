#!/bin/usr/python3
""" poultry management console"""
def main():
    while True:
        print("Welcome to the Poultry Information Management System (PIMS)")
        print("Please select an option:")
        print("1. View Inventory")
        print("2. View Sales")
        print("3. View Medication Operations")
        print("4. Exit")

        option = input("> ")

        if option == "1":

            # Call the function to view inventory
            view_inventory()
        elif option == "2":
            # Call the function to view sales
            view_sales()
        elif option == "3":
            # Call the function to view medication operations
            view_medication_operations()
        elif option == "4":
            break
        else:
            print("Invalid option. Please try again.")
            def view_inventory():
                # Use your Inventory class here
                pass
            def view_sales():
                # Use your Sales class here
                pass
            def view_medication_operations():
                # Use your Medication class here
                pass
            if __name__ == "__main__":
                main()
