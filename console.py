#!/bin/usr/python3
""" poultry management console"""
from models.engine.db_storage import DBStorage
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
    session = models.DBStorage()

    # Query all medication operations
    medications = session.all(models.Medication)

    # Print each medication operation
    for medication in medications.values():
        print(f"Poultry ID: {medication.poultry_id}")
        print(f"Species: {medication.species}")
        print(f"Quantity: {medication.quantity}")
        print(f"Age in Weeks: {medication.ageweeks}")
        print(f"Date of Medication: {medication.dateofmedication}")
        print(f"Medication Name: {medication.medecation_name}")
        print(f"Dosage: {medication.dosage}")
        print(f"Medication Type: {medication.medicationtype}")
        print(f"Withdrawal Period: {medication.withdrawalperiod}")
        print(f"Supplier: {medication.supplier}")
        print(f"Cost: {medication.cost}")
        print("------------------------")
    pass
if __name__ == "__main__":
    main()
