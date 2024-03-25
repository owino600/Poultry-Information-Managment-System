#!/bin/usr/python3
""" poultry management console"""
import models

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
    session = models.DBStorage()
    """Query all sales"""
    sales = session.all(models.Sales)
    
    """Print each sale"""
    for sale in sales.values():
        print(f"Sales ID: {sale.Sales_id}")
        print(f"Sales Date: {sale.sales_date}")
        print(f"Buyer Name: {sale.buyer_name}")
        print(f"Poultry ID: {sale.poultry_id}")
        print(f"Quantity: {sale.quantity}")
        print(f"Unit Price: {sale.unit_price}")
        print(f"Total Price: {sale.total_price}")
        print(f"Payment Method: {sale.payment_method}")
        print("------------------------")
        pass
def view_medication_operations():
    # Use your Medication class here
    pass
if __name__ == "__main__":
    main()
