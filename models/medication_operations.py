#!/bin/usr/python3
from sqlalchemy import Column, String
import models
from models.base_model import BaseModel
"""medication_operations.py"""
class Medication(BaseModel):
    __tablename__ = "medication"
    poultry_id = Column(String(60), nullable=True)
    medicine = Column(String(128), nullable=False)
    Poultry_class = Column(String(60), nullable=False)
    def __init__(self, *args, **kwargs):
        """initialize medication"""
        super().__init__(*args, **kwargs)