#!/usr/bin/python3
import models
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, DateTime, Float, Enum
class Sales(BaseModel):
    __tablename__= 'product_sales'
    Sales_id = Column(Integer(), nullable=False)
    sales_date = Column(DateTime, default=models.base_model.datetime.utcnow)
    buyer_name = Column(String(60), nullable=False)
    poultry_id = Column(Integer(), nullable=False)
    quantity = Column(Integer(), nullable=False)
    unit_price = Column(Float(18,0), nullable=False)
    total_price = Column(Float(18,0), nullable=False)
    payment_method = Column(Enum('Cash', 'Credit', 'Debit', 'Online Transfer', 'Check'), nullable=False)
    
    
    def __init__(self, *args, **kwargs):
        """initialize sales"""
        super().__init__(*args, **kwargs)
        
    def calculate_total_revenue(self, unit_price, quantity_sold):
        """
        Calculate total revenue for a product sale.

        Args:
            unit_price (float): Price per unit of the product.
            quantity_sold (int): Number of units sold.

        Returns:
            float: Total revenue from the sale.
        """
        self.unit_price = unit_price
        self.quantity_sold = quantity_sold
        
        return unit_price * quantity_sold