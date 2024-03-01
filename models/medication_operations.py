#!/bin/usr/python3
"""medication_operations.py"""
from db_connection import session  # Import your database session
from models import Medication  # Import the Medication model (adjust the import path as needed)

def add_medication(poultry_id, medication_name, dosage, administration_time):
    """Adds a new medication record to the database."""
    new_medication = Medication(
        poultry_id=poultry_id,
        medication_name=medication_name,
        dosage=dosage,
        administration_time=administration_time
    )
    session.add(new_medication)
    session.commit()

def get_medication_history(poultry_id):
    """Retrieves medication history for a specific bird."""
    # Implement the query to retrieve medication records for the given poultry_id
    # Return the results as needed

# Add other medication-related functions (update, delete, etc.) as required

# Example usage:
if __name__ == "__main__":
    # Test adding a medication record
    add_medication(poultry_id=1, medication_name="Antibiotic", dosage=10, administration_time="2024-03-01T10:00:00.000000")
