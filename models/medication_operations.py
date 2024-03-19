#!/usr/bin/python3
from sqlalchemy import Column, String, DateTime, Integer
from models.base_model import BaseModel
import models
"""medication_operations.py"""


class Medication(BaseModel):
    __tablename__ = "medication"
    poultry_id = Column(String(60), nullable=True)
    species = Column(String(60), nullable=False)
    quantity = Column(
            Integer(), nullable=False)
    ageweeks = Column(
            Integer(), nullable=False)
    dateofmedication = Column(
            DateTime, default=models.base_model.datetime.utcnow)
    medecation_name = Column(String(128), nullable=False)
    dosage = Column(String(50), nullable=False)
    medicationtype = Column(String(50), nullable=False)
    withdrawalperiod = Column(String(128), nullable=False)
    supplier = Column(String(128), nullable=True)
    cost = Column(Integer(), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize medication"""
        super().__init__(*args, **kwargs)
