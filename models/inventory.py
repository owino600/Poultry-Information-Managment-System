#!/usr/bin/python3
""" track the poultry cycle from birth to ready market"""
from datetime import datetime

import models
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, DateTime, Float, Text

class Inventory(BaseModel):
    __tablename__= 'product_sales'
    Product_id = Column(Integer(), primary_key=True, nullable=False)
    Product_name = Column(String(60), nullable=False)
    Category= Column(Integer(), nullable=False)
    Description = Column(Text(200), nullable=True)
    quantity = Column(Integer(), nullable=False)
    unit_price = Column(Float(50), nullable=False)
    supplier = Column(String(128), nullable=True)
    date_received = Column(DateTime, default=models.base_model.datetime.utcnow)
    Expiration_date = Column(DateTime, default=models.base_model.datetime.utcnow)