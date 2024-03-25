#!/usr/bin/python3
""" poultry management console"""
import models
from models import engine
from models.base_model import BaseModel, Base
from models.inventory import Inventory
from models.medication_operations import Medication
from models.sales import Sales


classes = {"Inventory": Inventory, "BaseModel": BaseModel, "Sales":Sales,
           "Medication": Medication}

if not isinstance(Base, object):
    Base.metadata.create_all(engine)

class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}
     
def main():
    while True:
        print("Welcome to the Poultry Information Management System (PIMS)")
        print("Please select an option:")
        print("1. View Inventory")
        print("2. View Sales")
        print("3. add Sales")
        print("4. View Medication Operations")
        print("5. Exit")

        option = input("> ")

        if option == "1":

            # Call the function to view inventory
            view_inventory()
        elif option == "2":
            # Call the function to view sales
            view_sales()
        elif option == "3":
            add_sale()
        elif option == "4":
            # Call the function to view medication operations
            view_medication_operations()
        elif option == "5":
            break
        else:
            print("Invalid option. Please try again.")
def view_inventory():
    # Use your Inventory class here
    pass
def add_sale():
    session = models.storage
    """Query all sales"""
    sales = session.all(models.sales)
    
    sales_id = input("Please enter the Sales ID: ")
    sales_date = input("Please enter the Sales Date: ")
    buyer_name = input("Please enter the Buyer Name: ")
    poultry_id = input("Please enter the Poultry ID: ")
    quantity = input("Please enter the Quantity: ")
    unit_price = input("Please enter the Unit Price: ")
    total_price = input("Please enter the Total Price: ")
    payment_method = input("Please enter the Payment Method: ")

    # Create a new Sale object
    new_sale = models.sales.Sales(sales_id=sales_id, sales_date=sales_date, buyer_name=buyer_name, poultry_id=poultry_id, quantity=quantity, unit_price=unit_price, total_price=total_price, payment_method=payment_method)

    # Add the new Sale object to the storage
    session.new(new_sale)
    session.save()
def view_sales():
    session = models.storage
    """Query all sales"""
    sales = session.all(models.sales.Sales)
    """Print each sale"""
    for sale in sales.values():
        print(f"Sales ID: {sale.sales_id}")
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
    session = models.storage

    # Query all medication operations
    medications = session.all(models.medication_operations)

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
