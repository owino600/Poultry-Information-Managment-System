#!/bin/usr/python3
""" track the poultry cycle from birth to ready market"""
from datetime import datetime

class Time():
    def __init__(self):
        dt = datetime.utcnow()
        dt = "{}{}{}{}{}{}".format(dt.day, dt.month, dt.year, dt.hour, dt.min, dt.second)
print("Projected time")