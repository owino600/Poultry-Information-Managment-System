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
        
    def calculate_total_revenue(self, unit_price, quantity_sold):
        """
        Calculate total revenue for a product sale.

        Args:
            unit_price (float): Price per unit of the product.
            quantity_sold (int): Number of units sold.

        Returns:
            float: Total revenue from the sale.
        """
        return unit_price * quantity_sold

# Example usage:
if __name__ == "__main__":
    # Create a sales record
    sale = Sales(product_id="123", product_name="Chicken Feed", product_type="Feed")
    unit_price = 10.0  # Price per bag of chicken feed
    quantity_sold = 50  # Number of bags sold

    total_revenue = sale.calculate_total_revenue(unit_price, quantity_sold)
    print(f"Total revenue from sales: ${total_revenue:.2f}")