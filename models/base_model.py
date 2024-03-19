#!/usr/bin/python3
"""Base_model"""
from datetime import datetime
import uuid
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

time_format = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object
    
class BaseModel:
    """The BaseModel class for poultry management"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            # Convert string timestamps to datetime objects
             # Convert string timestamps to datetime objects
            self.created_at = datetime.strptime(kwargs.get("created_at", datetime.utcnow().strftime(time_format)), time_format)
            self.updated_at = datetime.strptime(kwargs.get("updated_at", datetime.utcnow().strftime(time_format)), time_format)
            # Generate a new UUID if not provided
            self.id = kwargs.get("id", str(uuid.uuid4()))
        else:
            # Initialize with default values
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Converts the instance to a dictionary"""
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
            # Add other attributes specific to your project
        }

    # Add any other methods or features relevant to poultry management
    # ...

# Example usage:
if __name__ == "__main__":
    poultry = BaseModel(name="Chicken A", age_in_days=30, breed="Leghorn")
    print(poultry)
    poultry.save()
    print(poultry.to_dict())
