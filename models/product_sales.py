#!/usr/bin/python3
import models
from models.base_model import BaseModel
from sqlalchemy import Column, String
class Sales(BaseModel):
    __tablename__= 'product_sales'
    product_id = Column(String(60), nullable=False)
    product_name = Column(String(60), nullable=False)
    product_type = Column(String(128), nullable=False)
    def __init__(self, *args, **kwargs):
        """initialize sales"""
        super().__init__(*args, **kwargs)